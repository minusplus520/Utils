#!/bin/csh


if ( "$1" == "" ) then
    echo "eg : zcuienv [env_file_name]"
    exit
endif

if ( ! -f "$1" ) then
    echo "file:$1 not exist"
    exit
endif

set file_conf=`grep -m 1 FILE_CONF $1`
echo $file_conf
$file_conf

set tg_comp=`grep -m 1 TG_COMP $1`
echo $tg_comp
$tg_comp

set remotesyn=`grep -m1 REMOTESYN $1`
echo $remotesyn
$remotesyn
