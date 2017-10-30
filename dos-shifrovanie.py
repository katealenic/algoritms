
def main():
    n=int(input("Введите 1 для зашифрования и 2 для расшифрования: "))
    if n==1:
        numb1=int(input("Введите число: "))
        new_text=""
        text=input("Введите текст: ")
        for i in text:
            new_text+=main1(numb1,i)
        print(new_text)
    elif n==2:
        numb1=int(input("Введите число: "))
        new_text=""
        text=input("Введите текст: ")
        for i in text:
            new_text+=main2(numb1,i)
        print(new_text)
    else:
        print("Не верно ввели!")

def main1(numb1,symb1):

    numb=create(numb1,10)
    
    k11=[1,7,9,4,8,3,10,6]
    k22=[8,3,6,5,10,2,9,1]
    k1=numb.copy()
    k1.remove(0)
    k1.remove(0)
    k2=numb.copy()
    k2.remove(0)
    k2.remove(0)
    i=0
    while i<8:
        k1[i]=numb[k11[i]-1]
        k2[i]=numb[k22[i]-1]
        i+=1

    symb2=create(symb1,8)
    symb=symb2.copy()

    
    
    ip=[2,6,3,1,4,8,5,7]
    i=0
    while i<8:
        symb[i]=symb2[ip[i]-1]
        i+=1

    L=symb.copy()
    y=0
    while y<4:
        r=L.pop()
        y+=1
    R=symb[4:]
    
    v1=s_matric(symb,R,L,k1,1)

    v2=s_matric(v1,v1[4:],v1[:4],k2,2)

    ip1=[4,1,3,5,7,2,8,6]
    i=0
    while i<8:
        v1[i]=str(v2[ip1[i]-1])
        i+=1
        
    string=''.join(v1)
    print(int(string,2))
    return chr(int(string,2))

def main2(numb1,symb1):
    
    numb=create(numb1,10)
    
    k11=[1,7,9,4,8,3,10,6]
    k22=[8,3,6,5,10,2,9,1]
    k1=numb.copy()
    k1.remove(0)
    k1.remove(0)
    k2=numb.copy()
    k2.remove(0)
    k2.remove(0)
    i=0
    while i<8:
        k1[i]=numb[k11[i]-1]
        k2[i]=numb[k22[i]-1]
        i+=1
    
    nn=8
    numb1=symb1
    numb2=[]
    numb2=list(bin(ord(numb1))[2:])
    
    n=0
    for i in numb2:
        n+=1
    i=0
    while i<n:
        t=numb2[i]
        numb2[i]=int(t)
        i+=1
    i=nn
    j=0
    numb=numb2.copy()
    u=0
    while u<nn-n:
        numb.append(0)
        u+=1
    if n<10:
        while i>0:
            if i>n:
                numb[nn-i]=0
            else:
                numb[nn-i]=numb2[j]
                j+=1
            i-=1
    
    symb2=numb
    symb=symb2.copy()
    
    ip=[2,6,3,1,4,8,5,7]
    i=0
    while i<8:
        symb[i]=symb2[ip[i]-1]
        i+=1

    L=symb.copy()
    y=0
    while y<4:
        r=L.pop()
        y+=1
    R=symb[4:]
    
    v1=s_matric(symb,R,L,k2,1)

    v2=s_matric(v1,v1[4:],v1[:4],k1,2)

    ip1=[4,1,3,5,7,2,8,6]
    i=0
    while i<8:
        v1[i]=str(v2[ip1[i]-1])
        i+=1
        
    string=''.join(v1)
    'print(int(string,2))'
    return chr(int(string,2))

    
def s_matric(symb,R,L,k1,mam):
    
    ep=[4,1,2,3,2,3,4,1]
    sep=symb.copy()
    i=0
    rrr=symb[4:]
    while i<8:
        sep[i]=rrr[ep[i]-1]
        i+=1
    
    xor=xor2(sep,k1,8)
    l=xor[:len(L)]
    r=xor[len(L):]
    

    sl={(0,0):1,(0,1):0,(0,2):3,(0,3):2,
        (1,0):3,(1,1):2,(1,2):1,(1,3):0,
        (2,0):0,(2,1):2,(2,2):1,(2,3):3,
        (3,0):3,(3,1):1,(3,2):3,(3,3):1}
    
    sr={(0,0):1,(0,1):1,(0,2):2,(0,3):3,
        (1,0):2,(1,1):0,(1,2):1,(1,3):3,
        (2,0):3,(2,1):0,(2,2):1,(2,3):0,
        (3,0):2,(3,1):1,(3,2):0,(3,3):3}

    i1=l[0]*pow(2,1)+l[3]*pow(2,0)
    j1=l[1]*pow(2,1)+l[2]*pow(2,0)

    i11=r[0]*pow(2,1)+r[3]*pow(2,0)
    j11=r[1]*pow(2,1)+r[2]*pow(2,0)

    sll=list(bin(sl[i1,j1])[2:])
    srr=list(bin(sr[i11,j11])[2:])

    
    
    n1=0
    for q in sll:
        n1+=1
    n2=0
    for q in srr:
        n2+=1
        
    if n1==1:
        a=sll[0]
        sll.append(0)
        sll[0]=0
        sll[1]=a
        
    if n2==1:
        a=srr[0]
        srr.append(0)
        srr[0]=0
        srr[1]=a

    if n1==0:
        sll.append(0)
        
    if n2==0:
        srr.append(0)
    
    
    sll.extend(srr)
    
    
    i=0
    while i<4:
        t=sll[i]
        sll[i]=int(t)
        i+=1
        
    s=sll.copy()
    

    p4=[2,4,3,1]
    i=0
    while i<4:
        s[i]=sll[p4[i]-1]
        i+=1
    
    ss=xor2(L,s,4)

    sss=R.copy()
    

    if mam==1:
        sss.extend(ss)
        return sss

    else:
        ss.extend(sss)
        return ss
    
    
    
def xor2(ep,k,n):
    x=ep.copy()
    i=0
    while i<n:
        if (ep[i]==1 and k[i]==0) or (ep[i]==0 and k[i]==1):
            x[i]=1
        else:
            x[i]=0
        i+=1
    
    return x

    
def create(numb1,nn):
    numb2=[]
    if nn==10:
        numb2=list(bin(numb1)[2:])
    if nn==8:
        numb2=list(bin(ord(numb1))[2:])
    n=0
    for i in numb2:
        n+=1
    i=0
    while i<n:
        t=numb2[i]
        numb2[i]=int(t)
        i+=1
    i=nn
    j=0
    numb=numb2.copy()
    u=0
    while u<nn-n:
        numb.append(0)
        u+=1
    if n<10:
        while i>0:
            if i>n:
                numb[nn-i]=0
            else:
                numb[nn-i]=numb2[j]
                j+=1
            i-=1
    print(numb)
    return numb
main()
