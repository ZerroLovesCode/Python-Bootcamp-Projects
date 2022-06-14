from ntpath import join
import random
from tokenize import Special
AlphaList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NumList = ['0','1', '2', '3', '4', '5', '6', '7', '8','9']
Splchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '<', '>', '?', '/', '.', ',', '_','-','+','=','`','~']
numA = int(input('How many letters in the password? '))
numN = int(input('How many numbers in the password? '))
numS = int(input('How many special characters in the password? '))
pw = []

for i in range(numA):
    pw.append(random.choice(AlphaList))
for i in range(numN):
    pw.append(random.choice(NumList))
for i in range(numS):
    pw.append(random.choice(Splchars))    

random.shuffle(pw)
passW = "".join(pw)
print(f'Your Password is: {passW}')
