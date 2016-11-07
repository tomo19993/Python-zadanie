import os
print (os.getcwd())
os.chdir("C:/Users/lenovo/Desktop/python")
with open("sc.xyz",'w') as sc:
    dim=10
    num_of_atoms=dim**3
    for x in range(0,dim):
        for y in range(0,dim):
            for z in range(0,dim):
                sc.write("%d %d %d\n"%(x,y,z))

l_sc=[]
#lista.append((x,y,z))
with open("sc.xyz",'r') as fp:
    dim=10
    for line in fp: # read rest of lines
        l_sc.append([int(dim) for dim in line.split()])
l_surf=[]
mid=int(len(l_sc)/2)
start=l_sc[mid]
i = 0
for x in range(0,len(l_sc)):
            result = l_sc[x]*start[0] 
            if(result[i] <= 0):
              l_surf.append(l_sc[x])
              i+=1
with open("l_surf.xyz",'w') as fpointer:
    for item in l_surf:
         fpointer.write("%s\n" % item)