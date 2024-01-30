class Bowling():

    def __init__(self,scores):
        self.scores = scores

# This method checks the consecutive 10s in the game
    def isTurkey(self):
        score_in_a_row = 0

        for score in self.scores:
            if score == 10:
                score_in_a_row += 1
                if score_in_a_row == 3:
                    return True
            else:
                score_in_a_row = 0
        return False


# This methods checks 3 occurences of 7 in the game
    def freeGame(self):
        if self.scores.count(7) == 3:
            return True
        return False


#This methods used to find the lowest score in the frame
    def getLowestScore(self):
        lowest_score = min(self.scores)
        lowest_index = self.scores.index(lowest_score)
        return lowest_index


# This gets the median of the total score
    def getmedian(self):
        count = sorted(self.scores)
        n = len(count)
        if n % 2 == 0:
            return (count[(n // 2)] + count[(n // 2) ] -1) / 2
        else:
            return count[n // 2]

# user input for manual entry or data in the game
choice = int(input("Please select 1 for manual entry of scores else press 0: "))
Scores = []
if choice == 1:
    No_of_attempts = int(input("How many number of frames in the game? "))
    for i in range(No_of_attempts):
        Scores.append(int(input("Enter the score for choice : ")))
elif choice == 0:
    Scores = [7,9,6,10,10,10,7,5,8,7]

# creates the instrance of the bowling class
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

print("Lowest Score:", Scores[index],"which occured in Frame", index + 1)

print("The median is", MyBowling.getmedian())