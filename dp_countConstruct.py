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
    print(targetString,strArray,countConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "skateboard"
    strArray = ["bo","rd","ate","t","ska","sk","boar"]
    print(targetString,strArray,countConstruct(targetString,strArray))
    
    memo = dict()
    targetString= "enterapotentpot"
    strArray = ["a","p","ent","enter","ot","o","t"]
    print(targetString,strArray,countConstruct(targetString,strArray))
    
    memo = dict()
    targetString= "purple"
    strArray = ["purp","p","ur","le","purpl"]
    print(targetString,strArray,countConstruct(targetString,strArray))
    
    memo = dict()
    targetString = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
    strArray = ["e","ee","eee","eeee","eeeee","eeeeee"]
    print(targetString,strArray,countConstruct(targetString,strArray))
            