i="";
for argument in "$@" 
do
    
    i=$((i + argument)) + " ";
done

echo "$i"