"""def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
print(palindrome('noon'))"""

def first(word): 
    return word[0] 
 
def last(word): 
    return word[-1] 
 
def middle(word): 
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0:
        return True
    elif len(word) == 1:
        return True
    elif len(word) > 1 and first(word) == last(word) and is_palindrome(middle(word)) == True:
        return True
print(is_palindrome("noon"))






