from numpy import size
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    sta = Stack(len(in_cabin)) #設定sta的長度跟in_cabin一樣，而根據題目描述in_cabin長度又等於out_cabin
    size = len(in_cabin)
    steps = [] #設定一個空的list名字叫做steps，裡面會放進出站的步驟
    x=0;y=0 #變數x拿來讀out_cabin的位子，變數y拿來讀in_cabin的位子
    while True: #進入迴圈 
        z=0 #變數z之後會拿來決定是否跑進最後一個if條件
        if(in_cabin[y] == out_cabin[x]): #如果in_cabin的第一個數字跟out_cabin的第一個數字一樣，sta先push再pop
            sta.push(in_cabin[y])
            steps.append('push')
            sta.pop()
            steps.append('pop')
            if(y<size-1): #如果y尚未超出size-1(未讀取完畢) y就+1 
                y+=1
            if(x<size-1): #如果x尚未超出size-1 x就+1
                x+=1
            else: #如果x讀完了就跳出迴圈
                break
            z+=1
        if(sta.data[sta.top] == out_cabin[x]): #如果堆疊sta的最上層跟out_cabin的第一個數字一樣，sta就pop
            steps.append('pop')
            sta.pop()
            if(x<size-1): #如果x尚未超出size-1 x就+1
                x+=1
            else: #如果x讀完了就跳出迴圈
                break
            z+=1
        if(z==0): #如果上述兩個條件都不是z依然等於0，就先push(in_cabin)然後看情況再跑一次
            steps.append('push')
            sta.push(in_cabin[y])
            if(y<size-1): #如果y尚未超出size-1(未讀取完畢) y就+1
                y+=1
            if sta.isFull(): #如果sta堆疊滿了即無解，將steps設為空list，然後break迴圈
                steps = []
                break
    return(steps)


if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3,4,5], out_cabin = [4,5,1,2,3])
    print(step)

#留言板