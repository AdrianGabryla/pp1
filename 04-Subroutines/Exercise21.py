import mymath
import mykeyboard
x = mymath.generate_number()
y = mykeyboard.read_number()
print(f"Computer number: {x}")
if x == y:
    print("You won the game!!")
