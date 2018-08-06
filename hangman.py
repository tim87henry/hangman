import random
import os

""" The findMatch proc is used to find if the character,
entered by the user, is present in the actual answer. 
If present, it returns the index/indices of the matched character.
Else, it returns None.
"""
def findMatch(st, ch):
    return [i for i, letter in enumerate(st) if letter == ch]

""" The getWord proc is used to fetch a random 
name from the file 'names.txt'
"""
def getWord():
    f=open("names.txt","r+")
    lines=f.readlines()
    return lines[random.randint(0,len(lines))]


""" The findChances proc is used to calculate the number of 
chances the user gets, for the chosen word.
"""
def findChances(a):
    unique_a=[]
    for alph in a:
        if alph not in unique_a:
            unique_a.append(alph)
    return len(unique_a)+4


# Main program starts here

a=getWord()
a=a.replace('\n','')
ln=len(a)
num_chance=findChances(a)
win=0
b=[]
for k in range(ln):
    if a[k]==" ":
        b.append(' ')
    else:
        b.append('_')
for i in range(1,num_chance+1):
    print("You have "+str(num_chance)+" chances to guess the word\n")
    if b.count('_')>0:
        print(*b)
        print("\nChance number "+str(i))
        ch=input("Enter the alphabet  :  ")
        mat=findMatch(a,ch)
        if str(mat)!=None:
            for n in mat:
                b[n]=b[n].replace('_',ch)
        os.system("cls")
    else:
        
        win=1
        break
if not win:
    print("Sorry, you LOST!!!!!!!!!")
    print("The word was "+str(a))
else:
    print(*b)
    print("You've WON !!!!!!!!!!!!!!!!")
