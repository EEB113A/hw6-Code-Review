from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    len_out_cabin = len(out_cabin)      #判斷out_cabin的長度
    station = Stack(len_out_cabin)      
    ans = []                            #定義ans為存放答案的list
    i = 0
    k =0
    while i < len(in_cabin):            
        station.push(in_cabin[i])       #將in_cabin的數字加進station
        ans.append("push")              #每加一次就在ans裡再加push
        j = 0
        while j < len_out_cabin:
            if out_cabin == []:         #當out_cabin被刪到變空集合即break
                break
            elif out_cabin[0] == station.data[k]:
                station.pop()           #刪除station當前指到的數
                ans.append("pop")       #每出站一次就在ans裡再加pop
                out_cabin.pop(0)        #刪除out_cabin第0項
                j = 0
                k -= 1
                continue
                
            j += 1
        i += 1
        k += 1
    if len(ans) != 2*len_out_cabin:     #當不符合這個條件即為不正常，所以輸出空集合
        ans =[]
    return ans
    


if __name__ == "__main__":
    step = iostep(in_cabin =    [1,2,3], out_cabin =     [2, 1,3])
    print(step)

#留言板