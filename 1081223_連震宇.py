from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    size = len(in_cabin)   # 讀取輸入長度

## 方法一   
    # A = [None]             # 建立儲存 push進去的空list，也就是車站 Stack
    # B = size*[None]*2      # 建立儲存'push'&'pop'的空list
    # B_index = 0            # B list的起始位置

    # in_cabin.append(None)  # 給予 None 避免在 del 後變成 [] list 導致判斷式的錯誤
    # out_cabin.append(None) # 給予 None 避免在 del 後變成 [] list 導致判斷式的錯誤

    # for i in range(0,size):
    #     if(A[-1] == out_cabin[0] and A != [None] and out_cabin != [None]): # 當 push的值和要 pop的值相等，並且 A list 裡的值不為[None]，out_cabin list 裡的值不為[None]
    #         del A[-1], out_cabin[0]         # 刪除儲存在 stack 裡的值和要pop的值
    #         B[B_index] = 'pop'              # 儲存動作'pop'到 B list裡
    #         B_index = B_index + 1           # 換到下一格          
    #     if(in_cabin[0] != out_cabin[0] and in_cabin[0] != None and A[-1] != out_cabin[0]): # 當 push的值和要 pop的值不相等，並且要 push的值不為[None]，Stack裡最外面的值和要 pop的值不相等
    #         A.append(in_cabin[0])           # 將要 push的值儲存到 Stack裡
    #         del in_cabin[0]                 # 刪除要 push的值
    #         B[B_index] = 'push'             # 儲存動作'push'到 B list裡
    #         B_index = B_index + 1           # 換到下一格 
    #     if(in_cabin[0] == out_cabin[0] and in_cabin[0] != None and out_cabin[0] != None): # 當 push的值和 pop的值相同，並且 in_cabin list 裡的值不為[None]，out_cabin list 裡的值不為[None]
    #         B[B_index] = 'push'             # 儲存動作'push'到 B list裡
    #         B_index = B_index + 1           # 換到下一格
    #         del in_cabin[0], out_cabin[0]   # 刪除 push的值和 pop的值
    #         B[B_index] = 'pop'              # 儲存動作'pop'到 B list裡
    #         B_index = B_index + 1           # 換到下一格       
    #     if(in_cabin == [None] and out_cabin == [None]):       # 如果要 push和 pop的值都使用完畢，代表進出 Stack 是正確的                 
    #         return B                        # 回傳 B list
    #     elif(in_cabin[0] == None and A[-1] != out_cabin[0]):  # 如果已經沒有要 push進去的值，並且 Stack裡最外面的值和要 pop出來的值並不相等時
    #         return []                       # 回傳空的list
##----------------------------------------------------------------------------------------
##方法二
    st = Stack(size)  # 設定Stack長度
    i = 0             # in_cabin list 起始位置
    j = 0             # out_cabin list 起始位置
    q = 0             # 判斷 Stack 的值
    count = 0         # 計數長度
    C = size*[None]*2 # 建立儲存'push'&'pop'的空list
    C_index = 0       # B list的起始位置  
    
    for k in range(size):
        if(count == size): # 如果計數值和長度相等
            break          # 跳出迴圈 
        while(in_cabin[i] != out_cabin[j]): # 當輸入值和輸出值不相等
            st.push(in_cabin[i])            # push 輸入值到 Stack
            C[C_index] = 'push'             # 儲存動作'push'到 C list裡
            C_index = C_index + 1           # 換到下一格
            i = i + 1                       # 換到下一格
        if(in_cabin[i] == out_cabin[j]):    # 如果輸入值和輸出值相等
            st.push(in_cabin[i])            # push 輸入值到 Stack
            C[C_index] = 'push'             # 儲存動作'push'到 C list裡
            C_index = C_index + 1           # 換到下一格
            st.pop()                        # pop 值出去
            C[C_index] = 'pop'              # 儲存動作'pop'到 C list裡
            C_index = C_index + 1           # 換到下一格
            i = i + 1                       # 換到下一格
            count = count + 1               # 計數增加
            j = j + 1                       # 換到下一格
        if(count == size):                  # 如果計數值和長度相等
            break                           # 跳出迴圈 
        for x in range(i):
            for y in range(i):  
                if(count == size):              # 如果計數值和長度相等
                    break                       # 跳出迴圈 
                if(out_cabin[j] == in_cabin[y]):# 如果輸出值和輸入值相等    
                    st.pop()                    # pop 值出去
                    j = j + 1                   # 換到下一格
                    C[C_index] = 'pop'          # 儲存動作'pop'到 C list裡
                    C_index = C_index + 1       # 換到下一格
                    count = count + 1           # 計數增加
                    q = q + 1                   # 計數從 Stack 出去的值
                    if q > 1:                   # 如果超過兩個，代表不是從 Stack 的最外面 pop出去
                        return []               # 回傳空的list
            q = 0                               # 計數值歸零
    return C                                # 回傳 C list


       



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)

#留言板