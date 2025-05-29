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
	guess = input('guess: ').upper().split(" ")



	if len(guess) != CODE_LENGTH: 
		print(f'you must gues{ CODE_LENGTH} colors.')
		continue 
	for color in guess: 
		if color not in COLORS: 
			print(f' Invalid color : { color }. Try again ')
			break im
