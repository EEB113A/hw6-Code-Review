from re import L
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    len1 = len(in_cabin)                                             #計算車廂的長度
    ans = []                                                         #最後return的list     
    st = Stack(len1)                                                 #建立車站
    k = 0                                                            #之後依照順序需要的數字
    for i in out_cabin :
        while st.data[st.top] != i and i not in st.data :            #當top所指的數字並不等於目前所要pop的數字且所要pop的數字並不在車站內
            st.push(in_cabin[k])                                     #push in_cabin的車廂
            ans.append("push")                                       #答案新增push這個步驟
            k += 1                                                   #往下一個車廂前進
        if st.data[st.top] == i:                                     #如果top所指的數字等於目前所要pop的數字
            st.pop()                                                 #pop
            ans.append("pop")                                        #答案新增pop這個步驟
        else :                                                       #若堆疊順序錯誤
            ans = []                                                 #答案為空list
            break                                                    #break
    return ans                                                       #回傳答案

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)

#留言板