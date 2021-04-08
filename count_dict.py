word = input("Please enter a string\n")
count = {}
for x in word:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1   
count_sorted = sorted(count, key = count.get, reverse = True)
for r in count_sorted:
    print(r,"=",count[r])      
