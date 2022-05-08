from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    ans = []
    in_num = 0
    out_num = 0
    st = Stack(len(in_cabin))

    while(out_num < len(out_cabin)):

        if st.isEmpty():
            st.push(in_cabin[in_num])
            ans.append('push')
            in_num += 1
        if st.isFull() and st.data[st.top] != out_cabin[out_num]:
            ans=[]
            break
        if in_num == len(in_cabin) and st.data[st.top] != out_cabin[out_num]:
            ans=[]
            break
        
        if st.data[st.top] == out_cabin[out_num]:
            st.pop()
            ans.append('pop')
            out_num += 1
        elif st.data[st.top] != out_cabin[out_num]:
            st.push(in_cabin[in_num])
            ans.append('push')
            in_num += 1
    return ans


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)



#留言板