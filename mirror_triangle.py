for row in range(1,6):
    print(" "*(5-row),end="")
    for col in range(1,row+1):
        print(" %",end="")
    print( )
for row in range(5,0,-1):
    print(" "*(5-row),end="")
    for col in range(1,row+1):
        print(" %",end="")
    print( ) 