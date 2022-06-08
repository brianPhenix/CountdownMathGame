import math 
import itertools
import random as rnd
from Tools import *

Choose_Total = 6
Choose_Big = 1
Choose_Small = Choose_Total - Choose_Big

#Target = rnd.randint(101, 999)

# Cards: 25, 50, 75,  100
Big = [i for i in range(25, 101, 25)]  

# Cards: 1-10, 1-10
Small = [i for i in range(1, 11)] * 2  

# Operations
Math="+ - * /".split()



s = "Countdown Numbers Game"
print(s)
print("_"*(len(s)))
print("\n")

print("INPUT:")
print("Big Cards: ", Big)
print("Small Cards: ", Small)
print("\n")

Target = rnd.randint(100,1000)
#Target = 949


rnd.shuffle(Big)
Big = Big[:Choose_Big]

rnd.shuffle(Small)
Small = Small[:Choose_Small]

#Big = [25, 75]
#Small = [9,6,6,5]

Card = Big + Small





print("Cards: ", Card)
print("Target: ", Target)

print("\n\n")









class NumberGame():

           
    def __init__(self, Card, Math):
        self.Card = tuple(Card)
        self.Math = tuple(Math)
        self.Op = "op"
        self.Pair = [0,0]
        self.Result = [0]
        self.ListOfSteps = []
        self.Step = 0
        self.GoOn = 0
        
    def DoMath(self, a, b):
        dict={
            "+":a + b,        
            "-":a - b,
            "/":a / b,
            "*":a * b
             }
        return(dict.get(Game.Op))
                
    def CardOperation(self):
        result = round( Game.DoMath( *self.Pair ), 4)
        if (result - math.trunc(result))==0:
            result = math.trunc(result)
            t = tuple(( *self.Pair, Game.Op, result ))
            self.Result.append(result)
            self.ListOfSteps.append( t )
        else:
            Game.GoOn = 1
        return(result)


def DoGame(Game):
    Game.Step = 0
    nCard = 0
    for Game.Op in Game.Math:
        Game.Step = Game.Step + 1
        nCard = nCard + 1
        if Game.Step == 1:
            A = Game.Card[ 0 ]
            B = Game.Card[ nCard ]
        else:
            A = Game.Result[ Game.Step - 1 ]
            B = Game.Card[ nCard ]
        Game.Pair = A, B
        Game.GoOn=0 
        result = Game.CardOperation()
        if(Game.GoOn or result==Target):
            return()




#Game = NumberGame(Card, Math)
#DoGame(Game)

greek_D = "\u0394" 
greek_R = "\u03C1" 


CardPerm = tuple(itertools.permutations(Card))
#CardPerm = CardPerm[0:10]


L = [Math] * (Choose_Total - 1) 
MathPerm = tuple(itertools.product(*L) )



GameResult=[]

ListOutput=[]
ListOutputTarget=[]

NGameTotal = len(CardPerm) * len(MathPerm)
NGame=0
NOut=0
NTarget=0

print(NGameTotal, len(CardPerm), len(MathPerm) )

for CardSet in CardPerm:
    for MathSet in MathPerm:

        NGame = NGame + 1

        Game = NumberGame(CardSet, MathSet)
        Game.GoOn=0
        DoGame(Game)
        if(Game.GoOn): continue
        answer = Game.Result[Game.Step]

        diff = answer - Target
        if type(answer)==int and diff <1 and diff>-1:
            NOut = NOut + 1
            if diff == 0:
                GameResult.append( (answer, tuple(Game.ListOfSteps)) ) 
                target=1
                NTarget = NTarget + 1
                tag = f"TARGET   ({NTarget})"
            else:
                tag   = f"{diff}"
                target=0

            s0 = "  "
            s1 = f"{NOut}"
            s2 = f"{greek_R}"
            s3 = f"{answer}"
            s4 = f"{greek_D}"
            s5 = f"{tag}"

            ind=0
            if len(GameResult)==1: ind=1
            if len(GameResult) % 40 == 0 and NGameTotal - NGame >20: ind=1
            if ind:
                printColHeader()

            output = s0.ljust(6) + s1.rjust(4) + "\t\t" + s3.rjust(6) + "\t\t\t" + s5.rjust(6)
            ListOutput.append(output)
            if target : ListOutputTarget.append(output)
            print(output)


GameResult_T = tuple(GameResult)



print("\n\n")
print("List of Games on TARGET:")
print("\n")




if len(ListOutputTarget)>0: printColHeader()
printT(ListOutputTarget)

print("\n\n")

#printT(GameResult_T)

print("\n\n")
print("\n\n")

ls = list(GameResult_T)

#def get_second(tup):
#    return tup[1][0]

#ls.sort(key=get_second)

#printT(ls)
 
print("\n\n")
print("\n\n")

printColHeader()

ls = list(set(ls))
def getKey(tup):
    return tup[1][0][3]

ls.sort(key=getKey)
printT(ls)


        
        
        

        
        
        

    

