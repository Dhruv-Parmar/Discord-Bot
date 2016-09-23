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
async def roll(dice : str):
	"""Rolls a dice in NdN format."""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		await bot.say('Format has to be in NdN!')
		return

	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
	"""Chooses between multiple choices."""
	await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
	"""Repeats a message multiple times."""
	for i in range(times):
		await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
	"""Says when a member joined."""
	await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def load(char_name):
	"""Load specified character"""
	data = []
	exists = False
	fo = open(char_name + ".txt", "r")
	data = [line.rstrip('\n') for line in fo]
	fo.close()
	for i,v in enumerate(data[:]):
		tok = v.find('=')
		data[i] = v[tok+1:]
	for char in party:
		if (data[0] == char.name):
			await bot.say('%s already exists in the party.' %char_name)
			exists = True
	if (exists == False):
		temp = character(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22])
		party.append(temp)
		await bot.say('%s has been added to the party!' %data[0])

@bot.command()
async def display(char_name):
	"""Displays players stats n stuff"""
	found = False
	for char in party:
		if (char.name == char_name):
			await bot.say("Name = " + char.name + "\nDescriptor = " + char.descriptor + "\nType = " + char.type_ + "\nFocus = " + char.focus + "\nTier = " + char.tier + "\nEffort = " + char.effort + "\nXP = " + char.xp + "\nMight Max = " + char.might_max + "\nMight Current = " + char.might_current + "\nMight Edge = " + char.might_edge + "\nSpeed Max = " + char.speed_max + "\nSpeed Current = " + char.speed_current + "\nSpeed Edge = " + char.speed_edge + "\nIntellect Max = " + char.intellect_max + "\nIntellect Current = " + char.intellect_current + "\nIntellect Edge = " + char.intellect_edge + "\nEquipment = " + char.equipment + "\nMoney = " + char.money + "\nAdvancement = " + char.advancement + "\nNotes = " + char.notes + "\nBackground = " + char.background + "\nSkills = " + char.skills + "\nSpecial Abilities = " + char.special_abilities)
			found = True
	if (found == False):
		await bot.say("I couldn't find that character in the party. (%s)" %char_name)

@bot.command()
async def weather():
	"""Random weather condition"""
	foo = [ 
		'It\'s a dry and sunny day with occasional breeze.',
		'It\'mostly sunny with only a few passing clouds. There\'s a slight breeze.',
		'It\'s cloudy with a strong breeze. It doesn\'nt look like it\'s going to clear up any time soon.',
		'Dark clouds begin gathering and the winds are picking up.',
		'Acid rain begins to fall. Any metal around you begins to break down in minutes'
	]
	foo_choice = random.choice(foo)
	await bot.say(foo_choice)

@bot.group(pass_context=True)
async def cool(ctx):
	"""Says if a user is cool.
	In reality this just checks if a subcommand is being invoked.
	"""
	if ctx.invoked_subcommand is None:
		await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
	"""Is the bot cool?"""
	await bot.say('Yes, the bot is cool.')

bot.run('MjI4MjM3MDEyMTAzMjAwNzY5.CsRx3Q.p8llqXeRVGjDhMAtFnjbmjhTvDU')
