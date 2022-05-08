from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    sta = Stack(len(in_cabin))  # 設定sta長度
    size = len(in_cabin)
    steps = []  # 設定空的list名字
    x = 0;
    y = 0  # x=out_cabin的位子，y=in_cabin
    while True:
        z = 0  # 決定if條件
        if (in_cabin[y] == out_cabin[x]):  # 如果in_cabin的第一個數字跟out_cabin的第一個數字一樣，sta先push再pop
            sta.push(in_cabin[y])
            steps.append('push')
            sta.pop()
            steps.append('pop')
            if (y < size - 1):  # 如果y沒超出size-1    y就+1
                y += 1
            if (x < size - 1):  # 如果x沒超出size-1    x就+1
                x += 1
            else:  # 如果x讀完了就跳出迴圈
                break
            z += 1
        if (sta.data[sta.top] == out_cabin[x]):  # 如果堆疊sta的最上層跟out_cabin的第一個數字一樣，sta就pop
            steps.append('pop')
            sta.pop()
            if (x < size - 1):  # 如果x尚未超出size-1 x就+1
                x += 1
            else:  # 如果x讀完了就跳出迴圈
                break
            z += 1
        if (z == 0):  # 如果上述兩個條件都不是z依然等於0， 再跑一次
            steps.append('push')
            sta.push(in_cabin[y])
            if (y < size - 1):  # 如果y尚未超出size-1   y就+1
                y += 1
            if sta.isFull():  # 如果sta堆疊滿了即無解
                steps = []
                break
    return (steps)


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板