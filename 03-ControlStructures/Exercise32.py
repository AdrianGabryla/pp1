science = input("Are you interested in computer science? (Y/N): ") 
games = input("Do you like playing computer games? (Y/N): ")
ig = input("Do you have an Instagram account? (Y/N): ")
if science == "Y":
    science = "Yes"
else:
    science = "No"
if games == "Y":
    games = "Yes"
else:
    games = "No"
if ig == "Y":
    ig = "Yes"
else:
    ig = "No"
print(f"Interested in computer science: {science}")
print(f"Playing computer games: {games}")
print(f"Has an Instagram account: {ig}")