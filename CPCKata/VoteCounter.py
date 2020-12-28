import sys
import math

electionDate = 12*30-4
checksum = 0
voteArr = []
def getArray():
  global voteArr
  # If given a string of inputs as command line args, go ahead
  # Input must be innside of single quote
  if len(sys.argv) > 1:
    # Make sure it's a valid array
    if any(elem.upper() not in ['R','B'] for elem in sys.argv[1].split(',')):
      print('Given list of votes contains impropper votes')
      quit()
    voteArr = sys.argv[1].split(',')
  # otherwise, let the user input the votes
  else:
    while True:
      # let the user input a value
      print("Enter Vote ('Q' to terminate'): ")
      x = input()
      if len(x) == 1 and str(x.upper()) in ['R','B']:
        voteArr.append(x.upper())
      elif x.upper() == 'Q':
        break
      else:
        print('Sorry, McDonaldland, being a true dictatorship, you may not have write in votes.')

def calculateChecksum():
  accum = 0
  global checksum
  for vote in voteArr:
    if vote.upper() == 'R':
      accum += 82
    else:
      accum += 66
    
  checksum = math.modf(accum/electionDate)[0]
      


getArray()
calculateChecksum()
print(voteArr)