i="";
for argument in "$@" 
do
    
    i+="${argument} ";
done

echo "python /tmp/sudo.py $i"