#Sahil Raj
#21BCS3324


def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def tryPartition(a):
   
    n = len(a)
    pivot = a[n-1] 
    i,j = 0,0 
    for j in range(n-1):
        
        if a[j] <= pivot: 
            swap(a, i+1, j)
            i = i + 1
    swap(a, i+1, n-1)
    return i+1

def testIfPartitioned(a, k):

  
    res=True
    for idx in range(0, k): 
          if a[idx]>a[k]:
            res=False
            break
    for idx in range (k+1, len(a)): 
          if a[idx]<=a[k]:
            res=False
            break
    return res
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 10, 23],5) == True, ' Test # 1 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 11, 23],4) == False, ' Test # 2 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 23, 21],0) == True, ' Test # 3 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 22, 23],9) == True, ' Test # 4 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23],5) == False, ' Test # 5 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 13, 9, -11],5) == False, ' Test # 6 failed.'
assert testIfPartitioned([4, 4, 4, 4, 4, 8, 9, 13, 9, 11],4) == True, ' Test # 7 failed.'
print('Passed all tests (10 points)')


a1 = [1, 14, 5, 20, 4, 2, 54, 20, 87,98, 3, 1, 32]

assert( len(a1) > 0)

a2 = [-1, 5, 2, 3, 4, 8, 9, 14, 11, 23]

assert( len(a2) > 0)
assert (a1 != a2)


a3 = [-1, 5, 2, 3, 4, 8, 9, 13, 9, -11]

assert( len(a3) > 0)
assert (a3 != a2)
assert (a3 != a1)

def dummyFunction():
    pass

try:
    j1 = tryPartition(a1)
    assert not testIfPartitioned(a1, j1)
    print('Partitioning was unsuccessful - this is what you were asked to break the code')
except Exception as e: 
    print(f'Assertion failed {e} - this is fine since you were asked to break the code.')
    
try:
    j2 = tryPartition(a2)
    assert not testIfPartitioned(a2, j2)
except Exception as e: 
    print(f'Assertion failed {e} - this is fine since you were asked to break the code.')
    

try:
    j3 = tryPartition(a3)
    assert not testIfPartitioned(a3, j3)
except Exception as e: 
    print(f'Assertion failed {e} - this is fine since you were asked to break the code.')
    
dummyFunction()

print('Passed 5 points!')

def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def simplePartition(a, pivot):
   
    tail = len(a) - 1
    head = 0
    while True:
                
            if head >= tail:
                        # Print Pivot Info
                    print(f'Elements <= {pivot}: 0-{head - 1}')
                    print(f'Elements  > {pivot}: {tail}-{len(a) - 1}')
                    break
                
            if a[head] > pivot:
                    swap(a, head, tail)
                    tail = tail - 1
                    head = head - 1
            head = head + 1
    return a
def boundedSort(a, k):
        for j in range(1, k):
                simplePartition(a, j)
        return a
            
a = [1, 3, 6, 1, 5, 4, 1, 1, 2, 3, 3, 1, 3, 5, 2, 2, 4]
print(a)
simplePartition(a, 1)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 1 failed'

simplePartition(a, 2)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 2(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 2(B) failed'


simplePartition(a, 3)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 3(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 3(B) failed'
assert(a[8:12] == [3,3,3,3]), 'Simple Partition test 3(C) failed'

simplePartition(a, 4)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 4(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 4(B) failed'
assert(a[8:12] == [3,3,3,3]), 'Simple Partition test 4(C) failed'
assert(a[12:14]==[4,4]), 'Simple Partition test 4(D) failed'

simplePartition(a, 5)
print(a)
assert(a == [1]*5+[2]*3+[3]*4+[4]*2+[5]*2+[6]), 'Simple Parition test 5 failed'

print('Passed all tests : 10 points!')

from random import random

def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list)% 2 == 0 else 1


def matrix_multiplication(H, lst):
    # your code here
    result = [] 
    for i in range(len(H)):
       
        result.append(dot_product(H[i], lst))
    
    return result


def return_random_hash_function(m, n):
    
    H = []
    # for m rows
    for row in range(m):
        R = []
        # for n columns
        for col in range(n):
            # probability >= 1/2
            if random() >= 0.2:
                # entry is chosen as 1
                R.append(1)
            else:
                # entry is chosen as 0
                R.append(0)
    
        H.append(R)
   
    return H

A1 = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
b1 = [1,1,1,0]
c1 = matrix_multiplication(A1, b1)
print('c1=', c1)
assert c1 == [1,1,0] , 'Test 1 failed'

A2 = [ [1,1],[0,1]]
b2 = [1,0]
c2 = matrix_multiplication(A2, b2)
print('c2=', c2)
assert c2 == [1, 0], 'Test 2 failed'

A3 = [ [1,1,1,0],[0,1,1,0]]
b3 =  [1, 0,0,1]
c3 = matrix_multiplication(A3, b3)
print('c3=', c3)
assert c3 == [1, 0], 'Test 3 failed'

H = return_random_hash_function(5,4)
print('H=', H)
assert len(H) == 5, 'Test 5 failed'
assert all(len(row) == 4 for row in H), 'Test 6 failed'
assert all(elt == 0 or elt == 1 for row in H for elt in row ),  'Test 7 failed'

H2 = return_random_hash_function(6,3)
print('H2=', H2)
assert len(H2) == 6, 'Test 8 failed'
assert all(len(row) == 3 for row in H2),  'Test 9 failed'
assert all(elt == 0 or elt == 1 for row in H2 for elt in row ), 'Test 10 failed'
print('Tests passed: 10 points!')