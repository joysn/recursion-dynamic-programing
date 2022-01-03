# Can construct
# Given a target string, can we construct the target string from the given set of wordbank

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
            
# m = targetString length
# n = number of strings in strArray
# Brute Force
# time = O(n^m*m)
# Space = O(m*m)
# Memoization
# Time = O(n*m*m)
# Space = O(m*m+m)

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
    