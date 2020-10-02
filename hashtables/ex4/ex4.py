'''python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ] = [1, 3, 4]
'''

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # result = []
    # for elem in a:
    #     if elem < 0:
    #         continue
    #     else:
    #         for num in a:
    #             if num == -elem:
    #                 result.append(elem)

    result = []
    d = {}
    for elem in a:
        if elem == 0:
            continue
        d[elem] = True
        if -elem in d:
            result.append(abs(elem))



    return result

    # result = []
    # d = {}
    # for elem in a:
    #     d[elem] = True
    #     print(d[elem])
    #     if -elem in d:
    #         print(-elem)
    #         if elem > 0:
    #             result.append(elem)
    #         else:
    #             result.append(-elem)
        

    # return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
