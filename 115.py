m=50
def t(n,vals={}):
    if n not in vals:
        vals[n]=sum([t(k) for d in range(3,n+1) for k in range(3,n-d)])+n-2
        vals[n]=sum([t(k) for d in range(m,n+1) for k in range(m,n-d)])+n-(m-1)
    return vals[n]
def p(n):
    return sum([t(p) for p in range(2,n+1)])+1

i=51
while(p(i)<10**6):
    i+=1
print(i) 