import VoteCounter
import math

electionDate = 12*30-4

newReturnArray = []

def calculateVotesToChange():
  # see what votes are in the array cause if B is winning don't change
  mVotes = 0
  bVotes = 0

  for vote in VoteCounter.retArr[0]:
    if str(vote).upper() == 'M':
      mVotes +=1
    else:
      bVotes +=1
  # if Burgler is winning, don't do anything
  if bVotes > mVotes:
    return -1
  # If there are fewer votes than the election date, the set will not repeat and won't have the ability
  # to be manipulated
  if electionDate > VoteCounter.retArr[1]:
    return -2

  # to get to the same number remainder of the next set, we must got up by that amount of days in election
  for x in range(bVotes, VoteCounter.retArr[1]+1, electionDate):
    if VoteCounter.retArr[1] - x < x:
      return x - bVotes


def changeVotes(numbVotes):
  newVoteArr = []

  for vote in VoteCounter.retArr[0]:
    if str(vote).upper() == 'M' and numbVotes > 0:
      newVoteArr.append('B')
      numbVotes -= 1
    else:
      newVoteArr.append(vote)
  
  return newVoteArr

def compileAndCheck(newArray):
  accum = 0
  for vote in newArray:
    if vote.upper() == 'M':
      accum += 82
    else:
      accum += 66
    
  if int(str(math.modf(accum/electionDate)[0])[2:]) != VoteCounter.retArr[2]:
    return -3
  return 1

def sendNewData():
  global newReturnArray

  l = calculateVotesToChange()
  if l == -1:
    print("Ham Burgler is already winning, no need to change")
    return -1
  elif l == -2:
    print("Not enough votes cast to maintain illusion of election integrity")
    return -2
  else:
    newReturnArray.append(changeVotes(l))
    if compileAndCheck(newReturnArray[0]) == -3:
      print("Something went wrong")
      return -3
    else:
      newReturnArray.append(VoteCounter.retArr[1])
      newReturnArray.append(VoteCounter.retArr[2])
    return newReturnArray

print(sendNewData())
  

