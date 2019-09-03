ip = ["A", "B", "C"]

def perm(input, start):
    if(len(input)==start):
        print input
        return
    for c in range(start, len(input)):
        ip_copy = list(input)
        temp = ip_copy[start]
        ip_copy[start] = ip_copy[c]
        ip_copy[c] = temp
        perm(ip_copy, start+1)

perm(ip, 0)

## for all elements in arr
## idea is to pick say 'k' an element from the arr and it to the "PATH"
## and then pass the remaining elements (i.e, arr removing k )

""" example: 1,2,3
    Whatever you pick add it to the path --
    pick 1, path 1, arr[2,3]
        pick 2, path 12, arr[3]
            pick 3, path 123, arr[]
        pick 3 - path 13 - arr[2]
            pick 2, path 132, arr[]
    pick 2.......and so on
"""

def dfs(arr, path):
    
    if not arr:
        print path
    else:
        for i in xrange(len(arr)):
            #arr[:i]+arr[i+1:] => exclude arr[i] from first argument to dfs recursion
            #because we are adding it to the path
            dfs(arr[:i]+arr[i+1:], path+str(arr[i]))

dfs([1,2,3],"")
