import time
import subprocess
import sys

#add test items to list
src_dst_list = []
src_dst_list.append(['Chicago Cubs', 'Wrigley Field']) # 1
src_dst_list.append(['University of Notre Dame', 'Knute Rockne']) #1
src_dst_list.append(['Chocolate', 'Brain']) #2
src_dst_list.append(['Orange (fruit)', 'Purple']) #2
src_dst_list.append(['Telephone', 'Whistle']) #3
src_dst_list.append(['Peanuts', 'George H W Bush']) #3
src_dst_list.append(['Peanut', 'Cupcake']) #4
src_dst_list.append(['Adele', 'Malik Zaire']) #4
src_dst_list.append(['Somali lark', 'Battle of Great Bridge']) #4
src_dst_list.append(['Mirror Image', 'Dell']) #4
src_dst_list.append(['Socks', 'Wierd Al']) #5
src_dst_list.append(['Telephone', 'Grasshopper']) #7
src_dst_list.append(['Jesus', 'Johnnie Cochran']) #21

print "| Source                         | Destination                    | #Links, Time(1) | #Links, Time(2) | #Links, Time(3) | Average    | "
print "|--------------------------------|--------------------------------|-----------------|-----------------|-----------------|------------|"

for pair in src_dst_list:
    command = 'python wikipedia-bot.py "' + pair[0] + '" "' + pair[1] + '"'
    string = "| " + pair[0].encode("utf-8") + " "*(30-len(pair[0])) + " | " + pair[1].encode("utf-8") + " "*(30-len(pair[1])) + " |"
    sys.stdout.write(string)

    timeSum = 0
    distanceSum = 0

    for i in xrange(3):
        start = time.time()
        output = subprocess.check_output(command, shell=True)
        end = time.time()

        timeElapsed = end-start
        timeSum += timeElapsed

        distance = output.split("Distance:")[1].split()[0]
        distanceSum += int(distance)

        sys.stdout.write(' ' + distance + ", " + str((timeElapsed))[:7] + '      |')
    
    avgTime = timeSum/3
    avgDistance = distanceSum/3

    print ' ' + str(avgDistance) + ', ' + str(avgTime)[:7] + ' |'
