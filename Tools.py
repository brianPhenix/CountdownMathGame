

def printT(tp, start=0, stop=0):
    count = 0
    for s in tp:
        count = count + 1
        if(count < start): continue
        print( s )
        if(count == stop): break


def printColHeader():
    greek_R = "\u0394" 
    greek_D = "\u03C1" 
    colheader = "N".center(20) + greek_D.center(19) + greek_R.center(25)
    print("\n")
    print("_"*60)
    print("\n")
    print(colheader)
    print("\n")
