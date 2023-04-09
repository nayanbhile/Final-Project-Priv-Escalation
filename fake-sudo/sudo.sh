i="";
for argument in "$@" 
do
    
    i+="${argument} ";
done

echo "$i"