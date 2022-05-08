from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    length = len(in_cabin)
    station = Stack(length)
    ans_list = []
    check = False
    for i in range(0,length):
        if check:
            break
        while (True):
            if out_cabin[i] != station.data[station.top] and in_cabin == []:
                ans_list =[]
                check = True
                break
            if out_cabin[i] != station.data[station.top]:
                station.push(in_cabin[0])
                del in_cabin[0]
                ans_list.append("push")
            elif out_cabin[i] == station.data[station.top]:
                station.pop()
                ans_list.append("pop")
                break
    return ans_list
if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)

#留言板