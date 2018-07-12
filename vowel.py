val=input()
list1=['a','e','i','o','u']
for i in list1:
    if((val<='A' and val>='Z') or (val>='a' and val<='z')):
        if(val==i):
            print("Vowel")
            break
        else:
            print("Consonant")
            break
    else:
        print("Invalid")
        break
