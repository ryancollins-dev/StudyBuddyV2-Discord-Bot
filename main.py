# StudyBuddy V2 Discord Bot by Ryan Collins
#Aug 6, 2021
import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()
my_secret = os.environ['TOKEN']
study_words = ["study", "Study"]

a = []
a = open("data.txt")
contents = a.readlines()
a.close()
print("How about?: ", random.choice(contents)),

if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("!study"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = contents
    if "study" in db.keys():
      options = options + db["study"]

    if any(word in msg for word in study_words):
      await message.channel.send(random.choice(options))

keep_alive()
client.run(os.getenv("TOKEN"))
