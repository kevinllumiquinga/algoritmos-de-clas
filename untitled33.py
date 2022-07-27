def palindromo(a):
    test= True
    j=0  
    for i in reversed(range(len(a))):
        if a[i] != a[j]:
            test=False
            break
        else:
            j +=1
        if j==0 or (i+1)==0:
            break
    if test==False:
        print("no palíndromo")
    elif test==True:
        print("palidromo")
    
print(palindromo(5))



