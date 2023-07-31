n=int(input('Please input any number of your choice : '))
for i in range(1, n+1 ):
  
  if i % 3==0 and i % 5==0:
    print('SoloLearn')
    
  elif i % 2==0:
    continue 
    
  elif i % 3 ==0:
    print('Solo')
    
  elif i % 5==0:
    print('Learn')
    
  else:
    print (i)