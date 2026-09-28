a=input("今天有没有下雨？")
if(a=="有"):
    b=input("今天出门多久分钟？")
    b=int(b)
    if(b>=30):
        print("今天出门要带伞" )
    else:
        print("今天出门不用带伞")
else:
    c=input("今天风大不大？")
    
    if(c=="不大"):
            print("今天出门不要带伞")
    else:
            print("今天出门不用带伞 风大撑不住")

