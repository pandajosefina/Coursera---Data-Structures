# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation


    def fillDepth(parent, i , depth): 
        if depth[i] != 0: 
            return 
        if parent[i] == -1: 
            depth[i] = 1
            return 
        if depth[parent[i]] == 0: 
            fillDepth(parent, parent[i] , depth) 
        depth[i] = depth[parent[i]] + 1
    
    depth = [0 for i in range(n)] 
     
    for i in range(n): 
        fillDepth(parents, i, depth)     
        
    ht = depth[0]   
        
    for i in range(1,n): 
        ht = max(ht, depth[i]) 
     
    return ht
       


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
