"""
This is a function called maxSequence that takes a list as input and returns the sublist (consecutive items in the list) that has the maximum sum.
Example: maxSequence ([- 2, 1, -3, 4, -1, 2, 1, -5, 4]) returns 6: [4, -1, 2, 1]
"""

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


