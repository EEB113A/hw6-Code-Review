from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    size = len(out_cabin)
    stack = Stack(size)
    inn = 0
    out = 0
    answer = []
    while (out<size):      #當輸出達到size停止
        
        if inn == size and stack.data[stack.top]!=out_cabin[out]:   #判斷是否可以出出去完
            answer = []
            break
        if stack.data[stack.top]!=out_cabin[out]:  #將列車進站
            stack.push(in_cabin[inn])
            inn+=1
            answer.append('push')
        if stack.data[stack.top]==out_cabin[out]:   #將列車以指定順序出站
            out+=1
            stack.pop()
            answer.append('pop')
    return(answer)
    

    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2,1,3])
    print(step)

#留言板