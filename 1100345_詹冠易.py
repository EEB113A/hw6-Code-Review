from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    lens = len(in_cabin) #總共多少台車
    station = Stack(lens) #創建一個長度lens的Stack
    list = [] #空步驟list
    cin = 0 #count 車已經進入的次數
    cout = 0 #count 車已經離開的次數

    while cin < lens: #如果全部車都已經進入過就離開迴圈

        station.push(in_cabin[cin]) #將in_cabin[cin]對照的車號 push
        list.append("push") #list 新增"push"

        while station.data[station.top] == out_cabin[cout]: #station.data[station.top]] = 最頂層的車
    
            station.pop() #將最頂層對照的車號 pop
            list.append("pop") #list 新增"pop"

            cout += 1 #總共已經離開了多少台車
            if cout == lens: #如果全部車都已經離開就離開迴圈
                break
        cin += 1 #總共已經進入了多少台車
        
    if len(list) != 2*lens: #總共步驟的長度，一台車會有push和pop兩個步驟
        list = [] #如果沒有全部車都離開 list = 空list
    return list




if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)

#留言板