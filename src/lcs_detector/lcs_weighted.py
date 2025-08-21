import tokenizer

def LCS(codea,codeb):
    A = tokenizer.Tokenizar(codea)
    B = tokenizer.Tokenizar(codeb)
    m = len(A)
    n = len(B)
    L = [list(range(m+1)) for _ in range(n+1)]

    for i in range(1,m,1):
        
        for j in range(1,n,1):
    
            if (A[i] == B[i]):
                
                L[i][j] = L [i-1][j-1]+1
                
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
                
                
    


