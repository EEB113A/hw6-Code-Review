from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    num_in=0                                                              #進來次數
    num_out=0                                                             #出來次數
    lst=[]                                                                #設空的list
    sk=Stack(len(in_cabin))

    while(num_out<len(out_cabin)):                                        #設定這個迴圈執行得次數

            if sk.isEmpty():
                sk.push(in_cabin[num_in])                                 #空的push下一個，並list新增push
                lst.append('push')
                num_in += 1
            if( sk.isFull() or num_in==len(in_cabin)) and out_cabin[num_out] != sk.data[sk.top]:
                lst=[]                                                    
                break 

            if sk.data[sk.top]!=out_cabin[num_out]:                       #車站的頂層和預設車站出來不一樣，就push
                sk.push(in_cabin[num_in])
                lst.append('push')
                num_in += 1
            elif sk.data[sk.top] == out_cabin[num_out]:                   ##車站的頂層和預設車站出來一樣，就pop
                sk.pop()
                lst.append('pop')
                num_out += 1
    return lst

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板