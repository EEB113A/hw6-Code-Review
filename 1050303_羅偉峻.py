from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    step = []                       #先設定一個空list

    stack = Stack(len(in_cabin))    #車站大小跟in一樣

    for in_number in in_cabin:      #依照in次序進來
        stack.push(in_number)
        step.append('push')         #進來車站就在step裡加push

        while len(out_cabin) > 0 and out_cabin[0] == stack.data[stack.top]:   #當還需要out出去 且 out第一位數是車站最後一個時
            stack.pop()                     #就移除車站裡的目前最後一位進來的
            step.append('pop')              #且在step裡加pop
            out_cabin = out_cabin[1:]       #當out之後，刪掉已經出去的車廂

    if len(out_cabin) == 0:                 #若out為零，代表沒有車要出去了
        return step                         #那就return step
    else:
        return []                           #若out還需要車出去，但車站的車不匹配，那就return 空list


if __name__ == "__main__":
    step = iostep( in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    print(step)

#留言板