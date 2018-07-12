val=input()
list1=['a','e','i','o','u']
for i in list1:
    if(val>='a' and val<='z'):
        if(val==i):
            m=0
            break
        else:
            m=1
            break
    else:
        m=2
        break
if(m==0):
   print("Vowel")
elif(m==1):
   print("Consonant")
else:
   print("Invalid")
        
        
