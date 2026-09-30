j=1
while j<=3:
    
    
    i=1
    while i<=3:
        print("*",end="")
        
        i+=1
    
    print()    
    
    j+=1
    
    
j=1
while j<=5:
    i=1
    while i<=5:
        if j==1 or j==5 or i==1 or i==5:
            print("*",end="")
        else:
            print(" ", end="")
        i+=1
    
    print()
    j+=1