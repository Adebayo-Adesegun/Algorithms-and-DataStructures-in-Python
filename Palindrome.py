
def isPalindrome_method2(text):
  text = ''.join(filter(str.isalnum, text)) 
  text = text.lower()
  
  left, right = 0, len(text) -1
  
  while left < right:
    if text[left] != text[right]:
      return False
    
    right -=1
    left +=1
    
  return True
  
  

def isPalindrome(text):
  
  # First Step is to remove special characters from the text
  # The str.isalnum() method returns True if the characters are alphanumeric characters, meaning no special characters in the string
  text = ''.join(filter(str.isalnum, text)) 
  text = text.lower()
  
  
  # first technique : Reverse string and set pointer to beginning of both strings 
  reversed_text = text[::-1]
  
  for x in range(len(text)):
    if text[x] != reversed_text[x]:
      return False
    
  return True
  
  
    
print(isPalindrome("aabaa")) 
print(isPalindrome("aabbaa")) 
print(isPalindrome("abc")) 
print(isPalindrome("a")) # Edge case for single character
print(isPalindrome("")) # Edge case for empty string
print(isPalindrome("A man, a plan, a canal : Panama"))







  