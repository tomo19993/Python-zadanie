import random
num_list=[]
i=0
s=0
while i<1000:
    num_list.append(random.randint(0,1000))
    i+=1
for i in range(0,len(num_list)):
    s +=num_list[i]

print(s)
