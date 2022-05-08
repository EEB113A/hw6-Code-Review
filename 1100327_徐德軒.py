from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    st=Stack(len(in_cabin))
    output=[]#用來記錄step
    check=[]#用來模擬
    check2=[]#每push一次就把值從後插入check2
    check3=[]#每pop一次就pop一個check2的值進入check3
    for h in in_cabin:#複製一個跟in_cabin一樣的list
        check.append(h)
    for i  in out_cabin:#把out_cabin從頭讀一遍           
        if i in check:#如果值還在check內就代表還沒被push過
            for j in in_cabin:#判斷需要push幾次
                check2.append(j)
                if j in check:#若還沒讀到要找的值就在output插入'push'並刪除check1首個元素，避免push重複的值
                    st.push(j)
                    output.append('push')
                    del check[0]
                if j==i:#找到準備要pop的值就跳出迴圈
                    break      
        st.pop()
        check3.append(check2.pop())#將check最後進入的值pop出來，模擬stack的pop
        output.append('pop') 
    if check3==out_cabin:#若check3中的結果與out_cabin相同就代表可以以這個順序進出站
        return output
    else:
        return []
    





if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3]  , out_cabin = [2,1,3])
    print(step)

#留言板