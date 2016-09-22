import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

class character:
	def __init__ (self, name, descriptor, type_, focus, tier, effort, xp, might_max, might_current, might_edge, speed_max, speed_current, speed_edge, intellect_max, intellect_current, intellect_edge, equipment, money, advancement, notes, background, skills, special_abilities):
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
