from re import X
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    sta=Stack(len(in_cabin))
    step=[]
    while out_cabin:
        if in_cabin[0]==out_cabin[0]: #(1)如果in_cabin第一個數=out_cabin第一個數
            step.append("push") #先印push
            step.append("pop")  #再印pop
            in_cabin.pop(0)  #在in_cabin移除已經push的數
            out_cabin.pop(0) #在out_cabin移除已經pop的數
            
            if sta.top==-1 and in_cabin==[] and in_cabin==[]: #如果sta.top內沒有數且in,out都沒有數,就離開
                break 

        if sta.data[sta.top]==out_cabin[0]: #(2)如果sta.top的數=out_cabin的第一個數
            step.append("pop")  
            sta.top = sta.top -1 #sta.top回到還沒pop的數
            out_cabin.pop(0) #在out_cabin移除已經pop的數
            if sta.top==-1 and in_cabin==[] and in_cabin==[]: #如果sta.top內沒有數且in,out都沒有數,就離開
                break
            
        if in_cabin==[] and sta.data[sta.top]!=out_cabin[0]: #如果in_cabin內沒有數且sta.top的數!=out_cabin第一個數
            step=[] #進出站方式不成立 step=[]
            break    

        if in_cabin[0]!=out_cabin[0] and sta.data[sta.top]!=out_cabin[0]: #如果(1),(2)皆不成立
            step.append("push") #印push
            sta.push(in_cabin[0]) #in_cabin第一個數進到車站中
            in_cabin.pop(0) #在in_cabin移除已經push的數
            
        if in_cabin==[] and sta.data[sta.top]!=out_cabin[0]: #如果in_cabin內沒有數且sta.top的數!=out_cabin第一個數
            step=[] #進出站方式不成立 step=[]
            break

    return step    #回傳step結果

    
    


if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)

#留言板