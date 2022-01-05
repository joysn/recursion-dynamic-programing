# countConstruct
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

# m = length of targetString
# n = lenth of wordbank
# time = O(n^m)  
# space = O(m*m) 
    
if __name__ == "__main__":
    memo = dict()
    targetString = "def"
    strArray = ["d","ef","def"]
    print(targetString,strArray,allConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "abcdef"
    strArray = ["ab","abc","cd","def","abcd","ef","c"]
    print(targetString,strArray,allConstruct(targetString,strArray))
            
    memo = dict()
    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print(targetString,strArray,allConstruct(targetString,strArray))
    
    memo = dict()
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print(targetString,strArray,allConstruct(targetString,strArray))
    
    memo = dict()
    targetString= "purple"
    strArray = ["purp","p","ur","le","purpl"]
    print(targetString,strArray,allConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print(targetString,strArray,allConstruct(targetString,strArray))