from stack_diy import Stack


def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    L_in = len(in_cabin) #給in_cabin長度
    L_out = len(out_cabin) #給out_cabin長度
    i_in = 0  #in_cabin index
    i_out = 0  #out_cabin index
    outputword = '' #輸出的字(push、pop)
    ans1='' #輸出[
    ans2='' #輸出]
    stc = Stack(L_in) #stack
    cp = 0 #計數pop
    null = 0  #判斷範例2 ([])用的
    for x in range(L_in):  #進入迴圈
        if cp == L_out:  #判斷cp == L_out(計數pop是否與out_cabin長度相同)
            break  #是的話跳出迴圈

        while in_cabin[i_in] != out_cabin[i_out]: #迴圈判斷in_cabin長度是否與out_cabin長度不相同
            stc.push(in_cabin[i_in]) #不相同時進入，push in_cabin
            outputword = outputword + '\'push\', ' #輸出push
            i_in = i_in+1  #in_cabin index+1

        if in_cabin[i_in] == out_cabin[i_out]: #判斷in_cabin長度是否與out_cabin長度相同
            stc.push(in_cabin[i_in]) #相同時進入，push in_cabin
            outputword = outputword + '\'push\', ' #輸出push
            i_in = i_in+1 #in_cabin index+1

            stc.pop() #pop out_cabin
            outputword = outputword + '\'pop\', ' #輸出pop
            i_out = i_out+1 #out_cabin index+1
            cp = cp+1 #計數pop

        if cp == L_out: #判斷cp == L_out(計數pop是否與out_cabin長度相同)
            break #是的話跳出迴圈

        for y in range(i_in): #進入迴圈
            null = 0 #null=0
            for z in range(i_in): #進入迴圈
                if cp == L_out:  #判斷cp == L_out(計數pop是否與out_cabin長度相同)
                    break  #是的話跳出迴圈

                if in_cabin[z] == out_cabin[i_out]: #判斷in_cabin長度是否與out_cabin長度相同
                    stc.pop() #pop out_cabin
                    outputword = outputword + '\'pop\', ' #輸出pop
                    i_out = i_out+1 #in_cabin index+1
                    cp = cp+1 #計數pop
                    null = null+1 #null+1
                    if null > 1: #判斷是否null>1
                        return [] #回傳空集合
    outputword=outputword[:-1] #消除最後的,
    outputword=outputword[:-1] #消除最後的,
    ans1=ans1+'[' #輸出[
    ans2=ans2+']' #輸出]
    return ans1+outputword+ans2 #輸出解答
if __name__ == "__main__":
    """
    step = iostep(in_cabin=[1, 2, 3], out_cabin=[2, 1, 3])
    print(step)
    """
    """
    step = iostep(in_cabin=[1, 2, 3], out_cabin=[3, 1, 2])
    print(step)
    """
    """
    step = iostep(in_cabin = [1,2,3,4,5,6,7],out_cabin = [2,4,6,5,3,7,1])
    print(step)
    """
    
    step = iostep(in_cabin = [1,2,3,4,5],out_cabin = [3,4,1,2,5])
    print(step)
    
    

#留言板