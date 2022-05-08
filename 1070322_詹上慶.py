from tarfile import FIFOTYPE
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    outputlist=[]#最後的return
    size=len(in_cabin)#stack 的大小
    sta=Stack(size)
    i=0
    
    for j in range(len(in_cabin)):#從要輸出的第一個點慢慢比對
        sta.push(in_cabin[j])
        outputlist.append('push')
        if in_cabin[j]==out_cabin[i]:#13-15慢慢塞入假如加入的剛剛好是要pop的點
            while sta.top>-1 and sta.data[sta.top] == out_cabin[i]:#16-19 pop後繼續比對輸出的下一個點假如還是一樣繼續pop
                sta.pop()
                outputlist.append('pop')
                i=i+1

    if sta.top!=-1:#假如無法順立有輸出，sta.top不會到-1，用此判斷錯誤
        outputlist=[]
    
    return outputlist

if __name__ == "__main__":
    step = iostep(in_cabin =    [1,2,3,4,5], out_cabin =     [3,4,2,1,5])
    print(step)

#留言板