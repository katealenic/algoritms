
def improveLabels(val):

    for u in S:
        lu[u] -= val
    for v in V:
        if v in T:
            lv[v] += val
        else:
            minSlack[v][0] -= val

def improveMatching(v):

    u = T[v]
    if u in Mu:
        improveMatching(Mu[u])
    Mu[u] = v
    Mv[v] = u

def slack(u,v): return lu[u]+lv[v]-w[u][v]

def augment():

    while True:

        ((val, u), v) = min([(minSlack[v], v) for v in V if v not in T])
        assert u in S
        if val>0:        
            improveLabels(val)

        assert slack(u,v)==0

        T[v] = u                            
        if v in Mv:
            u1 = Mv[v]                       
            assert not u1 in S
            S[u1] = True                    
            for v in V:                     
                if not v in T and minSlack[v][0] > slack(u1,v):
                    minSlack[v] = [slack(u1,v), u1]
        else:
            improveMatching(v)              
            return

def maxWeightMatching(weights):

    global U,V,S,T,Mu,Mv,lu,lv, minSlack, w
    w  = weights
    n  = len(w)
    U  = V = range(n)
    lu = [ max([w[u][v] for v in V]) for u in U]  
    lv = [ 0 for v in V]
    Mu = {}                                     
    Mv = {}
   
    while len(Mu)<n:
        free = [u for u in V if u not in Mu]      
        u0 = free[0]
        S = {u0: True}                            
        T = {}
        minSlack = [[slack(u0,v), u0] for v in V]
        augment()

    
    val = sum(lu)+sum(lv)
    print("Целевая функция равна:")
    print(val)
    'return (Mu, Mv, val)'

n = 4
i=0
w = [[0 for v in range(n)] for u in range(n)]
for u in range(n):
    for v in range(n):
        w[u][v] = int(input())
        

maxWeightMatching(w)
