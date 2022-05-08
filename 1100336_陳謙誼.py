from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list

    
    #建一個空的Step
    Step=[]
    Len=len(in_cabin)
    #先定義一個sta=Stack()
    st=Stack(Len)
    
    k=-1   #list的話第一個是0，因為st有push一個值進去就加1，所以起始值設為-1，這樣第一個加進去的值才會是st.data[0](第一個數)
    while (in_cabin!=[]  or out_cabin!=[]): #在in和out的cabin皆不為[]的情況下持續跑迴圈
        #1.如果in_cabin[0]==out_canin[0]，就先push 再pop
        if in_cabin!=[] and in_cabin[0]==out_cabin[0]: #如果沒in_cabin!=[]就會out of range
            Step.append("push")    #在Step結尾加push
            Step.append("pop")    #在Step結尾加pop
            st.push(in_cabin[0])   #把in_cabin的第一個push進st內(pop下的那行，只要把in_cabin的一個數push進st內就把in_cabin push進st內的那個數刪掉)
            st.pop()               #把st內的鋼加進去的pop出來
            del in_cabin[0]         #把in_cabin的第一個刪掉，讓下一個變成第一個
            del out_cabin[0]       #把out_cabin的第一個刪掉，讓下一個變成第一個

        #2.如果Stack的top==out_cabin[0]，就pop出去
        elif st.data[k]==out_cabin[0]:  #st的top是st.data[剛push進去的值]
            Step.append("pop")   #在Step結尾加pop
            st.pop()   #st帶入Stack(堆疊)中的pop跑，把後放入的(top)放入
            del out_cabin[0]  #把out_cabin的第一個刪掉，讓下一個變成第一個
            k-=1   #從st pop出去就-1
            

        #3.假設上述兩個都不成立，就push
        elif  in_cabin!=[] and in_cabin[0]!=out_cabin[0] and st.data[k]!=out_cabin[0]:
            st.push(in_cabin[0])     #把in_cabin的第一個push進st內
            Step.append("push")     #在Step結尾加push
            del in_cabin[0]        #把in_cabin的第一個刪掉，讓下一個變成第一個
            k+=1   #push進來一個數到st就加1

            
        #4.上述的皆不符合，Step設為[]，跳出迴圈
        elif not in_cabin and st.data[0]!=0:
            Step=[]
            break
    
    #最後就return step即可
    return Step






if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    #(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    #(in_cabin = [1, 2, 3], out_cabin = [3, 1, 2])
    #(in_cabin = [1,2,3,4,5,6,7],out_cabin = [2,4,6,5,3,7,1])
    print(step)

#留言板