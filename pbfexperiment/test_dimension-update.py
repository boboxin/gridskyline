# Test different data dimension
# Data: 1000 records, possible instance = 5, radius = 5
# Data: dimension from 2 to 10
# Sliding window = 300
import os, sys
sys.path.append(os.path.abspath(os.pardir))

import time

# from .. import PBF
from PBF import pbfsky, batchImport,gravity


def dim_time():
    print("=== Test how dimension of data affect running time ===")
    dim = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    for d in dim:
        path = 'pdfex_dim_result-nosk2.txt'
        f = open(path,'a+')
        indata = batchImport('10000_dim'+str(d)+'_pos5_rad5_01000.csv', 5)
        dqueue = indata[0] #turn inputlist to dqueue
        locatlist = indata[1] #location for
        
        print('========== Data dimension = '+ str(d) + ' ==========')
        print('---------- Brute force ----------')
        tbsky = pbfsky(10000,d, 5, 5, [0,1000], wsize=300)
        
        start_time = time.time()

        for i in range(10000):
            tbsky.receiveData(dqueue[i],locatlist[i])
            tbsky.updateSkyline()
        dtime1 = time.time() - start_time
        print("--- %s seconds ---" % (dtime1))
        f.write('========== Data dimension = {a} ==========\n' . format(a=tbsky.dim))
        f.write('dimension:{a} ; time:{b}\n'.format(a=tbsky.dim,b= dtime1))
        
def dim_avgsk():
    print("=== Test how dimension of data affect candidate size ===")
    dim = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for d in dim:
        path = 'pdfex_dim_result-nosk2.txt'
        path2 = 'pdfex_dim_skresult.txt'
        f = open(path,'a+')
        f2 = open(path2,'a+')
        indata = batchImport('10000_dim'+str(d)+'_pos5_rad5_01000.csv', 5)
        dqueue = indata[0] #turn inputlist to dqueue
        locatlist = indata[1] #location for
        
        print('========== Data dimension = '+ str(d) + ' ==========')
        print('---------- Brute force ----------')
        tbsky = pbfsky(10000,d, 5, 5, [0,1000], wsize=300)
        f2.write('========== Data dimension = {a} ==========\n' . format(a=tbsky.dim))
        avgsk1, avgsk2 = 0, 0
        for i in range(10000):
            tbsky.receiveData(dqueue[i],locatlist[i])
            tbsky.updateSkyline()
            avgsk1 += len(tbsky.getSkyline())
            f2.write('\n========== time slot = {a} ==========\n' . format(a=i))
            f2.write('skyilne size : {a}\n'  . format(a=len(tbsky.getSkyline())))
            for s1 in tbsky.getSkyline():
                f2.write('{a}\n'  . format(a=s1))
            # avgsk2 += len(tbsky.getSkyline2())
        # tbsky.removeRtree()
        avgsk1 = avgsk1/10000
        # avgsk1, avgsk2 = avgsk1/10000, avgsk2/10000
        print('Avg. sky1: '+ str(avgsk1))
        # print('Avg. sky2: '+ str(avgsk2))
        f.write('========== Data dimension = {a} ==========\n' . format(a=tbsky.dim))
        f.write('Avg. sky1:{a} \n'.format(a=avgsk1))
        
if __name__ == '__main__':
    print("1: Test time\n2: Test average skyline size \n3: Run all test")
    switch = int(input('Choose your test: '))
    if switch == 1: # test time
        dim_time()
    elif switch == 2: # test avg sky
        dim_avgsk()
    elif switch == 3:
        dim_time()
        dim_avgsk()
    else:
        print('error')
