"""
This is a function called maxSequence that takes a list as input and returns the sublist (consecutive items in the list) that has the maximum sum.
Example: maxSequence ([- 2, 1, -3, 4, -1, 2, 1, -5, 4]) returns 6: [4, -1, 2, 1]
"""
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


