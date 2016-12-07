import time
import subprocess

src_dst_list = []
src_dst_list.append(['chicago cubs', 'wrigley field'])
src_dst_list.append(['university of notre dame', 'knute rockne'])
src_dst_list.append(['chocolate', 'brain'])
src_dst_list.append(['orange (fruit)', 'purple'])
src_dst_list.append(['angela merkel', 'peyton manning'])

print "| Source                         | Destination                    | # Link Separation | Elapsed Time "
print "-----------------------------------------------------------------------------------------------------"

for pair in src_dst_list:
    command = 'python wikipedia-bot.py "' + pair[0] + '" "' + pair[1] + '"'
    string = "| " + pair[0] + " "*(30-len(pair[0])) + " | " + pair[1] + " "*(30-len(pair[1])) + " | "
    print string
    for i in xrange(2):
        start = time.time()
        #print command
        output = subprocess.check_output(command, shell=True)
        distance = output.split("Distance:")[1].split()[0]
        end = time.time()
        print distance + "                 | " + str((end-start)) + ' s',
