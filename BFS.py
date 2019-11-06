from collections import deque
from grafh_classes import grafh
outvar = 0



def bfs(g,s):
    Q=[]
    pi={}
    d={}
    color={}
    # first init the data structure for the BFS to work curractly
    for i in g.v:
        pi[i.id]=None
        d[i.id]=None
        color[i.id]='WHITE'
    #init the first stage in the queue
    Q = deque([s])
    d[s.id]=0
    color[s.id]="GRAY"
    # while there is somting in the Queue 
    while Q:
        #start by poping the first element in the queue
        u=Q.popleft()
        #for each point the connects to u do the fullowing
        for j in E[u.id]:
            #first chack if the node allrady in the procees
            if color[j.id]=="WHITE":
                d[j.id]=d[u.id]+1
                pi[j.id]=u.id
                color[j.id]="GRAY"
                Q.append(j)
        color[u.id]="BLACK"
    return True
