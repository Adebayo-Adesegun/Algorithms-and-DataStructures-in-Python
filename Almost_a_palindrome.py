

# Description
# Given a string, determine if it is almost a palindrome. A string is almost a palindrome if it becomes a palidrome
# by removing one letter. Consider only alphanumeric characters and ignore case sensitivity.


def isPalindrome_method(text):
  text = ''.join(filter(str.isalnum, text)) 
  text = text.lower()
  
  left, right = 0, len(text) -1
  
  while left < right:
    if text[left] != text[right]:
      return False
    
    right -=1
    left +=1
    
  return True

def is_almost_a_palindrome(text):
  
  # Edit test to remove special characters and spaces from the text
  text = ''.join(filter(str.isalnum, text)) 
  text = text.lower()
  
  left ,right = 0, len(text) -1
  
  is_palindrome = False
  min_index_to_remove = 0
  max_index_to_remove = 0
  
  while left < right:
    
    if text[left] != text[right]:
      is_palindrome = False
      min_index_to_remove = min(left, right)
      max_index_to_remove = max(left, right)
      break

    left += 1
    right -= 1
    
  if is_palindrome is False:
  # Left  side first
    min_index_side_check = text[:min_index_to_remove] +  text[min_index_to_remove+1:]
    if isPalindrome_method(min_index_side_check):
      return True
    
    max_index_side_check = text[:max_index_to_remove] +  text[max_index_to_remove+1:]
    if isPalindrome_method(max_index_side_check):
      return True
    
    return False
    

  else:
    return True
      
    
    
  
  return text



# Edge cases

print(is_almost_a_palindrome("raceacar")) # True
print(is_almost_a_palindrome("abccdba")) # True
print(is_almost_a_palindrome("abcdefdba")) # False
print(is_almost_a_palindrome("")) # True
print(is_almost_a_palindrome("a")) # True
print(is_almost_a_palindrome("ab")) # True