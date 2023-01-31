mkdir $1

cp zTopBuild.log $1/
cp zTime* $1/
cp -rf ztime* $1/


if [ $# -gt 1 ]; then
    cp zPar.log $1/
fi
