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

# m is the targetSum
# n is the number of  numbers
# Brute Force
# time O(n^m*m)
# Spave O(m*m)

# Memoization
# time O(n*m*m)
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
    
    
# D:\>python dp_bestSum.py
# 7,[4,5,3,7] True [7]
# 7,[4,5] False None
# 7,[2,3] True [3, 2, 2]
# 7,[4,2] False None
# 8,[2,3,5] True [5, 3]
# 0,[2,3,5] False []
# 300,[7,14] False None