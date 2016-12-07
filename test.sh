timeout1=15
timeout2=30
timeout3=45


#test correctness
echo "Testing Correctness"
command=`python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" | tail -n 1`
output="Distance: 1 | Evansville, Indiana -> Bosse Field"
diff <(echo "$command") <(echo "$output")

command=`python wikipedia-bot.py "University of Notre Dame" "Knute Rockne" | tail -n 1`
output="Distance: 1 | University of Notre Dame -> Knute Rockne"
diff <(echo "$command") <(echo "$output")


#test performance
echo "Testing Articles 1 Link Apart with Timeout of $timeout1 seconds"
timeout $timeout1 python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" > /dev/null 2>&1

echo "Testing Articles 2 Links Apart with Timeout of $timeout2 seconds"
timeout $timeout2 python wikipedia-bot.py "chocolate" "brain" > /dev/null 2>&1

echo "Testing Articles 3 Links Apart with Timeout of $timeout3 seconds"
timeout $timeout3 python wikipedia-bot.py "Bob Ross" "red" > /dev/null 2>&1
