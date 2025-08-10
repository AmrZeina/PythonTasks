line = input().split()  # read first line
k = int(line[0])  #no of lists
m = int(line[1])  #modulo

if not (1 <= k <= 7): exit("Invalid K")
if not (1 <= m <= 1000): exit("Invalid M")



lists = []  # to store the lists

for i in range(k):
    parts = input().split()  
    n = int(parts[0])  # no of elements in each list
    nums = []  
    for j in range(1, n + 1):
        nums.append(int(parts[j]))  # add each number to its list
    lists.append(nums)  

for lst in lists:
    if not (1 <= len(lst) <= 7): exit("Invalid Ni")
    for num in lst:
        if not (1 <= abs(num) <= 10**9): exit("Invalid element")


max_s = 0  # best result

def search(i, total):  
    global max_s
    if i == k:  # if we picked one from each list
        s = total % m  
        if s > max_s:  # if better
            max_s = s
        return
    for num in lists[i]:  # try each number in current list
        search(i + 1, total + num * num)  # go to next list

search(0, 0)  # start with first list
print(max_s)  
