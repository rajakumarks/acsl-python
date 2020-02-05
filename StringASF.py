'''
 PROBLEM:  Given 2 strings, separated by a space, calculate the ACSL Sameness Factor (ASF).  
 Repeat the following 3 steps in order until no other deleting aligns like characters:
  ● Align the strings from left to right.  
  ● Delete the like characters in the like locations from left to right. 
  ● Proceeding from left to right, if the like location characters are not the same and deleting a 
    character at a location in one of the strings which shifts the remaining characters to the left
    causes like characters to be at that location, delete those characters and any other like characters
    at like locations.  If there is a case as in NAPE and  ANTI where it is possible to delete a character at the
    same location in both strings, then delete it in the second string.  Therefore, the A would be deleted and the NTI
    shifted to the left. 
    
    Calculate the ACSL Sameness Factor by doing the following: 
    ● Calculate the difference in the alphabetic locations from the aligned string characters in the second string to the string
     character in the first string.  B to D would add 2 to the ASF.  D to B would add -2 to the ASF.  
     ● If there are characters remaining in one of the strings, add the number of those characters to the ASF. 
        Example:    ABCDEFT ABXCGBTZFP
        ABCDEFT →    CDEF →    CDEF →    CDEF →   DEF →   DEF  → DE 
        ABXCGBTZFP → XCGBZFP → XCGBZFP → CGBZFP → GBZFP → GBFP → GBP  
        The ASF is calculated as: G to D = -3  B to E = + 3  P = + 1   (-3 + 3 + 1 = 1) 
         
'''
'''gives minimum length for given two strings 
'''
def giveMLen(z1, z2):
    if (len(z1) >= len(z2)):
        return len(z2)
    else:
        return len(z1)
'''
returns a list of charcters which are not equal at same position. 
'''
def remove(z1, z2):
    return [i for i, j in zip(z1, z2) if i != j]
'''
returns the lists, after removal of matching character at same position of two lists
'''
def checkSeq(z1, z2):
    l1 = []
    l2 = [] 
    if (len(z1) == len(z2)):
        l1 = remove(z1, z2)
        l2 = remove(z2,z1)
    elif (len(z1) > len(z2)):
        l1 = remove(z1, z2)
        l2 = remove(z2,z1)
        for i in range(len(z1) - len(z2)):
            l1.append(z1[len(z2) + i])
    else:
        l1 = remove(z1, z2)
        l2 = remove(z2,z1)
        for i in range(len(z2) - len(z1)):
            l2.append(z2[len(z1) + i])
    return l1, l2
'''
returns lists, compares and removes matching charcters at next position of lists
'''
def seq(min, z1, z2):
    for i in range(min - 1 ):
        if(z1[i] == z2[i + 1]):
            z2 = z2[:i] + z2[(i + 1):]
            z1, z2 = checkSeq(z1,z2)
            break
        elif (z1[i + 1] == z2[i]):
            z1 = z1[:i] + z1[(i + 1):]
            z1, z2 = checkSeq(z1,z2)
            break
    return z1, z2
def letter_to_int(letter):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alphabet.index(letter) + 1
'''
comparing alphabets and returns number sequence as per the problem
'''
def asf(str1, str2):
    sum = 0
    if (len(str1) > len(str2)):
        for x in range(len(str2)):
            sum += (letter_to_int(str1[x]) - letter_to_int(str2[x]))
        #print(len(str2), len(str1))
        sum += len(str1) - len(str2)
    elif (len(str2) > len(str1)):
        for x in range(len(str1)):
            sum += (letter_to_int(str1[x]) - letter_to_int(str2[x]))
        #print(len(str2), len(str1))
        sum += len(str2) - len(str1)
    else:
        for x in range(len(str2)):
            sum += (letter_to_int(str1[x]) - letter_to_int(str2[x]))
        #print(len(str2), len(str1))
    return sum
'''input = ("BLAMEABLENESSES BLAMELESSNESSES",\
        "MEZZAMINES RAZZMATAZZ",\
        "ABBREVIATIONS ABBREVIATORS",\
        "ABCDEFGHIJKLMNO ABKCLDZZHQJWWLX",
        "ABCDEFGHIJKL ABXEWFRRH"  )'''
input = ("MYARTLOLLIPOPS MYLARBALLOONS",\
         "MASSACHUSETTSBAYCOLONY MINUTEMANNATIONALHISTORICALPARK",\
        "LOWERMACTOWNSHIPPA CRANBERRYTOWNSHIPPA",\
        "AMERICANCOMPUTERSCIENCELEAGUE NATIONALACADEMICGAMESLEAGUE",\
        "ABCDEFGHIJK ABDCEFGKILKJMN")
for L in input:
    s1, s2 = L.split(' ')
    #print('original strings' , s1, s2)
    l3, l4 = checkSeq(s1,s2)
    #print('after seq removal', l3, l4, giveMLen(l3, l4))
    for i in range(giveMLen(l3, l4) - 1 ):
        l3, l4 = seq(giveMLen(l3, l4), l3, l4)
        #print('After removal', l3, l4)
    print(s1, s2, asf(l3,l4))
