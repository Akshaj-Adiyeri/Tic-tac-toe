a1,a2,a3,=" "," "," "
b1,b2,b3=" "," "," "
c1,c2,c3=" "," "," "
print("    1 ","   2 ","   3")
print("a ","  "," |  ","  ","| ","  ")
print("   ------------------")
print("b  ","  ","|  ","  ","| ","  ")
print("   ------------------")
print("c  ","  ","|  ","  ","|","  ")
while True:
    pos=input("enter position: ")
    opt=input("X or 0?: ")
    globals()[pos]=opt
    print()
    print("    1 ","    2 ","  3")
    print("a   ",a1, " |  ",a2," | ",a3)
    print("   ------------------")
    print("b   ",b1, " |  ",b2," | ",b3)
    print("   ------------------")
    print("c   ",c1, " |  ",c2," |",c3)
    print()
    if a1==a2==a3!=" ":
        print("player",a1,"wins!")
        break
    elif b1==b2==b3!=" ":
        print("player",b1,"wins!")
        break
    elif c1==c2==c3!=" ":
        print("player",c1,"wins!")
        break
    elif a1==b1==c1!=" ":
        print("player",a1,"wins!")
        break
    elif a2==b2==c2!=" ":
        print("player",a2,"wins!")
        break
    elif a3==b3==c3!=" ":
        print("player",a2,"wins!")
        break
    elif a1==b2==c3!=" ":
        print("player",a1,"wins!")
        break
    elif a3==b2==c1!=" ":
        print("player",a3,"wins!")
        break
    
