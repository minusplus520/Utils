echo "qstat:" > "/remote/us01home54/chenc/.aliasscript/qstat.log"
qstat | tee -a "/remote/us01home54/chenc/.aliasscript/qstat.log"
echo "Time:" >> "/remote/us01home54/chenc/.aliasscript/qstat.log"
date | tee -a "/remote/us01home54/chenc/.aliasscript/qstat.log"
