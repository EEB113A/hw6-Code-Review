from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 因為題目假設 out_cabin 為出站車廂的排列，長度與 in_cabin 相等，所以不檢查兩者長度是否一致
    # make return list
    step = [] 
    # make Station Stack
    station_Stack = Stack(len(in_cabin))
    # 透過使用index數值，以避免較耗效能的 list's pop method
    index_already_out = 0
    index_in = 0
    while True:
        # 如果以下condition成立，則表示所有cabin皆已出站
        if index_already_out == len(out_cabin): 
            return step 
        # 如果以下condition成立，則表示該out_cabin可以出站
        elif station_Stack.data[station_Stack.top] == out_cabin[index_already_out]: 
            station_Stack.pop()
            index_already_out += 1 
            step.append('pop')
        # 如果以下condition成立，則表示所有cabin皆已進站
        elif index_in == len(in_cabin):
            return []
        # 如果以上三個condition皆不成立，則表示新的cabin可以進站
        else:
            station_Stack.push(in_cabin[index_in])
            index_in += 1
            step.append('push')


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)

    # ########## Test Data ###################################
    # # Test data 1
    # in_cabin = [1,2,3]
    # out_cabin = [3,1,2]
    # print(iostep(in_cabin, out_cabin))
    # # Test data 2
    # in_cabin = [1,2,3,4,5,6,7]
    # out_cabin = [2,4,6,5,3,7,1]
    # print(iostep(in_cabin, out_cabin))
    # # Test data 3
    # in_cabin = [1,2,3,4,5]
    # out_cabin = [3,4,1,2,5]
    # print(iostep(in_cabin, out_cabin))
    # # Test data 4
    # in_cabin = [1,2,3,4,5]
    # out_cabin = [3,4,5,2,1]
    # print(iostep(in_cabin, out_cabin))
    

#留言板