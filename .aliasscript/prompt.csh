# Add these lines to your ~/.cshrc.mine file on the linux grace machines...
# don't worry too much about what they mean.


# set prompt
set     red="%{\033[1;31m%}"
set   green="%{\033[1;32m%}"
set  yellow="%{\033[1;33m%}"
set    blue="%{\033[1;34m%}"
set magenta="%{\033[1;35m%}"
set    cyan="%{\033[1;36m%}"
set   white="%{\033[1;37m%}"
set     end="%{\033[0m%}"

#set prompt = "${blue}[%T] ${green}%B%n@%m:: ${cyan}%c05 ${white}%% %b${end}"
set prompt = "${blue}[%T] ${green}%B%n@%m:: ${cyan}%~ \n${white}%% %b${end}"

unset red green yellow blue magenta cyan yellow white end

bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

