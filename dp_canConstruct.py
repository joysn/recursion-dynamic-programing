# Can construct
# Given a target string, can we construct the target string from the given set of wordbank

import copy
global debug
debug = False

def canConstruct(targetString, strArray):

    if targetString in memo.keys():
        return memo[targetString]
    if targetString == "":
        return True
        
    for substr in strArray:
        idx = targetString.find(substr)
        if idx == 0:
            newTargetString = targetString[len(substr):]
            print(targetString,"-",substr,"=",newTargetString) if debug else None
            if canConstruct(newTargetString,strArray):
                memo[targetString] = True
                return True
                
    memo[targetString] = False
    return False


def canConstruct_bottomup(targetString,wordbank):

    l = len(targetString)

    tab = [False for i in range(l+1)]
    tab[0] = True

    for i in range(l+1):
        newTargetString = targetString[i:]
        if tab[i] is not False:
            for word in wordbank:
                idx = newTargetString.find(word)
                if (i+len(word) <= l) and (idx == 0):
                    # tab[i+len(word)] = copy.deepcopy(tab[i])
                    # tab[i+len(word)].append(word)
                    tab[i+len(word)] = True

                    if i+len(word) == l:
                        # print(tab)
                        return tab[l]

    # print(tab)
    return tab[l]

# m = targetString length
# n = number of strings in strArray
# Brute Force
# time = O(n^m*m)
# Space = O(m*m)
# Memoization
# Time = O(n*m*m)
# Space = O(m*m+m)

# Tabulation
# Time = O(m*n*m) m - for size of table, n - for each word to be considered, m - max length of each word (to calculate the idx)
# Space = O(m) - size of table, 

if __name__ == "__main__":
    memo = dict()
    targetString = "abcdef"
    strArray = ["ab","abc","cd","def","abcd"]
    print(targetString,strArray,canConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print(targetString,strArray,canConstruct(targetString,strArray))
    
    memo = dict()
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print(targetString,strArray,canConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print(targetString,strArray,canConstruct(targetString,strArray))

    print("******************")
    print("Bottom Up Approach")
    print("******************")
    targetString = "abcdef"
    strArray = ["ab","abc","cd","def","abcd"]
    print(targetString,strArray,canConstruct_bottomup(targetString,strArray))


    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print(targetString,strArray,canConstruct_bottomup(targetString,strArray))
    
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print(targetString,strArray,canConstruct_bottomup(targetString,strArray))
    
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print(targetString,strArray,canConstruct_bottomup(targetString,strArray))