import time
import subprocess

src_dst_list = []
src_dst_list.append(['chocolate', 'brain'])
src_dst_list.append(['orange (fruit)', 'purple'])

print "| Source | Destination | # Link Separation | Elapsed Time "

for pair in src_dst_list:
    command = 'python wikipedia-bot.py "' + pair[0] + '" "' + pair[1] + '"'
    start = time.time()
    output = subprocess.check_output(command, shell=True)
    distance = output.split("Distance:")[1].split()[0]
    end = time.time()
    print "| " + pair[0] + " | " + pair[1] + " | " + distance + " | " + str((end-start)) + ' s'
