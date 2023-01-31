filename=${1}
zipName=${1}.gz

mv ${1} $zipName
gunzip $zipName
