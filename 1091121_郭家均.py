from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    push = 'push' #push字串
    pop = 'pop' #pop字串
    sta = Stack( len( in_cabin ) + 1 ) #建立Stack
    re = [] #回傳值
    out_index = 0 #out的索引值


    for i in in_cabin :

        re.append( push ) #push進來

        if out_cabin[out_index] != i : #如果不同
            sta.push( i ) #丟到stack裡
            continue #跑下一個

        out_index = out_index + 1 #out索引值+1
        re.append( pop ) #pop出去

        while True :

            if sta.isEmpty() : #Stack空了
                break #跳出迴圈

            x = sta.pop() 

            if out_cabin[out_index] == x : #如果相同
                re.append( pop ) #pop出去
                out_index = out_index + 1 #out索引值+1

            else : #如果不同
                sta.push( x ) #丟到stack裡
                break #跳出迴圈



    while out_index < len( out_cabin ) :#有沒有剩

        x = sta.pop()

        if out_cabin[out_index] == x : #如果相同
            re.append( pop ) #pop出去
            out_index = out_index + 1 #out索引值+1

        else : #如果不同
            break #跳出迴圈

 
    if sta.isEmpty() : #都pop完了

        return re #回傳re
        
    return [] #還有剩的話回傳[]


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板