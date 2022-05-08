from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    stack_in = Stack(len(in_cabin))#stack的長度=in_cabin的長度
    j=0 #用來控制out_cabin
    x=0 #計算push次數
    y=0 #計算pop次數
    A=[] 
    B=[]
    for i in range(len(in_cabin)): #看in_cabin的長度多大就跑幾次
        stack_in.push(in_cabin[i]) #push進stack
        A.append("push ")          #紀錄在A
        x+=1                       #PUSH次數+1
        while(not stack_in.isEmpty()): #偵測stack是否非空

            a=stack_in.pop()          #若非空 則pop
              
            if (out_cabin[j] == a):    #若stack.top與out相等

                A.append("pop")        #pop出
                y+=1                   #pop次數+1
                                           
                j = j + 1              #這次成功,往out的下一個位置看
            else:
                stack_in.push(a)      #若失敗，補回去
                break
    if(x+y==len(in_cabin)*2)and(x==y):        #若push+pop等於總長度*2且push次數等於pop次數則回傳A 
        return A
    else:
        return B                              #若不等於則回傳[]
        
    
            


        
    

    
     

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)

#留言板