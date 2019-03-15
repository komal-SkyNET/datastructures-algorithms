ip = ["A", "B", "C", "D"]

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
