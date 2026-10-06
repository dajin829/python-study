h=input("请输入你的身高")
w=input("请输入你的体重")
h=float(h)
w=float(w)

def calc_bmi(h,w):
    bmi=w/(h*h)

    return bmi
print(f"{calc_bmi(h,w):.2f}")