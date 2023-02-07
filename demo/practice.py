def addition(list1,list2):
  
  list1.extend(list2)
  list1.sort()
  print(list1)
  
list1 = ["A", "E", "C","D","P","Q"]
list2 = ["G", "F", "B"]
list1 = [1,2,3,4,5,6]

B=3
if len(list1)%B==0:
    res=[list1[i:i+B] for i in range(0,len(list1)-B+1,B)]
else:
    res=[list1[i:i+B] for i in range(0,len(list1)-B+1,B)]
    res.append(list1[(len(list1)-len(list1)%B):len(list1)])
print(res)
