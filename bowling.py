class Bowling:
    def __init__(self, scores):
        self.scores = scores

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

    def freeGame(self):
        if self.scores.count(7) == 3:
            return True
        return False

    def getLowestScore(self):
        lowest_score = min(self.scores)
        lowest_frame = self.scores.index(lowest_score) + 1
        return lowest_frame - 1

    def getMedian(self):
        sorted_scores = sorted(self.scores)
        n = len(sorted_scores)
        if n % 2 == 1:
            return sorted_scores[n // 2]
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (sorted_scores[mid1] + sorted_scores[mid2]) / 2


# Prompting the user to enter scores
Scores = []
for i in range(10):
    score = int(input(f"Enter score for frame {i + 1}: "))
    Scores.append(score)

# Creating an instance of the class Bowling
MyBowling = Bowling(Scores)

if MyBowling.isTurkey():
    print("Congrats! You got a Turkey")
else:
    print("No Turkey")

if MyBowling.freeGame():
    print("Free Game")
else:
    print("No Free Game")

index = MyBowling.getLowestScore()
print("Lowest Score:", Scores[index], "which occurred in Frame", index + 1)
print("The median score is:", MyBowling.getMedian())
