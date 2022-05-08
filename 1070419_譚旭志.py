import re
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list

    stack_step = []              #定義一個空list紀錄步驟回傳值
    stack_len = len(in_cabin)    #計算in_cabin長度
    st = Stack(stack_len)        #定義st套用class Stack
    
    for i in in_cabin:                            #從in_cabin裡抓值出來
        st.push(i)                                #push進st裡
        stack_step.append('push')                 #stack_step新增'push'的動作
        for j in range(st.top, -1, -1):           #從st裡往回檢查資料
            if st.data[j] == out_cabin[0]:        #判斷是否和out_cabin的第一位資料相同
                st.pop()                          #pop進st裡
                stack_step.append('pop')          #stack_step新增'pop'的動作
                out_cabin.remove(out_cabin[0])    #移除out_cabin的第一位資料
            else:
                break                             #不一樣就跳出迴圈
    
    if st.top != -1:       #如果st裡還有值(意謂著車站裡面還有數字)
        stack_step = []    #步驟回傳值為空list
    
    return stack_step      #回傳步驟回傳值

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板