# hw1_binary_hex_converter
## 程式碼報告
![image](https://github.com/TMUb908111071/hw1_binary_hex_converter/assets/161851654/e43eb03b-fc18-46e9-b72b-724e835635d4)

## 執行結果
![image](https://github.com/TMUb908111071/hw1_binary_hex_converter/assets/161851654/644853d6-1af1-4eaa-bf0a-856feeac04a4)
***
## 程式碼解釋
### 首先讓使用者輸入所想選擇的0~255中的整數數字
```
number = int(input("請輸入0~255的整數數字: "))
```

### 如果輸入的範圍不在0~255中，輸出「請重新輸入」，告訴使用者重新輸入
```
if int(number) > 255 or int(number) < 0:
    print("請重新輸入")
```
