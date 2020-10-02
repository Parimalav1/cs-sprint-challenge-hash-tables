'''
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
d = {4: 0, 6: 1, 10: 2}
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
'''

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # for i in range(length):
    #     for j in range(i+1, length):
    #         if weights[i] + weights[j] == limit:
    #             if weights[i] > weights[j]:
    #                 return [i, j]
    #             else:
    #                 return [j, i]
    # return None

    d = {}

    for i in range(length):
        complement_wt = limit - weights[i]
        if complement_wt in d:
            complement_idx = d[complement_wt]
            return [max(i, complement_idx), min(i, complement_idx)]
            # if i > complement_idx:
            #     return [i, complement_idx]
            # else:
            #     return [complement_idx, i]
        else:
            d[weights[i]] = i

    return None



