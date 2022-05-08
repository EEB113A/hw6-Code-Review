from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lst = []                                 #定義一個list來t存放進行的步驟 ("push" or "pop")
    len_in = len(in_cabin)                   #求出進來的列車車廂長度
    len_out = len(out_cabin)                 #求出出去的列車車廂長度
    st = Stack(len_out)                      #建立一個Stack物件代表車站
                        
    i = 0                                    #定義i的初始值為0
    while i < len_in:                        #外面的迴圈在寫i表示index值從0~len_in-1。
        st.push(in_cabin[i])                 #將index 0的列車車廂開入車站
        lst.append("push")                   #在lst中加入"push" 字串
        j = 0                                #定義j的初始值為0
        while j < len_out-1:                 #裡面的迴圈在寫j表示index值從0~len_out-2
            if out_cabin == []: 
                break                        #如果out_cabin中的內容為空的話，跳出迴圈。
            elif out_cabin[0] == st.data[j]: #如果目前已進站的列車車廂等於出站列車車廂的安排順序 index 0的位置
                st.pop()                     #將該列車車廂開出站
                lst.append("pop")            #在lst中加入"pop" 字串
                out_cabin.pop(0)             #將出站列車車廂的安排順序 為index 0的位置的值刪除，原本在 index 1的值變成在 index 0。
                j=0                          #將j更新為0，下一次檢查才能將已進站的列車車廂出站。
                continue                     #i跑下一個index值
            j+=1                             #j每次加1
        i+=1                                 #i每次加1

    if len(lst) != 2 * len_out:              #判斷是否有車廂無法按照出站順序的狀況，透過檢查跑完迴圈後的lst長度有沒有不等於進來的列車車廂長度乘於2
        lst =[]                              #(因為正常情況下有進站("push")和出站("pop")，並且在lst中的個數為進站列車長度的兩倍。)
                                   
    return lst                               #回傳 lst 給主程式


if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3,4,5,6,7], out_cabin =  [2,4,6,5,3,7,1])
    print(step)

#留言板