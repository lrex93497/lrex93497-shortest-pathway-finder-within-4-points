# As mininium steps is 5 steps, process from 7 steps to 5 step first for number of possible pathway, then try possible pathway.
# modified time_subpath for each value after ':' for the time, in both reverse and normal sequence
# release version 1.0

time_subpath = {'ab':5,'ba':5,'ra':2,'ar':2,'ac':4,'ca':4,'br':7,'rb':7,'cr':1,'rc':1,'bc':3,'cb':3}

import itertools
import numpy as np
import pprint
total_path = {}
weight_subpath = {}
map = ['r', 'a', 'b', 'c']
set_7 = ()  # this is set_7
set_6 = ()
set_5 = ()
path = {0: ['a', 'a', 'a', 'a', 'a', 'a', 'a']}
total_time = 0
shortest_time = 999999
shortest_pathway = {}
all_shortest_pathway_s = {}
all_shortest_pathway_s_count = 0

for p in itertools.product(map, repeat=7):
    set_7 += p

set_7 = np.array_split(set_7, 16384)

# Possbile Pathways filter for 7 step
a = 0
n = 0
end = 16384
while n < end:
    if set_7[n][0] != 'r' or set_7[n][-1] != 'r':
        del set_7[n]
        n -= 1
        end -= 1
    n += 1


n = 0
n1 = 0
end = len(set_7)
tamp = 0
while n < end:
    n1 = 0
    while n1 < 6:
        n2 = n1 + 1
        if set_7[n][n1] == set_7[n][n2] and set_7[n][n1] == 'r':
            del set_7[n]
            n -= 1
            end -= 1
            break
        n1 += 1
    n += 1



n = 0
n1 = 0
oper_a = False
end = len(set_7)
while n < end:
    n1 = 0
    oper_a = False
    while n1 < 6:
        if set_7[n][n1] == 'a':
            oper_a = True
            while True:
                n1 += 1
                if n1 == 7:
                    break
                if oper_a == True and set_7[n][n1] == 'a':
                    del set_7[n]
                    n -= 1
                    end -= 1
                    break
        if oper_a == True:
            break
        else:
            n1 += 1
    n += 1



n = 0
n1 = 0
oper_b = False
end = len(set_7)
while n < end:
    n1 = 0
    oper_b = False
    while n1 < 6:
        if set_7[n][n1] == 'b':
            oper_b = True
            while True:
                n1 += 1
                if n1 == 7:
                    break
                if oper_b == True and set_7[n][n1] == 'b':
                    del set_7[n]
                    n -= 1
                    end -= 1
                    break
        if oper_b == True:
            break
        else:
            n1 += 1
    n += 1


n = 0
n1 = 0
oper_c = False
end = len(set_7)
while n < end:
    n1 = 0
    oper_c = False
    while n1 < 6:
        if set_7[n][n1] == 'c':
            oper_c = True
            while True:
                n1 += 1
                if n1 == 7:
                    break
                if oper_c == True and set_7[n][n1] == 'c':
                    del set_7[n]
                    n -= 1
                    end -= 1
                    break
        if oper_c == True:
            break
        else:
            n1 += 1
    n += 1

#below is 6 steps

for p in itertools.product(map, repeat=6):
    set_6 += p

set_6 = np.array_split(set_6, 4096)

# Possbile Pathways filter for 6 step
a = 0
n = 0
end = 4096
while n < end:
    if set_6[n][0] != 'r' or set_6[n][-1] != 'r':
        del set_6[n]
        n -= 1
        end -= 1
    n += 1


n = 0
n1 = 0
end = len(set_6)
tamp = 0
while n < end:
    n1 = 0
    while n1 < 5:
        n2 = n1 + 1
        if set_6[n][n1] == set_6[n][n2] and set_6[n][n1] == 'r':
            del set_6[n]
            n -= 1
            end -= 1
            break
        n1 += 1
    n += 1



n = 0
n1 = 0
oper_a = False
end = len(set_6)
while n < end:
    n1 = 0
    oper_a = False
    while n1 < 5:
        if set_6[n][n1] == 'a':
            oper_a = True
            while True:
                n1 += 1
                if n1 == 6:
                    break
                if oper_a == True and set_6[n][n1] == 'a':
                    del set_6[n]
                    n -= 1
                    end -= 1
                    break
        if oper_a == True:
            break
        else:
            n1 += 1
    n += 1



n = 0
n1 = 0
oper_b = False
end = len(set_6)
while n < end:
    n1 = 0
    oper_b = False
    while n1 < 5:
        if set_6[n][n1] == 'b':
            oper_b = True
            while True:
                n1 += 1
                if n1 == 6:
                    break
                if oper_b == True and set_6[n][n1] == 'b':
                    del set_6[n]
                    n -= 1
                    end -= 1
                    break
        if oper_b == True:
            break
        else:
            n1 += 1
    n += 1


n = 0
n1 = 0
oper_c = False
end = len(set_6)
while n < end:
    n1 = 0
    oper_c = False
    while n1 < 5:
        if set_6[n][n1] == 'c':
            oper_c = True
            while True:
                n1 += 1
                if n1 == 6:
                    break
                if oper_c == True and set_6[n][n1] == 'c':
                    del set_6[n]
                    n -= 1
                    end -= 1
                    break
        if oper_c == True:
            break
        else:
            n1 += 1
    n += 1

#below is 5 steps

for p in itertools.product(map, repeat=5):
    set_5 += p

set_5 = np.array_split(set_5, 1024)

# Possbile Pathways filter for 5 step different from 5 and 6 no r check after r repetition but set[n][1,2,3] can't be r
a = 0
n = 0
end = 1024
while n < end:
    if set_5[n][0] != 'r' or set_5[n][-1] != 'r':
        del set_5[n]
        n -= 1
        end -= 1
    n += 1

a = 0
n = 0

while n < len(set_5):
    if set_5[n][1] == 'r' or set_5[n][2] == 'r' or set_5[n][3] == 'r':
        del set_5[n]
        n -= 1
        end -= 1
    n += 1

n = 0
n1 = 0
oper_a = False
end = len(set_5)
while n < end:
    n1 = 0
    oper_a = False
    while n1 < 4:
        if set_5[n][n1] == 'a':
            oper_a = True
            while True:
                n1 += 1
                if n1 == 5:
                    break
                if oper_a == True and set_5[n][n1] == 'a':
                    del set_5[n]
                    n -= 1
                    end -= 1
                    break
        if oper_a == True:
            break
        else:
            n1 += 1
    n += 1



n = 0
n1 = 0
oper_b = False
end = len(set_5)
while n < end:
    n1 = 0
    oper_b = False
    while n1 < 4:
        if set_5[n][n1] == 'b':
            oper_b = True
            while True:
                n1 += 1
                if n1 == 5:
                    break
                if oper_b == True and set_5[n][n1] == 'b':
                    del set_5[n]
                    n -= 1
                    end -= 1
                    break
        if oper_b == True:
            break
        else:
            n1 += 1
    n += 1


n = 0
n1 = 0
oper_c = False
end = len(set_5)
while n < end:
    n1 = 0
    oper_c = False
    while n1 < 4:
        if set_5[n][n1] == 'c':
            oper_c = True
            while True:
                n1 += 1
                if n1 == 5:
                    break
                if oper_c == True and set_5[n][n1] == 'c':
                    del set_5[n]
                    n -= 1
                    end -= 1
                    break
        if oper_c == True:
            break
        else:
            n1 += 1
    n += 1

total_path = len(set_5)+len(set_6)+len(set_7)
all_set = set_5 + set_6 + set_7

print('\nTotal possible pathway is {}'.format(total_path))
print('\nAll pathway display out -> {}'.format(all_set))

#double loop to try all possible pathway to found out 1st shortest pathway
n=0
n1=0
between=''
total_time = 0
shortest_time = 999999
shortest_pathway = []
while n < total_path:
    total_time = 0
    n1 = 0
    while n1 < len(all_set[n])-1:
        between = str(all_set[n][n1]+all_set[n][n1+1])
        total_time = time_subpath[between] + total_time
        if(n1 == len(all_set[n])-2):
            if shortest_time > total_time:
                shortest_time = total_time
                shortest_pathway = all_set[n]
        n1 += 1
    n += 1

print('\nShortest distance/time is {}.'.format(shortest_time))
print('\nAll possible shortest pathways is listed below:')

#loop for all possible outcome and print it out automatically
n=0
n1=0
between=''
total_time = 0
while n < total_path:
    total_time = 0
    n1 = 0
    while n1 < len(all_set[n])-1:
        between = str(all_set[n][n1]+all_set[n][n1+1])
        total_time = time_subpath[between] + total_time
        if(n1 == len(all_set[n])-2):
            if shortest_time == total_time:
                all_shortest_pathway_s = all_set[n]
                print(all_shortest_pathway_s)
                all_shortest_pathway_s_count +=1
        n1 += 1
    n += 1
print('There are total of {} shortest pathways'.format(all_shortest_pathway_s_count))


