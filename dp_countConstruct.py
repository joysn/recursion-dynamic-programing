# countConstruct
# Given a target string, how many ways can we construct the target string from the given set of wordbank


def countConstruct(targetString, wordbank):

    if targetString in memo.keys():
        return memo[targetString]
    if targetString == "":
        return 1
        
    count = 0
    for substring in wordbank:
        idx = targetString.find(substring)
        if idx == 0:
            newtargetString = targetString[len(substring):]
            count += countConstruct(newtargetString,wordbank)
            
    memo[targetString] = count
    return count
    

def countConstruct_bottomup(targetString,wordbank):
    
    l = len(targetString)
    tab = [0 for i in range(l+1)]
    tab[0] = 1

    for i in range(l+1):
        newtargetString = targetString[i:]
        if tab[0] > 0:
            for word in wordbank:
                idx = newtargetString.find(word)
                if (i+len(word) <= l) and (idx == 0):
                    tab[i+len(word)]+= tab[i]

    return tab[l]



# m = size of target string
# n = number of wordbank
# Brute Force
# Time = O(n^m * m)
# Space = O(m*m)
# Memoization
# Time = O(n*m*m)
# Space = O(m*m)

if __name__ == "__main__":
    memo = dict()
    targetString = "abcdef"
    strArray = ["ab","abc","cd","def","abcd"]
    print("Memo:",targetString,strArray,countConstruct(targetString,strArray))
    print("BottomUp:",targetString,strArray,countConstruct_bottomup(targetString,strArray))

    memo = dict()
    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print("Memo:",targetString,strArray,countConstruct(targetString,strArray))
    print("BottomUp:",targetString,strArray,countConstruct_bottomup(targetString,strArray))
    
    memo = dict()
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print("Memo:",targetString,strArray,countConstruct(targetString,strArray))
    print("BottomUp:",targetString,strArray,countConstruct_bottomup(targetString,strArray))
    
    memo = dict()
    targetString= "purple"
    strArray = ["purp","p","ur","le","purpl"]
    print("Memo:",targetString,strArray,countConstruct(targetString,strArray))
    print("BottomUp:",targetString,strArray,countConstruct_bottomup(targetString,strArray))
    
    memo = dict()
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print("Memo:",targetString,strArray,countConstruct(targetString,strArray))
    print("BottomUp:",targetString,strArray,countConstruct_bottomup(targetString,strArray))


# % python countConstruct.py
# Memo: abcdef ['ab', 'abc', 'cd', 'def', 'abcd'] 1
# BottomUp: abcdef ['ab', 'abc', 'cd', 'def', 'abcd'] 1
# Memo: skateboard ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'] 0
# BottomUp: skateboard ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'] 0
# Memo: enterapotentpot ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'] 4
# BottomUp: enterapotentpot ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'] 4
# Memo: purple ['purp', 'p', 'ur', 'le', 'purpl'] 2
# BottomUp: purple ['purp', 'p', 'ur', 'le', 'purpl'] 2
# Memo: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'] 0
# BottomUp: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'] 0