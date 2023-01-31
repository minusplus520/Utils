#!/bin/sh



shell_postfix="csh"
find_zebu_env() {
    local sandbox_path=$1
    if [[ -f $sandbox_path/release/zebu_env.${shell_postfix} ]]; then
        echo $sandbox_path/release/zebu_env.${shell_postfix}
    elif [[ -f $sandbox_path/zebu_env.${shell_postfix} ]]; then
        echo $sandbox_path/zebu_env.${shell_postfix}
    else
        local base=$(basename $sandbox_path 2> /dev/null)
        if [[ -f $sandbox_path/$base/zebu_env.${shell_postfix} ]]; then
            echo $sandbox_path/$base/zebu_env.${shell_postfix} 
        else
            echo ""
        fi
    fi
}
check_release() {
    local sandbox_path=$1
    local zebu_env=$(find_zebu_env $sandbox)
    if [[ $zebu_env != "" ]]; then
        echo $sandbox_path
    else
        echo ""
    fi
}


legal_sandbox_root_array_with_prefix=()
append_sandbox_array() {
    local prefix=$1
    shift
    local sandbox_roots=$@
    for sandbox in ${sandbox_roots}
    do
        local root=$(check_release $sandbox)
        if [[ $root != "" ]]; then
            legal_sandbox_root_array_with_prefix+="$prefix:$root "
        fi
    done
}

add_user_clients() {
    # add p4 client
    local clients_root=($(p4 clients -u ${USER} | awk '{print $5}'))
    local tmp=${clients_root[@]}
    for client_root in ${tmp}
    do
        if [[ -f ${client_root}/.vgp4linklist ]]; then
            clients_root+=($(cat ${client_root}/.vgp4linklist | awk '{print $6}'))
        fi
    done
    append_sandbox_array client ${clients_root[@]}
}

get_all_nightly() {
    release="/remote/vgzeburelease3/zebu_nightly"
    local postfix=$1
    local after_array=()

    if [[ -d ${release}/$1 ]] ; then
        local TD_sandbox_root=$(/bin/ls -l ${release}/$1 | /bin/grep -v -- '->' | awk '{print $9}')
        for i in ${TD_sandbox_root}
        do
            after_array+="${release}/$postfix/${i} "
        done
    fi


    build="/remote/vtgimages/SAFE"
    after_array+="${build}/$postfix"

    echo $after_array
}
add_nightly_release() {
    local title=$1
    local prefix=$2
    local arr=$(get_all_nightly $prefix)
    append_sandbox_array $title ${arr[@]}
}

print_all_legal_sandbox() {
    echo "Other: Manually Input"
    local tmp=${legal_sandbox_root_array_with_prefix}
    for legal in ${tmp}
    do
       echo ${legal/:/: }
    done
}

select_sandbox() {
    local tmp_FZF=$FZF_DEFAULT_OPTS
    export FZF_DEFAULT_OPTS='--height 40% --layout=reverse -m --border --ansi'

    local sandbox=$(print_all_legal_sandbox | /remote/us01home50/chielin/.fzf/bin/fzf | awk '{print $2}')
    if [[ $sandbox == "Manually" ]]; then
        echo "Enter a sandbox path" >> /dev/stderr
        read -r line
        sandbox=${line}
    fi
    echo $sandbox

    export FZF_DEFAULT_OPTS=${tmp_FZF}
}

main() {

    local shell=$1
    if [[ $shell != "" ]]; then
        shell_postfix=$shell
    fi
    echo "Target SHELL: $shell_postfix" >> /dev/stderr

    source /remote/vgrnd106/chielin/bin/p4_util/sourceP4IfNeeded
    add_user_clients
    add_nightly_release TD linux64_TD
    add_nightly_release VCS2109 linux64_VCS2021.09
    add_nightly_release ZEBU2003 linux64_ZEBU2020.03

    selected_sandbox=$(select_sandbox)
    zebu_env_path=$(find_zebu_env $selected_sandbox)
    if [[ $zebu_env_path != "" ]]; then
        echo "source $zebu_env_path" >> /dev/stderr
    else
        echo "zebu_env.bash is not existed in the sandbox '$selected_sandbox', please check your sandbox or input." >> /dev/stderr
    fi

    echo $zebu_env_path

}

main $@
