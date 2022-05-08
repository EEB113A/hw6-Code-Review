from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    length_in=len(in_cabin)#設定輸入長度
    length_out=len(out_cabin)#設定輸出長度
    st=Stack(length_in)#初始化堆疊
    i=0#初始化輸入index
    j=0#初始化輸出index
    count=0#初始化計數值
    word=''#初始化回傳字串
    q=0#初始化檢驗值
    for z in range(length_in):#重複迴圈輸入長度的次數
        if count==length_out:#如果計數值與輸出長度一致
            break #跳出迴圈
        while in_cabin[i]!=out_cabin[j]:#如果輸入串的值不等於輸出串的值
            st.push(in_cabin[i])#push進堆疊
            word=word+'push, '#增加'push'進回傳的字串
            i=i+1#輸入index+1
        if in_cabin[i]==out_cabin[j]:#如果輸入串的值等於輸出串的值
            st.push(in_cabin[i])#push進堆疊
            word=word+'push, '#增加'push'進回傳的字串
            i=i+1#輸入index+1
            st.pop()#pop出堆疊
            word=word+'pop, '#增加'pop'進回傳的字串
            count=count+1#計數值+1
            j=j+1#輸出index+1
        if count==length_out:#如果計數值與輸出長度一致 
            break #跳出迴圈
        for x in range(i):#重複迴圈i次
            for k in range(i):  #############i=3
                if count==length_out:#如果計數值與輸出長度一致 
                    break #跳出迴圈
                if out_cabin[j]==in_cabin[k]:#如果輸入串的值等於輸出串的值
                    st.pop()#pop出堆疊
                    j=j+1#輸出index+1
                    word=word+'pop, '#增加'pop'進回傳的字串
                    count=count+1#計數值+1
                    q=q+1#檢驗值+1
                    if q>1:#如果檢驗值大於1
                        return []#回傳空陣列
            q=0 #檢驗值歸零     
    word=word[:-1]#清除最後的逗號
    word=word[:-1]#清除最後的逗號
    return [word]#回傳字串

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7] , out_cabin =  [2,4,6,5,3,7,1] )
    print(step)

#留言板