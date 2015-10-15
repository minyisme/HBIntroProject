#project for intro to python HB class
#will play a virtual baseball game

'''importing'''

#all imports
import random

'''end importing'''



'''scoreboard'''

#list of hits to fill in the visual scoreboard
#range 0 to 19 where 18 and 19 are total hits for each team
hits_by_team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
total_hits_by_team = [0, 0]

#function that draws a scoreboard for the game
def draw_scoreboard(hits_by_team, total_hits_by_team):
	print "Inning   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Total |"
	print "-----------"
	print "Player   | %i | %i | %i | %i | %i | %i | %i | %i | %i |   %i   |" %(hits_by_team[0], hits_by_team[2], hits_by_team[4], hits_by_team[6], hits_by_team[8], hits_by_team[10], hits_by_team[12], hits_by_team[14], hits_by_team[16], total_hits_by_team[0])
	print "-----------"
	print "Computer | %i | %i | %i | %i | %i | %i | %i | %i | %i |   %i   |" %(hits_by_team[1], hits_by_team[3], hits_by_team[5], hits_by_team[7], hits_by_team[9], hits_by_team[11], hits_by_team[13], hits_by_team[15], hits_by_team[17], total_hits_by_team[1])

#draw_scoreboard(hits_by_team, total_hits_by_team)

'''end scoreboard'''



'''pitching'''

#defining strike zone and ball zone
#each pitch can land in one of these 9 strike areas and 4 ball areas
strike_zone = ('in_up','in_mid','in_low','mid_up','mid_mid','mid_low','out_up','out_mid','out_low')
ball_zone = ('in','out','high','low')
locations = strike_zone + ball_zone

#separated locations for pitches that tend to land in corners/sides
low_locations = ('in_low','mid_low','out_low','in','out','low')
out_locations = ('mid_up','mid_mid','mid_low','out_up','out_mid','out_low','out','high','low')
low_in_locations = ('in_mid','in_low','mid_mid','mid_low','in','low')
low_out_locations = ('mid_mid','mid_low','out_mid','out_low','out','low')

#each pitch has different places it can be at
pitches = ('4s_fast','2s_fast','cutter','slider','curve','slurve','change','split','knuckle')


#funtion that gives a location for each time a pitch happens
#where pitches can be:
	#4s_fast: all 13 locations
		#'in_up','in_mid','in_low','mid_up','mid_mid','mid_low','out_up','out_mid','out_low','in','out','high','low'
	#2s_fast: all low and in and mid locations
		#'in_mid','in_low','mid_mid','mid_low','in','low'
	#cutter: all out and mid locations
		#'mid_up','mid_mid','mid_low','out_up','out_mid','out_low','out','high','low'
	#slider: all low and out and mid locations
		#'mid_mid','mid_low','out_mid','out_low','out','low'
	#curve: all low locations
		#'in_low','mid_low','out_low','in','out','low'
	#slurve: all low and out and mid locations
		#'mid_mid','mid_low','out_mid','out_low','out','low'
	#change: all 13 locations
		#'in_up','in_mid','in_low','mid_up','mid_mid','mid_low','out_up','out_mid','out_low','in','out','high','low'
	#split: all low locations
		#'in_low','mid_low','out_low','in','out','low'
	#knuckle: all 13 locations
		#'in_up','in_mid','in_low','mid_up','mid_mid','mid_low','out_up','out_mid','out_low','in','out','high','low'
def pitch_location(pitch):
	if pitch == '4s_fast' or pitch == 'knuckle' or pitch == 'change':
		location = random.choice(locations)
	elif pitch == 'curve' or pitch == 'split':
		location = random.choice(low_locations)
	elif pitch == 'slider' or pitch == 'slurve':
		location = random.choice(low_out_locations)
	elif pitch == '2s_fast':
		location = random.choice(low_in_locations)
	elif pitch == 'cutter':
		location = random.choice(out_locations)
	return location

#computer generates random pitch
def pitch_by_comp():
	pitch_result = pitch_location(random.choice(pitches))
	return pitch_result

#player is asked to supply a pitch
#while loop to reask for input when there is a typo
def pitch_by_player():
	pitch_choice = raw_input("What pitch do you want to pitch? (Choose from: '4s_fast','2s_fast','cutter','slider','curve','slurve','change','split', or 'knuckle')")
	while pitch_choice not in pitches:
		pitch_choice = raw_input("What pitch do you want to pitch? (Choose from: '4s_fast','2s_fast','cutter','slider','curve','slurve','change','split', or 'knuckle')")
	pitch_result = pitch_location(pitch_choice)
	return pitch_result

'''end pitching'''



'''hitting'''

#to hit or not to hit
swing_choice = ('Y','N')

#possible results that occur if pitch is not swung at
#think about adding hit_by_pitch, passed_ball, wild_pitch if finished with other code
no_swing_results = ('ball','strike')

#funtion that gives result of a player not swinging
#needs to be run when a player chooses to not swing at a pitch
#can be unincorporated once the logic of the functions are figured out
'''def no_swing():
	return random.choice(no_swing_results)'''

#function to call during inning when player is pitching
def hit_by_comp():
	hit_choice = random.choice(swing_choice)
	pitch_result = pitch_by_player()
	if hit_choice == 'Y':
		hit_result = random.choice(locations)
		if hit_result == pitch_result:
			swing_result = 'hit'
		else:
			swing_result = 'strike'
	elif hit_choice == 'N':
		if pitch_result in strike_zone:
			swing_result = 'strike'
		elif pitch_result in ball_zone:
			swing_result = 'ball'
	return swing_result

#function to call during inning when player is hitting
#can call on no_swing funtion in the 10th line instead of self incorporated if needed
#while loop put in to reask for input when there's a typo
def hit_by_player():
	hit_choice = raw_input("Would you like to hit this pitch? (Respond 'Y' or 'N'.)")
	while hit_choice not in swing_choice:
		hit_choice = raw_input("Would you like to hit this pitch? (Respond 'Y' or 'N'.)")
	pitch_result = pitch_by_comp()
	if hit_choice == 'Y':
		hit_result = raw_input("Which quadrant would you like to swing at? (Respond 1 of 9 locations in format, eg 'high_in', 'mid_mid', 'low_out'.)")
		while hit_result not in locations:
			hit_result = raw_input("Which quadrant would you like to swing at? (Respond 1 of 9 locations in format, eg 'high_in', 'mid_mid', 'low_out'.)")
		if hit_result == pitch_result:
			swing_result = 'hit'
		else:
			swing_result = 'strike'
	elif hit_choice == 'N':
		if pitch_result in strike_zone:
			swing_result = 'strike'
		elif pitch_result in ball_zone:
			swing_result = 'ball'
	return swing_result

'''end hitting'''



'''playing'''

#function to play top half an inning
def play_comp_pitch():
	print "Pitcher has pitched."
	print "It's your turn to hit"
	swing_result = hit_by_player()
	print "The result was a %s." %(swing_result)
	return swing_result

#function to play bottom half an inning
def play_player_pitch():
	print "It's your turn to pitch."
	swing_result = hit_by_comp()
	print "The result was a %s." %(swing_result)
	return swing_result

'''end playing'''



'''outs'''

#outs when computer is pitching
#a walk = a hit
def outs_comp_pitch():
	strikes = 0
	balls = 0
	for number in range (0,8):
		playing_result = play_comp_pitch()
		if playing_result == 'strike':
			strikes +=1
			if strikes == 3:
				print "Player struck out."
				play_result = 'out'
				break
		elif playing_result == 'ball':
			balls += 1
			if balls == 4:
				print "Player walked."
				play_result = 'hit'
				break
		elif playing_result == 'hit':
			print "Player got a hit."
			play_result = 'hit'
			break
		print "Strikes: %i. Balls: %i." %(strikes, balls)
	return play_result


#outs when player is pitching
def outs_player_pitch():
	strikes = 0
	balls = 0
	for number in range (0,8):
		playing_result = play_player_pitch()
		if playing_result == 'strike':
			strikes +=1
			if strikes == 3:
				print "Player struck out."
				play_result = 'out'
				break
		elif playing_result == 'ball':
			balls += 1
			if balls == 4:
				print "Player walked."
				play_result = 'hit'
				break
		elif playing_result == 'hit':
			print "Player got a hit."
			play_result = 'hit'
			break
		print "Strikes: %i. Balls: %i." %(strikes, balls)
	return play_result

'''end outs'''



'''half inning'''

#funtions that count the outs and the hits
#outs will help iterate through the innings
#hits will be used to add to the scoreboard

def inning_comp_pitch():
	outs = 0
	hits = 0
	while outs < 3:
		play_result = outs_comp_pitch()
		if play_result == 'hit':
			hits += 1
		if play_result == 'out':
			outs += 1
		print "Outs: %i." %(outs)
		inning_results = [hits, outs]
	return inning_results

def inning_player_pitch():
	outs = 0
	hits = 0
	while outs < 3:
		play_result = outs_player_pitch()
		if play_result == 'hit':
			hits += 1
		if play_result == 'out':
			outs += 1
		print "Outs: %i." %(outs)
		inning_results = [hits, outs]
	return inning_results

'''end half inning'''


'''innings'''

#innings logic
#switching between innings
#top of innings are odd numbers, bottom of innings are even numbers
#game ends at 18 innings
def baseball_game():
	inning = 1
	outs = 0
	hits_by_team_counter = 0
	while inning < 19:
		if inning % 2 == 1:
			print "It's the top of inning %i." %((inning + 1) / 2)
			inning_result = inning_comp_pitch()
			if inning_result[0] >= 1:
				hits_by_team[hits_by_team_counter] += inning_result[0]
				total_hits_by_team[0] = (hits_by_team[0]+hits_by_team[2]+hits_by_team[4]+hits_by_team[6]+hits_by_team[8]+hits_by_team[10]+hits_by_team[12]+hits_by_team[14]+hits_by_team[16])
			if inning_result[1] == 3:
				draw_scoreboard(hits_by_team, total_hits_by_team)
				inning += 1
				hits_by_team_counter += 1
		elif inning % 2 == 0:
			print "It's the bottom of inning %i." %(inning / 2)
			inning_result = inning_player_pitch()
			if inning_result[0] >= 1:
				hits_by_team[hits_by_team_counter] += inning_result[0]
				total_hits_by_team[1] = (hits_by_team[1]+hits_by_team[3]+hits_by_team[5]+hits_by_team[7]+hits_by_team[9]+hits_by_team[11]+hits_by_team[13]+hits_by_team[15]+hits_by_team[17])
			if inning_result[1] == 3:
				draw_scoreboard(hits_by_team, total_hits_by_team)
				inning += 1
				hits_by_team_counter += 1
	if total_hits_by_team[0] > total_hits_by_team[1]:
		print "You won!"
	elif total_hits_by_team[1] > total_hits_by_team[0]:
		print "Computer won. :("
	return "Game over!"
#need to add hits logic and who wins

'''end innings'''

print baseball_game()