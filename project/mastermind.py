import random

COLORS =  [ 'A', 'B', 'C', 'D']
TRIES =  10 
CODE_LENGTH = 4


def generate_code():
	code = []			
	for _  in range(CODE_LENGTH):
		color = random.choice(COLORS)
		code.append(color)
	return code 
def guess_code():
	while True:
		guess = input('guess: ').upper().split(" ")

		if len(guess) != CODE_LENGTH:
			print(f'you must guess {CODE_LENGTH} colors.')
			continue
		
		for color in guess:
			if color not in COLORS:
				print(f'Invalid color: {color}. Try again.')
				break
		else: # This else block executes if the for loop completes without a break
			return guess
