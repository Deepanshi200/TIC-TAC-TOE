def fun(inp):
    if inp < 0 or inp > 9:
        return 100
    if inp > 0 and inp < 4:
        return 0
    elif inp >= 4 and inp < 7:
        return 1
    elif inp >= 7 and inp < 10:
        return 2

def fun1(inp):
    if inp < 0 or inp > 9:
        return 100
    if inp > 0 and inp < 4:
        return inp - 1
    elif inp >= 4 and inp < 7:
        return inp - 4
    elif inp >= 7 and inp < 10:
        return inp - 7


l = [['-','-','-'],['-','-','-'],['-','-','-']]
t = [[0,0,0],[0,0,0],[0,0,0]]
ttrans = [[0,0,0],[0,0,0],[0,0,0]]
doo1=0
doo2=0
doo3=0
doo4=0
for k in l:
    print(k)

print("Enter the square number you want to place your mark on ")
print("For example for first square insert '1'")

c=0
satis =0 
satis2 = 0
while(c!=9):
    while(satis!=1):
        satis = 0
        inp = int(input("PLAYER 1:"))
        
        i1 = fun(inp)
        i2 = fun1(inp)

        if(i1<=2 and i2<=2 and l[i1][i2]=='-'):

            t[i1][i2]= 6
            ttrans[i2][i1]=6
            l[i1][i2] = "X"
            if(i1==i2):
                doo1 = doo1+1
            if(i1+i2==2):
                doo2 = doo2+1
            satis =1
            c=c+1
        else:
            print("wrong input. Try again")
        for k in l:
            print(k)
        for tt in t:
            #print(sum(tt))
            if(sum(tt)==18 or doo1==3 or doo2==3):
                print("Player 1 wins")
                c=9
                break
        for rr in ttrans:
            #print(sum(rr))
            if(sum(rr)==18):
                print("Player 1 wins")
                c=9
                break
    while(satis2!=1 and c!=9):
        satis2 = 0
        inp2 = int(input("PLAYER 2:"))


        i3 = fun(inp2)
        i4 = fun1(inp2)
        if(i3<=2 and i4<=2 and l[i3][i4]=='-'):

            t[i3][i4]= -6
            ttrans[i4][i3]=-6
            if(i1==i2):
                doo3 = doo3+1
            if(i1+i2==2):
                doo4 = doo4+1
            l[i3][i4] = "O"
            satis2 =1
            c=c+1
            satis2 = 1
        else:
            print("wrong input. Try again")
        for k in l:
            print(k)
        for tt in t:
            #print(sum(tt))
            if(sum(tt)==-18 or doo3==3 or doo4==4):
                print("player 2 wins")
                c=9
                break
        for rr in ttrans:
            if(sum(rr)==-18):
                print("player 2 wins")
                c=9
                break


        #print(c)
    satis = 0
    satis2 = 0
