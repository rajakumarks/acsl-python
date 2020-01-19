#TESTING acsl progrqm in python
'''Given a positive integer (call it N) and position in that integer (call it P) transform N. To transform N, find the Pth
digit of N from the right. Replace each of the digits to the left of the Pth digit by the sum of the that digit and the Pth
digit. if the sum is greater than 9, use just the units digits. Replace each of the digits to the right of the Pth digit by
the abosule value of the difference between it & the Pth digit. Do not change the Pth digit.
Ex.1 : N=102439, P=3 Ans is: (1+4)(0+4)(2+4)4(|3-4)(|9-4|) => 546415
Ex. 2: N=4329 , P=1 Ans is: (4+9)((3+9)(2+9)9 => 3219
'''
def addSeq(n, p):
    i = 0 
    for num in n[::-1]:
        sum = int(num) + p
        if(sum > 9):
            finalSq.insert(i, sum % 10)
        else:
            finalSq.insert(i, sum)
        i +=1
def subSeq(n, p):
    i = 0 
    for num in n[::-1]:
        sum = abs(int(num) - p)
        finalSq.append(sum)
        
input = "9876543210 5"
N,P = input.split(" ")
print("N: "+N +" P: "+P)
oriSq = list(N)
revSq = list(reversed(N))
print(revSq)
intP = int(revSq[int(P)-1])
print (intP)
addList = revSq[int(P) : None]
subList = revSq[:int(P)-1]
print(addList, subList)
finalSq = []
addSeq(addList, intP)
finalSq.append(intP)
subSeq(subList,intP)
print(''.join(str(x) for x in finalSq))
