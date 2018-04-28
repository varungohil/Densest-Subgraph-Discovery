import time

file = open("edges.txt","r")
edges = []
deg={}
dic={}
edges=file.readlines()
for i in edges:
    edge=map(int,i.split())
    if edge[0] not in dic.keys():
        dic[edge[0]]=[]
        deg[edge[0]]=0
    dic[edge[0]].append(edge[1])
    deg[edge[0]]+=1

    if edge[1] not in dic.keys():
        dic[edge[1]]=[]
        deg[edge[1]]=0
    dic[edge[1]].append(edge[0])
    deg[edge[1]]+=1
        
file.close()    

''' 
# in adjacency list at first place i'am storing degree of that vertex
dic={}
dic[0]=[1, 2, 3, 4]
dic[1] = [0, 2, 3, 4]
dic[2] = [0, 1, 3, 4]
dic[3] = [0, 1, 2, 4]
dic[4] = [0, 1, 2, 3, 5, 7]
dic[5] = [4, 6]
dic[6] = [5, 7]
dic[7] = [6, 4]
#ad_lis=[[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3, 5, 7], [4, 6], [5, 7], [6, 4]]
deg = {0:4,1:4,2:4,3:4,4:6,5:2,6:2,7:2}
n=8'''

def maxdensity(dic): #density of subgraph
    a=0
    if(len(dic)==0):
        return a
    for i in dic.keys():
        a+=len(dic[i])
    a=a/(2.0*len(dic))    
    return a

# counter is minimum degree in subgraph
def f_pop(counter): #
    tobedel=[]
    for i in deg.keys(): 
        if(deg[i]==counter):
            tobedel.append(i)
    '''print tobedel'''
    #print dic
    for k in tobedel:
        for j in dic[k]:
            (dic[j]).remove(k)
            deg[j]=deg[j]-1
             
        del dic[k]
        del deg[k]
            
#main 
start_time = time.clock()          
maxdens=0
subgraph=[]
while(len(deg)>0):
    mindeg=float('inf')
    for i in deg.keys():
        mindeg= min(deg[i],mindeg)
    '''print mindeg'''
    f_pop(mindeg)
    
    if (maxdensity(dic)>maxdens):
        maxdens=maxdensity(dic)
        subgraph=dic.keys()
        '''print "ans",maxdens,subgraph'''
    '''print dic'''
print time.clock() - start_time
print subgraph
print maxdens      


