import random
AlphaList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NumList = ['0','1', '2', '3', '4', '5', '6', '7', '8','9']
Splchars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '<', '>', '?', '/', '.', ',', '_','-','+','=','`','~']
l = int(input('How long do you want the password to be? '))

pw = ''

for i in range(l):
    listChooser = random.randint(0,2)
    if listChooser == 0:
        pw += random.choice(AlphaList)
    elif listChooser == 1:
        pw += random.choice(NumList)
    else:
        pw += random.choice(Splchars)
print(f'Your Password is: {pw}')