import random

def game():
    print("You are playing the game...")
    score = random.randint(1,100)
    with open("HighScore.txt") as f:
        High_Score = f.read() 
        if (High_Score != ""): 
            High_Score = int(score)
        else:
            High_Score = 0 #If empty
    print(f"Your Score is: {score}") 
    if(score>High_Score):
        with open("High_Score", "w") as f:
            f.write(str(score))
    return score
game()                   