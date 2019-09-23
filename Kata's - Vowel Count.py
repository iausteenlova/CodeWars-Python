# >> Vowels Count



def getcount(inputStr):
    num_vowels = 0
    inputStr = inputStr.lower()
    for i in range(len(inputStr)):
        if 'a' in inputStr[i]:
            num_vowels+=1
        elif 'e' in inputStr[i]:
            num_vowels+=1
        elif 'i' in inputStr[i]:
            num_vowels+=1
        elif 'o' in inputStr[i]:
            num_vowels+=1
        elif 'u' in inputStr[i]:
            num_vowels+=1
        else:
            pass
    return num_vowels



def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")



def getCount(s):
    return sum(c in 'aeiou' for c in s)



def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels



import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))



def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


#lambda function
getCount = lambda s: sum(s.count(i) for i in 'aeiou')


