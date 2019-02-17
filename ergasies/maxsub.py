def maxSequence(a,size): 
      
    max_s = 0
    max_e = 0
    
      
    for i in range(0, size): 
        max_e = max_e + a[i] 
        if max_e < 0: 
            max_e = 0
          
        elif (max_s < max_e): 
            max_s = max_e
            
              
    return max_s


a=[]
size =int(input("Enter list length:"))
print("Enter numbers:")
for i in range(size):
    data=int(input())
    a.append(data)

maxs=maxSequence(a,size)
print(maxs)


