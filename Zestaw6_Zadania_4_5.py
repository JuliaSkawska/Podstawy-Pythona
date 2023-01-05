import re
def UserEntry():
    user=input("Enter your string: ")
    return user

#zadanie 4 zestaw 6
def BigLetter(x):
    result=[]
    res=re.findall(r'([a-zA-Z0-9 ]{1,}\.)',x)
    for a in res:
        a=a.lower()
        if a[0]==" ":
            a=a[1].upper()+a[2:]
        else:
            a=a.capitalize()
        result.append(a)
    result=' '.join(result)
    return result
print(BigLetter(UserEntry()))

#zadanie 5 zestaw 6
def ChangeDate(x):
    res=re.sub(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',r'\3-\2-\1',x)
    return res
print(ChangeDate(UserEntry()))