import time
import subprocess
from pwn import *

# base_string = 'uscg{'
# ascii_int = 32 (this will go all the way up to 126
# for x in range(32,127):
#   print(chr(x))

# old code
# start_time = time.time()
# exec(open('pyshell.py').read())
# print('over')
# print('--- %s seconds ---' % (time.time() - start_time))



#range needs to be from 32-127
#proc.communicate needs to be base_string + str(x)
# if time of that run is longer than the saved run,
# concat x to base_string and 
# set saved run to this runs time

#will netcat running add to the time? add range so that the difference has to be larger than .25 or >=.25

base_string = 'uscg{'

# proc = subprocess.Popen('python pyshell.py', stdin=subprocess.PIPE, shell=True, encoding='utf8')
# start = time.time()
# proc.communicate(base_string+str(chr(31)))
# print(time.time() - start)

correct_end = 1.25

bob = True
while bob:
    if(base_string[-1] == ')'):
        print(base_string)
        break
    for x in range(32,44):
        proc = subprocess.Popen('python pyshell.py', stdin=subprocess.PIPE, shell=True, encoding='utf8')
        start = time.time()
        proc.communicate(str(base_string+chr(x)))
        end = time.time() - start
        print(end)
        if(end - correct_end >=.2):
            correct_end = end
            base_string = base_string+chr(x)
            break
        print(base_string+chr(x))
        print(end)
        print(correct_end)
        print(chr(x))
        # if proc.returncode:
            #continue
        # print("the flag was found")
        # print(base_string)
        # bob=False
        # break
