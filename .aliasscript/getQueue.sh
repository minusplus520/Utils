#!/bin/bash

usage()
{
    echo "Description:"
    echo "   Get the specified queue from zebuDev"
    echo
    echo "Usage:"
    echo "  $0 [options] "
    echo
    echo "  Options:"
    echo "    -h"
    echo "      print this help message"
    echo "    -m"
    echo "      minimum memory_free (Giga bytes) default: 0"
    echo "    -c"
    echo "      minimum m_core default: 0"
    echo "    -l"
    echo "      maximum load_average default: 99999"
}
load_average="99999"
m_core="0"
mem_free="0"
while getopts ":h:m:c:l:" option; do

  case $option in
    'h')  usage; exit;;
    'm')  mem_free=${OPTARG};;
    'l')  load_average=${OPTARG};;
    'c')  m_core=${OPTARG};;
    *)    exit;;
  esac
done

set -o xtrace
quser -P zebuDev -l mem_free=${mem_free}G,m_core=${m_core},la=${load_average}  | /u/chielin/.cargo/bin/rg " ok " | awk '{print $1}'| paste -sd ','


