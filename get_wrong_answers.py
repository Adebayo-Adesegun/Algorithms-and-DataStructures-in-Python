


def getWrongAnswers(N: int, C: str) -> str:
      # Write your code here
  
  answer = ''
  
  for i in range(N):
    if C[i] == 'A':
        answer = answer + 'B'
    else:
        answer = answer + 'A'
    
  
  return answer

getWrongAnswers(3, 'ABA')