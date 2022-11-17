
s=input("roman number:")
    
def romanToInt(s):
    dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
    }
    r=0
       
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    
    for i in s :
        r+=dict[i]
            
    return r
print(s)
r=romanToInt(s) 
print(r)