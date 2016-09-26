import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

"""figure out how to put a display function in here eventually"""
class character:
	def __init__ (self, name = None, descriptor = None, type_ = None, focus = None, tier = None, effort = None, xp = None, might_max = None, might_current = None, might_edge = None, speed_max = None, speed_current = None, speed_edge = None, intellect_max = None, intellect_current = None, intellect_edge = None, equipment = None, money = None, advancement = None, notes = None, background = None, skills = None, special_abilities = None):
		self.name = name
		self.descriptor = descriptor
		self.type_ = type_
		self.focus = focus
		self.tier = tier
		self.effort = effort
		self.xp = xp
		self.might_max = might_max
		self.might_current = might_current
		self.might_edge = might_edge
		self.speed_max = speed_max
		self.speed_current = speed_current
		self.speed_edge = speed_edge
		self.intellect_max = intellect_max
		self.intellect_current = intellect_current
		self.intellect_edge = intellect_edge
		self.equipment = equipment
		self.money = money
		self.advancement = advancement
		self.notes = notes
		self.background = background
		self.skills = skills
		self.special_abilities = special_abilities

'''Will hold all the character for "easy" iteration'''
party = []

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def add(left : int, right : int):
	"""Adds two numbers together."""
	await bot.say(left + right)

@bot.command()
async def change(name : str, stat : str, new_value : str):
	found = False
	old_value = ""
	for char in party:
		if (name == char.name):
			if (stat == "name"):
				old_value = char.name
				char.name = new_value
				found = True
			elif (stat == "descriptor"):
				old_value = char.descriptor
				char.descriptor = new_value
				found = True
			elif (stat == "type_"):
				old_value = char.type_
				char.type_ = new_value
				found = True
			elif (stat == "focus"):
				old_value = char.focus
				char.focus = new_value
				found = True
			elif (stat == "tier"):
				old_value = char.tier
				char.tier = new_value
				found = True
			elif (stat == "effort"):
				old_value = char.effort
				char.effort = new_value
				found = True
			elif (stat == "xp"):
				old_value = char.xp
				char.xp = new_value
				found = True
			elif (stat == "might_max"):
				old_value = char.might_max
				char.might_max = new_value
				found = True
			elif (stat == "might_current"):
				old_value = char.might_current
				char.might_current = new_value
				found = True
			elif (stat == "might_edge"):
				old_value = char.might_edge
				char.might_edge = new_value
				found = True
			elif (stat == "speed_max"):
				old_value = char.speed_max
				char.speed_max = new_value
				found = True
			elif (stat == "speed_current"):
				old_value = char.speed_current
				char.speed_current = new_value
				found = True
			elif (stat == "speed_edge"):
				old_value = char.speed_edge
				char.speed_edge = new_value
				found = True
			elif (stat == "intellect_max"):
				old_value = char.intellect_max
				char.intellect_max = new_value
				found = True
			elif (stat == "intellect_current"):
				old_value = char.intellect_current
				char.intellect_current = new_value
				found = True
			elif (stat == "intellect_edge"):
				old_value = char.intellect_edge
				char.intellect_edge = new_value
				found = True
			elif (stat == "equipment"):
				old_value = char.equipment
				char.equipment = new_value
				found = True
			elif (stat == "money"):
				old_value = char.money
				char.money = new_value
				found = True
			elif (stat == "advancement"):
				old_value = char.advancement
				char.advancement = new_value
				found = True
			elif (stat == "notes"):
				old_value = char.notes
				char.notes = new_value
				found = True
			elif (stat == "background"):
				old_value = char.background
				char.background = new_value
				found = True
			elif (stat == "skills"):
				old_value = char.skills
				char.skills = new_value
				found = True
			elif (stat == "special_abilities"):
				old_value = char.special_abilities
				char.special_abilities = new_value
				found = True
	if (found == True):
		await bot.say("```%s's %s value has been changed from %s to %s```" %(name,stat,old_value,new_value))
	else:
		await bot.say("```Either %s was not found in the party or %s stat doesn't match format on character sheet template```" %(name,stat))

@bot.command()
async def roll(dice : str):
	"""Rolls a dice in NdN format."""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		await bot.say('```Format has to be in NdN!```')
		return

	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
	"""Chooses between multiple choices."""
	await bot.say(random.choice(choices))


@bot.command()
async def load(char_name : str):
	"""Load specified character"""
	data = []
	chars_to_load = []
	exists = False
	if (char_name == "all"):
		fo = open("party.txt", "r")
		chars_to_load = [line.rstrip('\n') for line in fo]
		fo.close()
		for char in chars_to_load:
			fo = open(char + ".txt", "r")
			data = [line.rstrip('\n') for line in fo]
			fo.close()
			for i,v in enumerate(data[:]):
				tok = v.find('=')
				data[i] = v[tok+1:]
			for char in party:
				if (data[0] == char.name):
					await bot.say('```%s already exists in the party.\n```' %char)
					exists = True
			if (exists == False):
				temp = character(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22])
				party.append(temp)
				await bot.say('```%s has been added to the party!\n```' %data[0])
	else:
		fo = open(char_name + ".txt", "r")
		data = [line.rstrip('\n') for line in fo]
		fo.close()
		for i,v in enumerate(data[:]):
			tok = v.find('=')
			data[i] = v[tok+1:]
		for char in party:
			if (data[0] == char.name):
				await bot.say('```%s already exists in the party.\n```' %char_name)
				exists = True
		if (exists == False):
			temp = character(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22])
			party.append(temp)
			await bot.say('```%s has been added to the party!\n```' %data[0])

@bot.command()
async def display(char_name : str, stat : str = None):
	"""Displays players stats n stuff"""
	"""Probably super wasteful to concatenate via + or even at all"""
	found = False
	if (char_name == "all"):
		for char in party:
			await bot.say("```Name = " + char.name + "\nDescriptor = " + char.descriptor + "\nType = " + char.type_ + "\nFocus = " + char.focus + "\nTier = " + char.tier + "\nEffort = " + char.effort + "\nXP = " + char.xp + "\nMight Max = " + char.might_max + "\nMight Current = " + char.might_current + "\nMight Edge = " + char.might_edge + "\nSpeed Max = " + char.speed_max + "\nSpeed Current = " + char.speed_current + "\nSpeed Edge = " + char.speed_edge + "\nIntellect Max = " + char.intellect_max + "\nIntellect Current = " + char.intellect_current + "\nIntellect Edge = " + char.intellect_edge + "\nEquipment = " + char.equipment + "\nMoney = " + char.money + "\nAdvancement = " + char.advancement + "\nNotes = " + char.notes + "\nBackground = " + char.background + "\nSkills = " + char.skills + "\nSpecial Abilities = " + char.special_abilities + "\n\n\n```")
			found = True
	if (found == False):
		for char in party:
			if (char.name == char_name):
				if (stat != None):
					if (stat == "name"):
						await bot.say("```What do you think it is?```" %(char.name,char.name))
						found = True
					elif (stat == "descriptor"):
						await bot.say("```%s' descriptor is %s```" %(char.name,char.descriptor))
						found = True
					elif (stat == "type_"):
						await bot.say("```%s' type_ is %s```" %(char.name,char.type_))
						found = True
					elif (stat == "focus"):
						await bot.say("```%s' focus is %s```" %(char.name,char.focus))
						found = True
					elif (stat == "tier"):
						await bot.say("```%s' tier is %s```" %(char.name,char.tier))
						found = True
					elif (stat == "effort"):
						await bot.say("```%s' effort is %s```" %(char.name,char.effort))
						found = True
					elif (stat == "xp"):
						await bot.say("```%s' xp is %s```" %(char.name,char.xp))
						found = True
					elif (stat == "might_max"):
						await bot.say("```%s' might_max is %s```" %(char.name,char.might_max))
						found = True
					elif (stat == "might_current"):
						await bot.say("```%s' might_current is %s```" %(char.name,char.might_current))
						found = True
					elif (stat == "might_edge"):
						await bot.say("```%s' might_edge is %s```" %(char.name,char.might_edge))
						found = True
					elif (stat == "speed_max"):
						await bot.say("```%s' speed_max is %s```" %(char.name,char.speed_max))
						found = True
					elif (stat == "speed_current"):
						await bot.say("```%s' speed_current is %s```" %(char.name,char.speed_current))
						found = True
					elif (stat == "speed_edge"):
						await bot.say("```%s' speed_edge is %s```" %(char.name,char.speed_edge))
						found = True
					elif (stat == "intellect_max"):
						await bot.say("```%s' intellect_max is %s```" %(char.name,char.intellect_max))
						found = True
					elif (stat == "intellect_current"):
						await bot.say("```%s' intellect_current is %s```" %(char.name,char.intellect_current))
						found = True
					elif (stat == "intellect_edge"):
						await bot.say("```%s' intellect_edge is %s```" %(char.name,char.intellect_edge))
						found = True
					elif (stat == "equipment"):
						await bot.say("```%s' equipment list is %s```" %(char.name,char.equipment))
						found = True
					elif (stat == "money"):
						await bot.say("```%s' money is %s```" %(char.name,char.money))
						found = True
					elif (stat == "advancement"):
						await bot.say("```%s' advancement is %s```" %(char.name,char.advancement))
						found = True
					elif (stat == "notes"):
						await bot.say("```%s' notes are %s```" %(char.name,char.notes))
						found = True
					elif (stat == "background"):
						await bot.say("```%s' background is %s```" %(char.name,char.background))
						found = True
					elif (stat == "skills"):
						await bot.say("```%s' skills are %s```" %(char.name,char.skills))
						found = True
					elif (stat == "special_abilities"):
						await bot.say("```%s' special_abilities are %s```" %(char.name,char.special_abilities))
						found = True
				else:
					await bot.say("```Name = " + char.name + "\nDescriptor = " + char.descriptor + "\nType = " + char.type_ + "\nFocus = " + char.focus + "\nTier = " + char.tier + "\nEffort = " + char.effort + "\nXP = " + char.xp + "\nMight Max = " + char.might_max + "\nMight Current = " + char.might_current + "\nMight Edge = " + char.might_edge + "\nSpeed Max = " + char.speed_max + "\nSpeed Current = " + char.speed_current + "\nSpeed Edge = " + char.speed_edge + "\nIntellect Max = " + char.intellect_max + "\nIntellect Current = " + char.intellect_current + "\nIntellect Edge = " + char.intellect_edge + "\nEquipment = " + char.equipment + "\nMoney = " + char.money + "\nAdvancement = " + char.advancement + "\nNotes = " + char.notes + "\nBackground = " + char.background + "\nSkills = " + char.skills + "\nSpecial Abilities = " + char.special_abilities + "```")
					found = True
	if (found == False):
		await bot.say("```I couldn't find that character in the party. (%s)```" %char_name)

@bot.command()
async def weather():
	"""Random weather condition"""
	foo = [ 
		'```It\'s a dry and sunny day with occasional breeze.```',
		'```It\'mostly sunny with only a few passing clouds. There\'s a slight breeze.```',
		'```It\'s cloudy with a strong breeze. It doesn\'nt look like it\'s going to clear up any time soon.```',
		'```Dark clouds begin gathering and the winds are picking up.```',
		'```Acid rain begins to fall. Any metal around you begins to break down in minutes```'
	]
	foo_choice = random.choice(foo)
	await bot.say(foo_choice)

def save_character(char : character):
	fo = open(char.name+".txt", "w+")
	fo.write("name="+ char.name + "\n")
	fo.write("descriptor="+ char.descriptor + "\n")
	fo.write("type_="+ char.type_ + "\n")
	fo.write("focus="+ char.focus + "\n")
	fo.write("tier="+ char.tier + "\n")
	fo.write("effort="+ char.effort + "\n")
	fo.write("xp="+ char.xp + "\n")
	fo.write("might_max="+ char.might_max + "\n")
	fo.write("might_current="+ char.might_current + "\n")
	fo.write("might_edge="+ char.might_edge + "\n")
	fo.write("speed_max="+ char.speed_max + "\n")
	fo.write("speed_current="+ char.speed_current + "\n")
	fo.write("speed_edge="+ char.speed_edge + "\n")
	fo.write("intellect_max="+ char.intellect_max + "\n")
	fo.write("intellect_current="+ char.intellect_current + "\n")
	fo.write("intellect_edge="+ char.intellect_edge + "\n")
	fo.write("equipment="+ char.equipment + "\n")
	fo.write("money="+ char.money + "\n")
	fo.write("advancement="+ char.advancement + "\n")
	fo.write("notes="+ char.notes + "\n")
	fo.write("background="+ char.background + "\n")
	fo.write("skills="+ char.skills + "\n")
	fo.write("special_abilities="+ char.special_abilities + "\n")
	fo.close()

@bot.command()
async def save(var : str):
	found = False
	for char in party:
		if (var == char.name):
			save_character(char)
			found = True
			await bot.say("```Successfully saved %s```" %var)
	if (var == "all"):
		for char in party:
			save_character(char)
			found = True
			await bot.say("```Successfully saved all characters```")
	if (found == False):
		await bot.say("```%s character not found. (try !save all to just save everyone)```")



bot.run('MjI4MjM3MDEyMTAzMjAwNzY5.CsRx3Q.p8llqXeRVGjDhMAtFnjbmjhTvDU')
