#This program uses functions, but a while loop is still used to call the functions/run the game itself
#Player 1 is the red circle, while Player 2 is the green circle
#Condition 1: If player rolls both 1's, they lose a turn
#Condition 2: If player rolls 2 of the same number (with the exception of 1), they gain an extra turn 

import pygame, random

#drawing a 7x8 grid 
width = 7
height = 8
	
square_size = 80
	
drawing_window = pygame.display.set_mode((width*square_size, height*square_size))

drawing_window.fill((127, 127, 127))

white = (255, 255, 255)
black = (0,0,0)

colour = white

#draws the checkerboard
for i in range(0, width):
	for j in range(0, height):
		pygame.draw.rect(drawing_window, colour, (i * square_size, j * square_size, square_size, square_size))
		pygame.display.update()	
		if colour == white:
			colour = black
		else:
			colour = white
	if colour == white:
		colour = black
	else:
		colour = white

#variables to store player locations
player_1_x = square_size/2
player_1_y = square_size/2-10
player_2_x = square_size/2
player_2_y = square_size/2+10

#draws the starting locations of both players at the top left square (square 1)
pygame.draw.circle(drawing_window, (255,0,0), (player_1_x,player_1_y),10)
pygame.draw.circle(drawing_window, (0,255,0), (player_2_x,player_2_y),10)
pygame.display.update()
pygame.time.delay(3000)

#function to redraw the grid  
def draw_grid():

	white = (255, 255, 255)
	black = (0,0,0)

	colour = white

	for i in range(0, width):
		for j in range(0, height):
			pygame.draw.rect(drawing_window, colour, (i * square_size, j * square_size, square_size, square_size))
			pygame.display.update()	
			if colour == white:
				colour = black
			else:
				colour = white
		if colour == white:
			colour = black
		else:
			colour = white

#function to roll pair of dice of a random number from 1 to 3 
def roll_dice():
	global die_1
	global die_2
	die_1 = random.randint(1,6)
	die_2 = random.randint(1,6)

#function for player 1
def player_1():
	global player_1_x
	global player_1_y
	roll_dice()
	print("Player 1 rolled " + str(die_1) + " and " + str(die_2))
	print("---------------------")
	#call the grid drawing function so it erases previous locations of the players
	draw_grid()
	#if player rolls two 1's, they lose their turn 
	if die_1 == 1 and die_2 == 1:
		print("Player 1 lost their turn.")
		pygame.time.delay(1000)
		print("---------------------")
		player_2()
	else:
		player_1_x += (die_1+die_2)*80
		#moves player to the next row when they surpass their current row 
		while player_1_x > 560:
			player_1_x -= 560
			player_1_y += square_size
		#if player goes over the last tile, set position to be on the last tile
		while player_1_y > 640:
			player_1_x = 520
			player_1_y = 600
		#draws both players' new locations
		pygame.draw.circle(drawing_window, (255,0,0), (player_1_x, player_1_y), 10)
		pygame.draw.circle(drawing_window, (0,255,0), (player_2_x, player_2_y), 10)	
		pygame.display.update()
		pygame.time.delay(1000)
		#gives player an extra turn if they roll the same number (not 1's)
		if die_1 == die_2:
			print("Player 1 extra turn")
			pygame.time.delay(1000)
			print("---------------------")
			player_1()
			
#function for player 2
def player_2():
	global player_2_x
	global player_2_y
	roll_dice()
	print("Player 2 rolled " + str(die_1) + " and " + str(die_2))
	print("---------------------")
	draw_grid()
	#if player rolls two 1's, they lose their turn 
	if die_1 == 1 and die_2 == 1:
		print ("Player 2 lost their turn.")
		pygame.time.delay(1000)
		print("---------------------")
		player_1()
	else:
		player_2_x += (die_1+die_2)*80
		#moves player to the next row when they surpass their current row 
		while player_2_x > 560:
			player_2_x -= 560
			player_2_y += square_size
		while player_2_y > 640:
			player_2_x = 520
			player_2_y = 600
	#draws both players' new locations
	pygame.draw.circle(drawing_window, (0,255,0), (player_2_x, player_2_y), 10)	
	pygame.draw.circle(drawing_window, (255,0,0), (player_1_x, player_1_y), 10)
	pygame.display.update()	
	pygame.time.delay(5000)
	#gives player an extra turn if they roll the same number (not 1's)
	if die_1 == die_2:
		print("Player 2 extra turn")
		pygame.time.delay(1000)
		print("---------------------")
		player_2()

#while loop to control the game, and terminate when it ends
while True:
	player_1()
	
	#if player 1 lands on ending square, they win 
	if player_1_x > 480 and player_1_y > 560:
		print("Player 1 wins")
		pygame.time.delay(5000)
		break
	#if player 1 moves past the ending square, declare them as winner
	elif player_1_y > 640:
		print("Player 1 wins")
		pygame.time.delay(5000)
		break
	elif player_2_x > 480 and player_2_y > 560:
		print("Player 2 wins")
		pygame.time.delay(5000)
		break
	elif player_2_y > 640:
		print("Player 2 wins")
		pygame.time.delay(5000)
		break
	#if no winner is declared yet 
	else:
		player_2()
		if player_1_x > 480 and player_1_y > 560:
			print("Player 1 wins")
			pygame.time.delay(5000)
			break 
		elif player_1_y > 640:
			print("Player 1 wins")
			pygame.time.delay(5000)
			break
		elif player_2_x > 480 and player_2_y > 560:
			print("Player 2 wins")
			pygame.time.delay(5000)
			break
		elif player_2_y > 640:
			print("Player 2 wins")
			pygame.time.delay(5000)
			break

		
	