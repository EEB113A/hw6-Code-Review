from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list 

    # in_cabin和out_cabin長度相等
    if len(in_cabin) != len(out_cabin):  
        return False
    # 設一個空list作車站
    station = []
    # 設一個空list用來收集結果並回傳
    station_list = []
    j = 0
    for i in range(len(in_cabin)):
        # in_cabin的第i個值加進station
        station.append(in_cabin[i])
        station_list = station_list + ['push'] * 1
        # 一直進站直到station的最後一個位置的值等於out_cabin的第j個值
        while station and station[-1] == out_cabin[j]:
            station.pop() 
            j += 1  
            station_list = station_list + ['pop'] * 1
    if i == j - 1:
        return station_list
    else:
        return []

    


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)
    # ['push', 'push', 'pop', 'pop', 'push', 'pop']
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [3, 1, 2])
    print(step)
    # []
    step = iostep(in_cabin = [1, 2, 3, 4, 5, 6, 7], out_cabin = [2, 4, 6, 5, 3, 7, 1])
    print(step)
    # ['push', 'push', 'pop', 'push', 'push', 'pop', 'push', 'push', 'pop', 'pop', 'pop', 'push', 'pop', 'pop']
    step = iostep(in_cabin = [1, 2, 3, 4, 5], out_cabin = [3, 4, 1, 2, 5])
    print(step)
    # []

#留言板