_f100=15
_current=0
echo ""
printf '\e[1;34m%-6s\e[m' "Spawning Containers"
echo "
"
tput civis
stty -echo
CleanUp () {
   tput cnorm
   stty echo
}
trap CleanUp EXIT
docker-topo --create my-topology.yml > /dev/null 2>&1 &
ProgressBar () {
    _percent=$(("${1}*100/${_f100}*100"/100))
    _progress=$(("${_percent}*4"/10))
    _remainder=$((40-_progress))
    _completed=$(printf "%${_progress}s")
    _left=$(printf "%${_remainder}s")
    printf "\rProgress : [${_completed// /#}${_left// /-}] ${_percent}%%"
}
while [ "${_current}" -lt "${_f100}" ]
do
    sleep 1
    _current=$(docker ps -q | wc -l)
    ProgressBar "${_current}"
done
echo "
"
printf '\e[0;32m%-6s\e[m' "$(tput bold)Containers are Ready!!"
echo "
"
# EOF