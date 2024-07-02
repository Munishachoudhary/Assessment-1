def guess_the_number():
    print("Think number between 1 and 100, and I will try to guess")
    input("Press Enter when you're ready...")
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        print(f"Is your number {guess}?")
        feedback = input("Enter 'higher', 'lower', or 'correct': ").lower()

        if feedback == 'correct':
            print(f"I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'higher':
            low = guess + 1
        elif feedback == 'lower':
            high = guess - 1
        else:
            print("Invalid input")

    if low > high:
        print("Something went wrong")

guess_the_number()