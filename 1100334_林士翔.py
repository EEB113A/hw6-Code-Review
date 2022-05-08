from stack_diy import Stack

def iostep(in_cabin, out_cabin):    
    st=Stack(len(in_cabin)) # 建立一個 Stack 物件 st;   
    lst=[]    # 建立一個空 list
    start=0    # 從 in_cabin push 到 out_cabin 的起始點
    for i in out_cabin:  # 抓出 out_cabin 的element 

        if i in st.data and st.data[st.top]!=i:# 直接判斷i是否在st裡和st.data[st.top]是否等於i，如果都符合代表不成立
            lst=[]
            break

                                  
        for term in range(start,in_cabin.index(i)+1):# last小於i在in_cabin的位置才要push
            st.push(in_cabin[term])
            lst.append("push")
            start+=1        
                    
        st.pop() # 此時st.data[st.top]一定等於i,所以要pop
        lst.append("pop") 
                
    return lst


        


if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)

#留言板