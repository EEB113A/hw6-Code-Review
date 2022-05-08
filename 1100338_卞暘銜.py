from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    input = 0
    output = 0
    Size = len(out_cabin)
    stack = Stack(Size)
    answer = []
    while output<Size:
        if input == Size and stack.data[stack.top]!=out_cabin[output]:
            answer = []
            break  
        if stack.data[stack.top]!=out_cabin[output]:
            stack.push(in_cabin[input])
            input+=1
            answer.append('push')
        if stack.data[stack.top]==out_cabin[output]:
            output+=1
            stack.pop()
            answer.append('pop')
    return(answer)
    
    



if __name__ == "__main__":
    hw6_IN = [
    [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
    [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
    [[1, 2, 3, 4, 5], [2, 3, 5, 4, 1]],
    [[1, 2, 3, 4, 5], [2, 5, 4, 1, 3]],
    [[1, 2, 3, 4, 5, 6, 7], [7, 3, 5, 1, 4, 2, 6]],
    [[1, 2, 3, 4, 5, 6, 7], [2, 5, 4, 6, 3, 1, 7]],
    [[1, 2, 3], [3, 1, 2]],
    [[1, 2, 3], [2, 1, 3]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 6, 9, 4, 10, 2, 5, 7, 3, 8]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 5, 8, 3, 9, 2, 4, 10, 6, 7]],
    [[1, 2, 3, 4], [3, 2, 4, 1]],
    [[1, 2, 3, 4], [4, 3, 1, 2]]
]
    hw6_ANS = [
    ['push', 'pop', 'push', 'pop', 'push', 'pop', 'push', 'pop', 'push', 'pop'],
    ['push', 'push', 'push', 'push', 'push', 'pop', 'pop', 'pop', 'pop', 'pop'],
    ['push', 'push', 'pop', 'push', 'pop', 'push', 'push', 'pop', 'pop', 'pop'],
    [],
    [],
    ['push', 'push', 'pop', 'push', 'push', 'push', 'pop','pop', 'push', 'pop', 'pop', 'pop', 'push', 'pop'],
    [],
    ['push', 'push', 'pop', 'pop', 'push', 'pop'],
    [],
    [],
    ['push', 'push', 'push', 'pop', 'pop', 'push', 'pop', 'pop'],
    []
]
    score = 20
    for i in range(len(hw6_IN)):
        if iostep(hw6_IN[i][0],hw6_IN[i][1]) == hw6_ANS[i]:
            score += 5
    print(score)

#留言板