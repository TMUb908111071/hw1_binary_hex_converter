number=input("請輸入0~255的整數數字 :")

if(int(number)>255or(number)<255):print("請重新輸入")
elif(int(number)>=128):a=1 or a=0     #2的7次辨識
elif(int(number)-128>=64):b=1 or b=0  #2的6次辨識
elif(int(number)-192>=32):c=1 or c=0  #2的5次辨識
elif(int(number)-224>=16):d=1 or d=0  #2的4次辨識
elif(int(number)-240>=8):e=1 or e=0   #2的3次辨識
elif(int(number)-248>=4):f=1 or f=0   #2的2次辨識
elif(int(number)-252>=2):g=1 or g=0   #2的1次辨識
elif(int(number)-254>=1):h=1 or h=0   #2的0次辨識

x=int(a)*8+int(b)*4+int(c)*2+int(d)   #前4位數字的辨識數值
y=int(e)*8+int(f)*4+int(g)*2+int(h)   #後4位數字的辨識數值

if(x,y)=15:(x,y)=F     #設定x,y的辨識數值輸出結果應為什麼
elif(x,y)=14:(x,y)=E   
elif(x,y)=13:(x,y)=D   
elif(x,y)=12:(x,y)=C   
elif(x,y)=11:(x,y)=B   
elif(x,y)=10:(x,y)=A   
elif(x,y)=9:(x,y)=9    
elif(x,y)=8:(x,y)=8    
elif(x,y)=7:(x,y)=7    
elif(x,y)=6:(x,y)=6    
elif(x,y)=5:(x,y)=5    
elif(x,y)=4:(x,y)=4    
elif(x,y)=3:(x,y)=3    
elif(x,y)=2:(x,y)=2    
elif(x,y)=1:(x,y)=1    
elif(x,y)=0:(x,y)=0    

print("二進位:abcdefgh")    #輸出二進位的結果
print(""16進位:xy")         #輸出16進位的結果