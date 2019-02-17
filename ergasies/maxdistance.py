def maxDistance(a,num):
    
  maxSum=0
  maxtemp=0

  for i in range(len(a)):
  
        maxtemp=maxSum+a[i]
        if (maxtemp<num):
          maxSum=maxtemp
          maxtemp=0
        elif (maxtemp>num):
            maxtemp=0
            continue
        
        
  return maxSum
        
     

a=[]
size=int(input("Enter list length: "))
print("Enter distances: ")
for i in range(size): 
    data=int(input())
    a.append(data)
num=int(input("Enter number: "))
a.sort(reverse=True)
maxsu=maxDistance(a,num)
print(maxsu)


