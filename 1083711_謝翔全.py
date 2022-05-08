from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    trainlen = len(in_cabin) #車廂數量
    station = Stack(trainlen) #車站堆疊
    step = [] #記錄Push和Pop
    count = 0 #給out_cabin的計數器

    for i in range(0, trainlen):
        station.push(i+1)
        step.append("Push")
        while out_cabin[count] == station.data[station.top]: #判斷out_cabin的值是否與堆疊頂端的值相同，若相同，要列出Pop
            step.append("Pop")
            station.pop()
            count += 1
            if count == trainlen: #避免List index out of range錯誤
                break

    #跑完上面的迴圈時，當出去的車廂順序是正確時，車站堆疊應該是空的，如果是錯誤的，則車站堆疊還有車廂
    if station.isEmpty():
        return step
    else:
        return []
    



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

#留言板