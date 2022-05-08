from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    st = Stack(len(in_cabin)) #建一個Stack(車站)
    j = 0
    L = []
    c = 0
    for i in range(len(in_cabin)):
        st.push(in_cabin[i]) #從 in_cabin push到stack中
        L.append("push")
        c += 1
        while not st.isEmpty(): #stack不為空
            a = st.pop()        #從stack中pop出去到a暫存
            if(out_cabin[j] == a): #若out_cabin的第j項和a相符，代表確定有用到此項，即pop
                L.append("pop")    
                c += 1
            else:               #若沒有用到則push回stack
                st.push(a)
                break 
            j = j + 1
    if c == 2*len(in_cabin):    #合法的
        return L
    else:                       #非法的
        return []

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    #step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    #step = iostep(in_cabin = [1,2,3], out_cabin = [3,1,2])
    print(step)

#留言板