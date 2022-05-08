from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    output_list=[]   #這邊先定義一個list叫做output_list
    size=len(in_cabin)  #先取得該list的長度
    stack=Stack(size)   #這邊用Stack的類別
    i=0                 #i這邊做初始化的動作
    
    for j in range(len(in_cabin)):      #先從第一個去做對比
        stack.push(in_cabin[j])
        output_list.append('push')      #這邊去append"push"這個單字
        if in_cabin[j]==out_cabin[i]:   #如果是要pop的店就從這邊塞入
            while stack.top>-1 and stack.data[stack.top] == out_cabin[i]:   #繼續比對下一個字，>-1且剛好一樣的話繼續給pop，不是的話往下
                stack.pop()
                output_list.append('pop')#這邊去append"pop"這個單字
                i=i+1                    #這邊做累加

    if stack.top != -1:     #這邊去做題目第二個要求，當不等於-1 直接給[]
        output_list=[]
    
    return output_list      #這邊將值回傳到main


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板