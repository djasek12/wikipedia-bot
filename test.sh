TIMEOUT=10

echo "Testing Correctness"
command=`python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" | tail -n 1`
output="Distance: 1 | Evansville, Indiana -> Bosse Field"
diff <(echo "$command") <(echo "$output")


command2=`python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" 2>&1`
echo "Testing Time with Timeout of $TIMEOUT seconds"
timeout $TIMEOUT python wikipedia-bot.py "Evansville, Indiana" "Bosse Field" > /dev/null 2>&1
