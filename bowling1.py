# Bowling class 
class Bowling:

  def _init_(self, scores):
    self.scores = scores

  # Check if turkey (3 consecutive strikes)
  def isTurkey(self):
    consecutive_10s = 0 
    for score in self.scores:
        if score == 10:
            consecutive_10s += 1
            if consecutive_10s == 3:
             return True
        else:
          consecutive_10s = 0
    return False

  # Check if 3 scores of 7 for free game  
  def freeGame(self):
    if self.scores.count(7) == 3:
      return True
    return False
  
  # Find lowest score and frame  
  def getLowestScore(self):
    lowest_score = min(self.scores)
    lowest_frame = self.scores.index(lowest_score) + 1
    return lowest_frame - 1

  # Calculate median score
  def getMedian(self):
    sorted_scores = sorted(self.scores)
    n = len(sorted_scores)
    if n % 2 == 1:
      return sorted_scores[n // 2]
    else:
      mid1 = n // 2
      mid2 = mid1 - 1 
      return (sorted_scores[mid1] + sorted_scores[mid2]) / 2

# Main 

# Get scores from user input
Scores = []
for i in range(10):
  score = int(input(f"Enter score for frame {i+1}: "))
  Scores.append(score)

# Create Bowling object instance  
MyBowling = Bowling(Scores)

# Check for turkey
if MyBowling.isTurkey():
  print("Congrats! You got a Turkey")
else:
  print("No Turkey")

# Check for free game
if MyBowling.freeGame():
  print("Free Game")  
else:
  print("No Free Game")

# Get lowest score
index = MyBowling.getLowestScore()
print("Lowest Score:", Scores[index], "which occurred in Frame", index + 1)

# Get median score
print("The median score is:", MyBowling.getMedian())