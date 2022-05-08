from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lst = Stack(len(in_cabin))
    ret_lst = []
    tmp_in = 0
    tmp_out = 0

    try:#檢查是否成立
        while(tmp_out != len(out_cabin)):#判斷是否完成所有的push以及pop動作
            if lst.data[lst.top] != out_cabin[tmp_out]:#判斷執行push or pop
                #push
                lst.push(in_cabin[tmp_in])
                ret_lst.append("push")
                tmp_in += 1
            else:
                #pop
                lst.pop()
                ret_lst.append("pop") 
                tmp_out += 1
        return ret_lst
    except:
        return []

    



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

    step = iostep(in_cabin = [1, 2, 3, 4, 5, 6, 7], out_cabin = [2, 4, 6, 5, 3, 7, 1])
    print(step)

#留言板