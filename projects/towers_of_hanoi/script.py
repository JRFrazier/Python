from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.extend([left_stack, middle_stack, right_stack])
# Set up the Game
num_disks = int(input("\nHow many disks do you want ot play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks):
    left_stack.push(i)

num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

# Get User Input


def get_input():
    choices = [i.get_name()[0] for i in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))

        user_input = input()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for i in stacks:
        i.print_items()

    print("\nWhich stack do you wnat to move from?\n")
    from_stack = get_input()

    print("\nWhich stack do you want to move to?")
    to_stack = get_input()

    if to_stack.peek() == None:
        top_of_val = from_stack.pop()
        to_stack.push(top_of_val)
        num_user_moves += 1
    elif from_stack.peek() == None:
        print("Invalid move\nTry again...")
    elif to_stack.peek() < from_stack.peek():
        top_of_val = from_stack.pop()
        to_stack.push(top_of_val)
        num_user_moves += 1
    else:
        print("Invalid move\nTry again...")

    print(
        "\n\nNumber of Moves {0}/{1} ---------------------------------------".format(num_user_moves, num_optimal_moves))

if num_user_moves <= num_optimal_moves:
    print("You Win!\nGame Over")
else:
    print("Good Job!\nNext time try compleating it in {0} or less moves.".format(
        num_optimal_moves))

    # if from_stack.is_empty():
    #   print("\n\nInvalid Move. Try Again")
