number = int(input("請輸入0~255的整數數字: "))

if int(number) > 255 or int(number) < 0:                               #如果沒有輸入正確的數字範圍告訴使用者重新輸入
    print("請重新輸入")
else:    
    a=(number//128)                                                    #2的7次辨識
    b=((number - (128*a))//64)                                         #2的6次辨識
    c=((number - (128*a)-(64*b))//32)                                  #2的5次辨識
    d=((number - (128*a)-(64*b)-(32*c))//16)                           #2的4次辨識
    e=((number - (128*a)-(64*b)-(32*c)-(16*d))//8)                     #2的3次辨識
    f=((number - (128*a)-(64*b)-(32*c)-(16*d)-(8*e))//4)               #2的2次辨識
    g=((number - (128*a)-(64*b)-(32*c)-(16*d)-(8*e)-(4*f))//2)         #2的1次辨識
    h=((number - (128*a)-(64*b)-(32*c)-(16*d)-(8*e)-(4*f)-(2*g))//1)   #2的0次辨識

    print("二進位: {}{}{}{}{}{}{}{}".format(a, b, c, d, e, f, g, h))   #輸出2進位的結果

    
    if ((number) // 16)< 10:             #整數數字除以16的商數為此區間16進位的第1位數
        x = (int(number) // 16)
    elif ((number) // 16)==10: x=("A")   #不使用其他內建程式碼，設定得到的數字落於10~14之間的16進位之結果為A~E，其餘結果(應為15)輸出F
    elif ((number) // 16)==11: x=("B")
    elif ((number) // 16)==12: x=("C")
    elif ((number) // 16)==12: x=("D")
    elif ((number) // 16)==14: x=("E")
    else: x=("F") 
    if ((number) % 16 )< 10:             #整數數字除以16的餘數為此區間16進位的第2位數
        y = (int(number) % 16)
    elif ((number) % 16)==10: y=("A")    #不使用其他內建程式碼，設定得到的數字落於10~14之間的16進位之結果為A~E，其餘結果(應為15)輸出F
    elif ((number) % 16)==11: y=("B")
    elif ((number) % 16)==12: y=("C")
    elif ((number) % 16)==13: y=("D")
    elif ((number) % 16)==14: y=("E")
    else: y=("F") 

    print("16進位: {}{} ".format(x,y))   #輸出16進位的結果
