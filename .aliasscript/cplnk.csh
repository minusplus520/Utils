#!/bin/csh


if ( "$1" == "" ) then
    echo "e.g.: cplnk [filename.zti]"
    exit
endif

mv $1 $1.ori
cp -rf $1.ori/ $1

