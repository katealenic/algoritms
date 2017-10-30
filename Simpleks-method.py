
def main():
    r=0
    n=int(input("Введите количество переменных(сырья): "))
    nstr=int(input("Введите количество строк (количество ограничений): "))
    if n<=0 and nstr<0:
        print("Даные не корректно введены")
    else:
        print("Введите матрицу видов сырья построчно через enter\n")
        m={}
        for i in range(nstr):
            for j in range(n):
                m[i,j]=int(input())
        print()
        print("Введите матрицу материалов сырья(B) через enter\n")
        b={}
        for i in range(nstr):
            b[i]=int(input())
        print("Введите значения функции стоимости сырья через enter\n")
        f={}
        for i in range(n+nstr):
            if i<n:
                f[i]=int(input())
            else:
                f[i]=0;
        print()
        vari=int(input("Выберите что находите: 1-max, 2-min\n"))
        print()

        c={}
        u=0
        for i in range(nstr):
            c[u]=n+i;
            u+=1

        A={}
        t=0
        t1=-1
        for i in range(nstr):
            for j in range(n+nstr):
                if j<n:
                    A[i,j]=m[i,j]
                else:
                    if j==n+t and t1!=i:
                        A[i,j]=1
                        t+=1
                        t1=i
                    else:
                        A[i,j]=0
        M=mark(b,A,f,n,nstr,c)
        if vari==1:
            post=0
            while post==0:
                col=0
                r+=1
                for i in range(n+nstr):
                    if M[i]>=0:
                        col+=1
                if col==n+nstr:
                    post=1
                if r==4:
                    post=1
                else:
                    jj=min(M,n+nstr)-1
                    q={}
                    mem=0
                    for i in range(nstr):
                        if A[i,jj]==0 or round(A[i,jj],3)==0:
                            q[i]=0
                        else:
                            q[i]=b[i]/A[i,jj]
                        if q[i]<0:
                            mem=1
                    if mem==0:
                        ii=min(q,nstr)
                    else:
                        ii=max(q,nstr)
                    
                    b=new_b(b,A,ii,jj,n,nstr)
                    A=new_table(A,ii,jj,n,nstr)
                    c[ii]=jj
                    b[ii]=q[ii]
                    M=mark(b,A,f,n,nstr,c)
            
            num=0
            ee=0
            for i in range(nstr+n):
                print("x"+str(i+1)+"=")
                for j in range(nstr):
                    if i==c[j]:
                        num=b[j]
                        print(b[j])
                        ee-=1
                    else:
                        ee+=1
                    if ee==nstr:
                        print("0")
                        ee=0
            print("f=")
            print(M[0])
            
                      
        elif vari==2:
            post=0
            while post==0:
                col=0
                r+=1
                for i in range(n+nstr):
                    if M[i]<=0:
                        col+=1
                if col==n+nstr:
                    post=1
                if r==4:
                    post=1
                else:
                    jj=max(M,n+nstr)-1
                    q={}
                    mem=0
                    for i in range(nstr):
                        if A[i,jj]==0 or round(A[i,jj],3)==0:
                            q[i]=0
                        else:
                            q[i]=b[i]/A[i,jj]
                        if q[i]>0:
                            mem=1
                    if mem==0:
                        ii=max(q,nstr)
                    else:
                        ii=min(q,nstr)
                    
                    b=new_b(b,A,ii,jj,n,nstr)
                    A=new_table(A,ii,jj,n,nstr)
                    c[ii]=jj
                    b[ii]=q[ii]
                    M=mark(b,A,f,n,nstr,c)
            
            num=0
            ee=0
            for i in range(nstr+n):
                print("x"+str(i+1)+"=")
                for j in range(nstr):
                    if i==c[j]:
                        num=b[j]
                        print(b[j])
                        ee-=1
                    else:
                        ee+=1
                    if ee==nstr:
                        print("0")
                        ee=0
            print("f=")
            print(M[0])
            
        else:
            print("Неправильно выбрали к чему стремится функция: мин, макс. Повторите ещё!")

        
def mark(b,m,f,n,nstr,c):
    o={}
    k=0
    cij={}
    t=1
    
    for i in range(n+nstr):
        for j in range(nstr):
            if i==c[j]:
                cij[j]=f[i]
    for i in range(nstr):
        k+=b[i]*cij[i]
    o[0]=k
    k=0
    for j in range(n+nstr):
        for i in range(nstr):
            k+=m[i,j]*cij[i]
        o[t]=k-f[j]
        t+=1
        k=0
   
    return o

def max(m, n):
    max1=0
    for i in range(n):
        if m[max1]<m[i]:
            max1=i
    
    return max1
        
def min(m, n):
    min1=0
    for i in range(n):
        if m[i]<m[min1]:
            min1=i
    
    return min1

def new_table(a,ii,jj,n,nstr):
    new={}
    for i in range(nstr):
            for j in range(nstr+n):
                if i!=ii and j!=jj:
                    new[i,j]=a[i,j]-(a[i,jj]*a[ii,j]/a[ii,jj])
                if j==jj:
                    if i==ii:
                        new[i,j]=1
                    else:
                        new[i,j]=0
                if i==ii:
                    if a[ii,j]!=0:
                        new[i,j]=a[i,j]/a[ii,jj]
                    else:
                        new[i,j]=0
    
    return new

def new_b(b,a,ii,jj,n,nstr):
    new={}
    for i in range(nstr):
        if i==ii:
            new[i]=b[i]/a[ii,jj]
        else:
            new[i]=b[i]-(a[i,jj]*b[ii]/a[ii,jj])
                  
    return new
    
main()

    
    
