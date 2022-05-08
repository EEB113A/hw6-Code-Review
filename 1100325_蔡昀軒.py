from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    wrong = 0
    cabin = Stack(len(in_cabin))
    step = list()
    poptime = 0
    for i in in_cabin:
        cabin.push(i)
        step += ['push']               #每次push完在step中加入'push'
        while i >= out_cabin[poptime]: #當i >= out_cabin[poptime] 代表 out_cabin[poptime] 需要被 pop
            if cabin.data[cabin.top]!=out_cabin[poptime]: #如果要pop時結果是錯的
                wrong=1
            poptime += 1
            cabin.pop()
            step += ['pop']            #每次pop完在step中加入'pop'
            if poptime == len(out_cabin):
                break
    if wrong==1:
        return[]
    
    return step

            
    

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)

#留言板