import numpy as np
lst=[]
for i in range(9):
    num=int(input())
    lst.append(num)
    
    
def calculate(lst):
    '''
    This functions converts list into a 3 by 3 array and then runs a series
    of operations on the array( mean, sum, max, min, standard deviation)
    '''
    try:
        aarray=np.array([lst[0:3],lst[3:6],lst[6:9]])
        dictii={'mean':[list(aarray.mean(axis=0)), list(aarray.mean(axis=1)), (aarray.mean())],
            'variance':[list(aarray.var(axis=0)), list(aarray.var(axis=1)), (aarray.var())],
            'standard deviation':[list(aarray.std(axis=0)), list(aarray.std(axis=1)), (aarray.std())],
            'max': [list(aarray.max(axis=0)), list(aarray.max(axis=1)), (aarray.max())],
            'min': [list(aarray.min(axis=0)), list(aarray.min(axis=1)), (aarray.min())],
            'sum': [list(aarray.sum(axis=0)), list(aarray.sum(axis=1)), (aarray.sum())]
            }
        return dictii
    except ValueError:
        print('List must contain nine numbers.')

ansers=calculate(lst)
print(ansers)