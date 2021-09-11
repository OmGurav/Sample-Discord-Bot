import discord
import os
import requests
import json
import urllib
import random
from replit import db
from keep_alive import keep_alive
import img


client = discord.Client()

sad_words = ["sad","unhappy","depressed","angry","miserable","degressing"]

starter_encouragements = [
  "Cheer up!!", "Hang in there..", "You are a great person!", "You can do it!"
]

help = [
     ">>> **Help Commands** \n\nThese are the available commands:\n\n1. `$help` - Dailogue of all commands\n2. `$info` - Gives info of bot\n3. `$inspire` - presents quote\n4. `$meme` - presents meme\n5. `$search github` - searches the user on github\n6. `$GDSC lead` - presents GDSC Lead person\n7. `$GDSC core team` - presents GDSC Core team members\n8. `$GDSC tech team` - presents GDSC technical team members\n8. `$GDSC smo team` - presents GDSC social Media & outfare team members\n8. `$GDSC event team` - presents GDSC events team members\n8. `$GDSC wtm team` - presents GDSC wtm team members\n\n_This bot is Open Source_"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote =  json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.key():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
  else:
    db["encouragements"] = [encouraging_message] 

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

def search_github_user(username):
  response = urllib.request.urlopen("https://api.github.com/users/" + username )
  data = json.loads(response.read())
  github_url = data["html_url"]
  github_repos = data["repos_url"]
  github_resource = [github_url,github_repos]
  return github_resource

def get_meme():
  url = "https://some-random-api.ml/meme"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  path = data["image"]
  return path


@client.event
async def on_ready():
  print('Bot is live now as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith('$help'):
    await message.channel.send(''.join(help))

  if msg.startswith('$info'):
    await message.channel.send('>>> GDSC Bot v1.0.1')

  if msg.startswith('$GDSC lead'):
    await message.channel.send('>>> \n**GDSC GESCOENGG LEAD** \n\n Atharva Chandwadkar') 

  if msg.startswith('$GDSC core team'):
    await message.channel.send('>>> \n**GDSC GESCOENGG CORE TEAM** \n\n Preyas Mishra \t --Technical \n Saurabh kayande \t --Social Media & Outreach \n Mandar Pandit \t --Designing \n Pranali Redgaonkar \t --Events \n Pranjal Nawarkar \t --WTM') 
   
  if msg.startswith('$GDSC tech team'):
    await message.channel.send('>>> \n**GDSC GESCOENGG TECHNICAL TEAM** \n\n Om Gurav \n Nilesh Chinchole \n Vaishnavi Date \n Shrikant Gosavi \n Komal Patil') 
  
  if msg.startswith('$GDSC event team'):
    await message.channel.send('>>> \n**GDSC GESCOENGG EVENTS TEAM** \n\n Aniket Kote \n Aashutosh Chandratre \n Parth Parmar')

  if msg.startswith('$GDSC wtm team'):
    await message.channel.send('>>> \n**GDSC GESCOENGG WTM TEAM** \n\n Sharvari Tamboli \n Nikita Zalte')  

  if msg.startswith('$GDSC smo team'):
    await message.channel.send('>>> \n**GDSC GESCOENGG SM & O TEAM** \n\n Gaurav Patkari  \n Tanaya shisode \n Atharv Kare')    
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if msg.startswith("$search github"):
      user = msg.split(" ",2)[2]
      github_result = search_github_user(user)
      await message.channel.send(">>> " + github_result[0]) 

  if msg.startswith('$meme'):
    meme = get_meme()
    await message.channel.send(meme)       


keep_alive()

my_secret = os.environ['TOKEN']

client.run(my_secret)      