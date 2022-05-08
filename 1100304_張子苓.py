from stack_diy import Stack

def iostep(in_cabin, out_cabin):

    cabin_len = len(in_cabin)
    st = Stack(cabin_len)
    move = [None]*2*cabin_len
    act = 0
    in_dex = 0   #in_cabin的index
    out_dex = 0   #out_cabin的index
    while act<=2*cabin_len-1:
        if st.data[st.top]==out_cabin[out_dex]:   #1:若stack最上面的數字 = out_cabin[out_dex] ==> pop此數字
            st.pop()
            move[act]="pop"
            out_dex+=1
            act+=1
        else:
            if in_dex == cabin_len:   #所有數皆push至stack，但無法全部pop出來　==> 跳脫迴圈
                break            
            elif in_cabin[in_dex] == out_cabin[out_dex]:   #2:若in_cabin[in_dex] == out_cabin[out_dex] ==> 將此數先push再pop
                st.push(in_cabin[in_dex])
                move[act]="push"
                act+=1
                st.pop()
                move[act]="pop"
                act+=1
                in_dex+=1
                out_dex+=1
            else:
                st.push(in_cabin[in_dex])   #若1、2皆不成立 ==> 將in_cabin[in_dex]直接push
                move[act]="push"
                in_dex+=1
                act+=1
                

    if st.top==-1:   #stack內的數字皆已pop出來 ==> 成功
        return move 
    else:   #stack內還有數字無法pop出來 ==> 失敗
        return "[]"


    
if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板