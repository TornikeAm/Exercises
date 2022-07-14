'''
Firstly we need to find longest non-increasing suffix in the word
we then need to identify the separating point of prefix and suffix
then find rightmost successor of the pivot in the suffix, swap those 2
then we reverse the suffix to make it as low as possible.
'''

def bigger_is_greater(w):
    res = ''
    w=list(w)
    # print(w)

    i = len(w) -2
    ##finding the breaking point in word
    ### we need to find that breaking point to swap that with other char to get next bigger word
    while i >= 0 and w[i] >= w[i+1]:
        i-=1
    if i== -1:
        ### if it goes out of bound that means it cannot find greater word than original
        res='No answer'
    else:
        j= len(w)-1
        #from last char till i. we try to find successor of i
        while j >=i and w[j] <= w[i]:
            j-=1
        # then we swap those to and reverse.
        w[i],w[j] = w[j],w[i]
        w=''.join(w)
        res = w[:i+1] + w[i+1:][::-1]

    return res

inp = int(input('input Number of cases : \n'))
for i in range(inp):
    w = input('Input word : ')

    print(bigger_is_greater(w) + '\n')
