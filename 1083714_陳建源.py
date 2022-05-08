from inspect import stack
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    result = [] #return 結果
    train_station = Stack(len(in_cabin)) 
    count = 0 # out_cabin的index
    
    for i in range(0,len(in_cabin)):
        train_station.push(i+1)
        result.append('push')
        #當out_cabin的值等於train_station的最後的值就pop
        while out_cabin[count] == train_station.data[train_station.top]:
            result.append('pop') 
            train_station.pop()
            count += 1 
            if count == len(in_cabin):
                break
    if train_station.isEmpty():#使用isEmpty()來確定train_station是否清空
        return result
    else: #train_station沒有清空代表清空順序不對
        result = []
        return result

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7] , out_cabin = [2,4,6,5,3,7,1])
    print(step)

#留言板