from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    station=Stack(len(in_cabin))                   #建一個station物件
    step=[]                                        #建一個空的list
    
    #因為每次都只比對第0個位置的值，所以以下如果有將in_cabin[0]的值 或 out_cabin[0]的值刪掉，就代表該值已進入或離開station
    
    while True:
                
        if station.data[station.top]==out_cabin[0]:     #如果station的top的值 = out_cabin[0]的值
                station.pop()                           #將station的top的值pop出去
                step.append("pop")                      #在step裡面加入一個 'pop' 字串
                out_cabin.pop(0)                        #將out_cabin[0]的值刪掉
                                                    
        elif in_cabin[0]== out_cabin[0]:                #如果in_cabin[0]的值 = out_cabin[0]的值            
            station.push(in_cabin[0])                   #將in_cabin[0]的值push進station            
            step.append("push")                         #在step裡面加入一個 'push' 字串
            in_cabin.pop(0)                             #將in_cabin[0]的值刪掉
            
            station.pop()                               #將station的top的值pop出去(也就是剛push進來的值)
            step.append("pop")                          #在step裡面加入一個 'pop' 字串
            out_cabin.pop(0)                            #將out_cabin[0]的值刪掉
               
        else:
            station.push(in_cabin[0])                   #將in_cabin[0]的值push進station
            step.append("push")                         #在step裡面加入一個 'push' 字串
            in_cabin.pop(0)                             #將in_cabin[0]的值刪掉
                   
        #如果in_cabin裡的值都被刪掉 且 station的top的位置在-1(也就是station裡面的值都已pop掉)
        if  in_cabin==[] and station.top==-1:           
            break       
                    
        #如果in_cabin裡的值都被刪掉 但 station的top的值不等於out_cabin[0]的值(也就是station裡面還有值無法被pop掉)
        elif  in_cabin==[] and station.data[station.top]!= out_cabin[0] :     
            step=[]                                     #則step就清空
            break
            
    return step                                         #回傳step
        

if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3,4,5,6,7], out_cabin =  [2,4,6,5,3,7,1])
    print(step)

#留言板