#!/usr/bin/env python

import random
import math

print 'Starting the program'

hcount = 0
tcount = 0
for i in range(1,5001):
    random_num = round(random.random())
    if random_num == 0:
        face = 'tail'
        tcount += 1
    else:
        face = 'head'
        hcount += 1
    print "Attempt #"+str(i)+": Throwing a coin...It's a "+face+"!...Got "+str(hcount)+" head(s) and "+str(tcount)+" tail(s) so far"

print 'Ending the program, thank you!'
