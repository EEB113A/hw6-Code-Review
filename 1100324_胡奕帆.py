from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    st=Stack(len(in_cabin))#將長度放入stack
    out_index=0
    move=[""]*len(in_cabin)*2#設立空字串放push和pop
    st.push(in_cabin[0])#第一個數字進站
    in_index=1#進佔次數
    move[0]="push"#先設地0巷為push
    movetime=1#為進佔進度
    while movetime<=len(in_cabin)*2-1:#執行次數為in和out相加
        if  st.data[st.top]==out_cabin[out_index]:#如果最後一個數字和out指定的出站數字一樣的話就出站
            st.pop()
            out_index+=1
            move[movetime]="pop"
            movetime+=1
        else:#沒出站必定進佔
            if in_index==len(in_cabin):
                break
            st.push(in_cabin[in_index])
            in_index+=1
            move[movetime]="push"
            movetime+=1
    if st.top==-1:#進站出站皆完成且車站為原樣，回傳move字串
        return move
    else:#其餘回傳空字串
        return"[]"
            



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)


#      無stack版本
#from stack_diy import Stack

#def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
#    L=len(in_cabin)
#    lst=[0,in_cabin[0]]
#    lst1=["push"]
#    lst2=[]
#    no=[]
#    a=0
#    b=1
#    err=0
#    for i in range(L+2):
#        if  out_cabin[a]!=lst[-1]:
#            lst1.append("push")
#            try:
#                lst.append(in_cabin[b])
#            except IndexError:
#                err+=1
#                break
#            b+=1
#        elif out_cabin[a]==lst[-1]: 
#            out_cabin[a]==lst[-1]
#            lst1.append("pop")
#            lst2.append(out_cabin[a])
#            lst.pop()
#            a+=1
#        else:
#            break
#    if err!=0:
#        return []
#    if lst2 != out_cabin:
#        return []
#    if lst2 == out_cabin:
#        return lst1
#if __name__ == "__main__":
#    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
#    print(step)

#留言板