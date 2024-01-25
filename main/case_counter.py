"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""

text=input()
def case_counter(text):
    
    s=0
    low=0
    upper=0
    
    for i in range(0 ,(len(text))):
     x=text[i]
     
     if x>="a" and x<="z":
      s=1
      low=low+1
     if x>="A" and x<="Z":
      s=1
      upper=upper+1
      
    if s==0:
     print("low:"+'0'+"upper:"+'0')
    else:
     print("low:"+str(low))
     print("upper:"+str(upper))
pass

print(case_counter(text))
