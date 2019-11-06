from collections import deque
outvar = 0

class point:

    def __init__(self):
        global outvar
        self.id = str(outvar)
        outvar = outvar+1
        print("made point num : "+str(self.id))

class grafh:
    v=list()
    E=list()




def bfs(g,s):
    Q=[]
    pi={}
    d={}
    color={}
    
    for i in g.v:
        pi[i.id]=None
        d[i.id]=None
        color[i.id]='WHITE'
    
    Q = deque([s])
    d[s.id]=0
    color[s.id]="GRAY"

    while Q:
        u=Q.popleft()
        for j in E[u.id]:
            if color[j.id]=="WHITE":
                d[j.id]=d[u.id]+1
                pi[j.id]=u.id
                color[j.id]="GRAY"
                Q.append(j)
        color[u.id]="BLACK"
    return True
