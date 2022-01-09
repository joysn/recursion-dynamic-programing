# Best Sum
# Return shortest array of numbers whose sum is targetSum
import copy
def bestSum(targetSum, numbers):

    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    final_res = None
    for ele in numbers:
        res = copy.deepcopy(bestSum(targetSum-ele,numbers))
        if res is not None:
            res.append(ele)
            if final_res is None:
                final_res = copy.deepcopy(res)
            elif len(final_res) > len(res):
                final_res = copy.deepcopy(res)


    memo[targetSum] = copy.deepcopy(final_res)
    return memo[targetSum]


def bestSum_bottomup(targetSum,numbers):

    tab = [None for i in range(targetSum+1)]
    tab[0] = []

    for i in range(targetSum+1):
        # Only if it is not None, we can move ahead from this position
        if tab[i] != None:
            for num in numbers:
                # Check for out of bound
                # Do it only if the target is None. If it is not None, it means that we have already reached the position with smaller amount of steps
                if i+num <= targetSum and tab[i+num] is None:
                    tab[i+num] = copy.deepcopy(tab[i])
                    tab[i+num].append(num)
                    # Break if we already got targetSum
                    if i+num == targetSum:
                        return tab[i+num]

    return tab[targetSum]


    

# m is the targetSum
# n is the number of  numbers
# Brute Force
# time O(n^m*m)
# Spave O(m*m)

# Memoization
# time O(n*m*m)
# Space O(m*m)

# Bottom Up
# time = O(n*m*m)
# Space O(m*m)

if __name__ == "__main__":
    memo = dict()
    print("7,[4,5,3,7] True",bestSum(7,[4,5,3,7]))

    memo = dict()
    print("7,[4,5] False",bestSum(7,[4,5]))

    memo = dict()
 
    print("7,[2,3] True",bestSum(7,[2,3]))

    memo = dict()
    print("7,[4,2] False",bestSum(7,[4,2]))

    memo = dict()
    print("8,[2,3,5] True",bestSum(8,[2,3,5]))

    memo = dict()
    print("0,[2,3,5] False",bestSum(0,[2,3,5]))

    memo = dict()
    print("300,[7,14] False",bestSum(300,[7,14]))
    
    memo = dict()
    print("100,[1,2,5,25] True",bestSum(100,[1,2,25]))


    print("******************")
    print("Bottom Up Approach")
    print("******************")
    print("7,[4,5,3,7] True",bestSum_bottomup(7,[4,5,3,7]))
    print("7,[4,5] False",bestSum_bottomup(7,[4,5]))
    print("7,[2,3] True",bestSum_bottomup(7,[2,3]))
    print("7,[4,2] False",bestSum_bottomup(7,[4,2]))
    print("8,[2,3,5] True",bestSum_bottomup(8,[2,3,5]))
    print("0,[2,3,5] False",bestSum_bottomup(0,[2,3,5]))
    print("300,[7,14] False",bestSum_bottomup(300,[7,14]))
    print("100,[1,2,5,25] True",bestSum_bottomup(100,[1,2,25]))
    
# D:\>python dp_bestSum.py
# 7,[4,5,3,7] True [7]
# 7,[4,5] False None
# 7,[2,3] True [3, 2, 2]
# 7,[4,2] False None
# 8,[2,3,5] True [5, 3]
# 0,[2,3,5] False []
# 300,[7,14] False None
# ******************
# Bottom Up Approach
# ******************
# 7,[4,5,3,7] True [7]
# 7,[4,5] False None
# 7,[2,3] True [2, 2, 3]
# 7,[4,2] False None
# 8,[2,3,5] True [3, 5]
# 0,[2,3,5] False []
# 300,[7,14] False None
# 100,[1,2,5,25] True [25, 25, 25, 25]