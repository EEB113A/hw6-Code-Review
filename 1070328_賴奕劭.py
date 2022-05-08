from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    stack_step = []                                 # 欲回傳之list先定義為空的list
    stack_len = len(in_cabin)
    st = Stack(stack_len)

    for i in in_cabin:
        st.push(i)                                  # push進st裡面
        stack_step.append('push')                   # stack_step加入push
        for j in range(st.top, -1,-1):              # 從st往回檢查
            if st.data[j] == out_cabin[0]:
                st.pop()                            # pop進st裡面
                stack_step.append('pop')            # stack_step加入pop
                out_cabin.remove(out_cabin[0])
            else:
                break
    if st.top != -1:                                # 若st內還有值
        stack_step = []                             # 則回傳值為空的list
    
    return stack_step


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板