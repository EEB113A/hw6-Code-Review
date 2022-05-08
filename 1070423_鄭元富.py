import re
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    stack_step = []
    stack_len = len(in_cabin)
    st = Stack(stack_len)
    for i in in_cabin:
        st.push(i)
        stack_step.append('push')
        for j in range(st.top, -1, -1):
            if st.data[j] == out_cabin[0]:
                st.pop()
                stack_step.append('pop')
                out_cabin.remove(out_cabin[0])
            else:
                break
    if st.top != -1:
        stack_step = []
    return stack_step

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板