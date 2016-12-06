#test correctness
echo "Testing Correctness"
command=`python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" | tail -n 1`
output="Distance: 1 | Evansville, Indiana -> Bosse Field"
diff <(echo "$command") <(echo "$output")

#test performance
echo "Testing Articles 1 Link Apart with Timeout of 10 seconds"
timeout 30 python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" > /dev/null 2>&1

echo "Testing Articles 2 Links Apart with Timeout of 20 seconds"
timeout 60 python wikipedia-bot.py "chocolate" "brain" > /dev/null 2>&1

echo "Testing Articles 3 Links Apart with Timeout of 30 seconds"
timeout 60 python wikipedia-bot.py "Bob Ross" "red" > /dev/null 2>&1
