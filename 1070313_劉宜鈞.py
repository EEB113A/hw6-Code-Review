from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    outputlist=[] # 先把最後的回傳值設為空字串none
    size=len(in_cabin) # 計算Stack內的長度大小
    sta=Stack(size) # 代入函式
    i=0
    #下面迴圈是用來，從第一個輸出點一個一個比對
    for j in range(len(in_cabin)):
        sta.push(in_cabin[j])
        outputlist.append('push')
        if in_cabin[j]==out_cabin[i]: # 假設要加進來的剛好是要pop的，則一個個加入進來
            while sta.top>-1 and sta.data[sta.top] == out_cabin[i]: 
                # 在做一次的pop後，繼續比對下一個要輸出的點，如果還是一樣，則繼續做pop
                sta.pop()
                outputlist.append('pop') # 做pop
                i=i+1 # 跳下一個

    if sta.top!=-1: # 用此判斷錯誤，假設輸出不成立的話，sta.top不會到-1
        outputlist=[] # 設none
    
    return outputlist # return，回傳outputlist值


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3, 4, 5, 6, 7], out_cabin = [2, 4, 6, 5, 3, 7, 1])
    print(step)

#留言板