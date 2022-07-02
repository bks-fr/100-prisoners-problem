import numpy as np
from numpy.random import default_rng
rng = default_rng()

prisoners_total = 100


def seed_boxes(prisoners_total):
    prisoners_total
    global asource
    global abox
    for i in range(1,prisoners_total+1):
        n=len(asource)
        if n == 1 :
            box=1
        else :
            box=rng.integers(1,n+1)
        # print("i={},n={},box={}".format(i,n,box))
        # print(asource)
        abox[i-1]=asource[box-1]
        asource = np.delete(asource,box-1)

def run_group(prisoners_total,abox):
    group_success = 0
    for prisoner in range (1,prisoners_total+1):
        tries=50
        prisoner_success = 0
        next_box = prisoner
        for i in range(1,tries+1):
            if abox[next_box-1] == prisoner :
                group_success = group_success + 1
                prisoner_success = 1
                break
            else:
                next_box = abox[next_box-1]
        if prisoner_success == 0:
            break
    if group_success == prisoners_total:
        return 1
    else:
        return 0

num_runs = 4000
num_success = 0
for i in range(1,num_runs+1):
    asource = np.arange(1,prisoners_total+1)
    abox = np.zeros((prisoners_total,), dtype=int)
    seed_boxes(prisoners_total)
    num_success+=run_group(prisoners_total,abox)
    print("Runs:{},Success:{},Percentage:{}".format(i,num_success,100*num_success/i), end="\r")
print('') 
