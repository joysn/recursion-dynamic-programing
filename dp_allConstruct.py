# allConstruct
# Given a target string, list all ways can we construct the target string from the given set of wordbank

import copy

global debug
debug = False
def allConstruct(targetString, wordbank):
    print("Calling with ",targetString) if debug else None
    
    if targetString in memo.keys():
        return memo[targetString]
        
    if targetString == "":
        return [[]]
        
    all_ways = []
    for word in wordbank:
        idx = targetString.find(word)
        if idx == 0:
            newTargetString = targetString[len(word):]
            ways = allConstruct(newTargetString,wordbank)
            print("Returning for:",newTargetString,"Got:",ways) if debug else None
            print("Ways:",ways) if debug else None
            if ways is not None:
                for w in ways:
                    w.insert(0,word)
                print("Ways:",ways) if debug else None
            
                for w in ways:
                    all_ways.append(w)
            
    if len(all_ways) > 0:
        memo[targetString] = copy.deepcopy(all_ways)
        return all_ways
        
    memo[targetString] = None
    return None


def allConstruct_bottomup(targetString, wordbank):

    if targetString == "":
        return [[]]

    l = len(targetString)
    tab = [[] for i in range(l+1)]
    tab[0] = [[]]

    for i in range(l+1):
        newTargetString = targetString[i:]
        paths = []
        if len(tab[i]) > 0:
            for word in wordbank:
                idx = newTargetString.find(word)
                if (i+len(word) <= l) and idx == 0:
                    temp_list = copy.deepcopy(tab[i])
                    for path in temp_list:
                        path.append(word)
                    for p in temp_list:
                        tab[i+len(word)].append(p)
                    

    return tab[l]


# m = length of targetString
# n = lenth of wordbank
# time = O(n^m)  
# space = O(m*m) 

# Bottom Up (Bad way!!!!)
# Time = O(m*n*m*m) 
# m = for every character for target string
# n = for every word in wordbank
# m = max size of the word for find
# m = max number of paths

# Space = O(m*m*m)
# m = size of table
# m = max number of paths
# m = max size of string
    
if __name__ == "__main__":
    memo = dict()
    targetString = "def"
    strArray = ["d","ef","def"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()
    
    memo = dict()
    targetString = "abcdef"
    strArray = ["ab","abc","cd","def","abcd","ef","c"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()
            
    memo = dict()
    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()
    
    memo = dict()
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()
    
    memo = dict()
    targetString= "purple"
    strArray = ["purp","p","ur","le","purpl"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()
    
    memo = dict()
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print("Memo: ",targetString,strArray,allConstruct(targetString,strArray))
    targetString = "eeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee"]
    print("BottomUp: ",targetString,strArray,allConstruct_bottomup(targetString,strArray))
    print()




# % python allConstruct.py
# Memo:  def ['d', 'ef', 'def'] [['d', 'ef'], ['def']]
# BottomUp:  def ['d', 'ef', 'def'] [['def'], ['d', 'ef']]

# Memo:  abcdef ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'] [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
# BottomUp:  abcdef ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'] [['abc', 'def'], ['ab', 'c', 'def'], ['abcd', 'ef'], ['ab', 'cd', 'ef']]

# Memo:  skateboard ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'] None
# BottomUp:  skateboard ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'] []

# Memo:  enterapotentpot ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'] [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
# BottomUp:  enterapotentpot ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'] [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]

# Memo:  purple ['purp', 'p', 'ur', 'le', 'purpl'] [['purp', 'le'], ['p', 'ur', 'p', 'le']]
# BottomUp:  purple ['purp', 'p', 'ur', 'le', 'purpl'] [['purp', 'le'], ['p', 'ur', 'p', 'le']]

# Memo:  eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'] None
# BottomUp:  eeeeeeeef ['e', 'ee', 'eee', 'eeee', 'eeeee'] []