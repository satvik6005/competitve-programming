#graph problem
#graph structure adjacency list formed using dictionary of lists
#another dictionary to make nodes visited or non visited

def dfs(node,nod_level,level,adj_list,parent,parent_dic):
    parent_dic[node]=parent
    nod_level[node]=level
    for i in adj_list[node]:
        if i is not parent_dic[node]:
            dfs(i,nod_level,level+1,adj_list,node,parent_dic)





    
        

    

def preprocess(adj_list,nod_level,parent_dic):
    dfs(1,nod_level,0,adj_list,-1,parent_dic)
def LCA(adj_list,a,b,nod_level,parent_dic):
    if nod_level[a]>nod_level[b]:
        d=nod_level[a]-nod_level[b]
        while d!=0:
            a=parent_dic[a]
            d-=1

    else:
        d=nod_level[b]-nod_level[a]
        while d!=0:
            b=parent_dic[b]
            d-=1
    if a==b:
        return a
    else:
        while a!=b:
            a=parent_dic[a]
            b=parent_dic[b]

        return a
    


   
def m():
    
        
    test=int(input())
    while test:
        inp=list(map(int,input().split(" ")))
        n=inp[0]
        q=inp[1]
        adj_list={}
        nod_level={}
        parent_dic={}
        for i in range(1,n+1):
            adj_list[i]=[]
            nod_level[i]=0
            parent_dic[i]=0
        for i in range(1,n):
            edge=list(map(int,input().split(" ")))
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        query=[]
    
        for i in range(0,q):
            query.append(list(map(int,input().split(" "))))
        

        preprocess(adj_list,nod_level,parent_dic)

        p=[]    
        for j in query:
            c=0
            k=j[0]
            d=j[1]
            nodes=j[2::]
            for i in range(0,len(nodes)):
                for j in range(i+1,len(nodes)):
                    lca=LCA(adj_list,nodes[i],nodes[j],nod_level,parent_dic)
                    distance=nod_level[nodes[i]]+nod_level[nodes[j]]-(2*nod_level[lca])
                    if distance==d:
                        c+=1
          
            p.append(c)
        for i in p:
            print(i)
                

            
            
        test-=1

m()

        


        






    
  