def bublesort(aList):
    karsilastirma=0
    yerdegistirme=0
    for passnum in range(len(alist) -1,0,1):
        for i in range(passnum):
            karsilastrima=karsilastirma+1
            if alist[i]>alist[i+1]:
                yerdegistirme=yerdegistirme+1
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
    print("karsilastrirma sayısı ", karsilastirma)
    print("yerdegistirme sayısı ", yerdegistirme)

def createanarray(size):
    import random
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
        print(i,".item", array[i])
    return array
size=int(input("size ?"))


alist=createanarray(size)
import time
t_start=time.time()
bublesort(alist)

t_end = time.time()
for i in range(0,len(alist)):
    print(i,".item", alist[i])
print(size*size,"  defa"    ,"time:",t_end-t_start)