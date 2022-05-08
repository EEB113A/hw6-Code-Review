from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    st=Stack(len(in_cabin)) 
    out_index=0    
    move=[""]*len(in_cabin)*2
    st.push(in_cabin[0])
    in_index=1
    move[0]="push"
    movetime=1
    while movetime<=len(in_cabin)*2-1:
        if st.data[st.top]==out_cabin[out_index]:  #st最上層是out_cabin[out_index], 將其拖出(pop)
            st.pop()
            out_index+=1
            move[movetime]="pop"
            movetime+=1
        else:
            if in_index==len(in_cabin): #已將in_cabin全部push進st, 但無法全數pop出來, 失敗跳出
                break
            st.push(in_cabin[in_index])
            in_index+=1
            move[movetime]="push"
            movetime+=1
    if st.top==-1:  #成功
        return move
    else:
        return "[]" 
 
if __name__ == "__main__":
    #step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    step=iostep(in_cabin=[1,2,3,4,5],out_cabin=[1,5,4,3,2])
    print(step)




if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板