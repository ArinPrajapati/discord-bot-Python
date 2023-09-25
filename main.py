import discord
import os
import requests

intents = discord.Intents.all()

client = discord.Client(intents=intents)

valid_categories = [
    'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday',
    'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death',
    'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family',
    'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god',
    'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor',
    'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal',
    'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # Always print the message content
    print("Message ID:", message.id)
    print("Content:", message.content)
    print("Channel Name:", message.channel.name)
    print("Author Name:", message.author.name)
    print("Guild Name:", message.guild.name)

    # Check if the message author is the bot
    if message.author == client.user:
        return

    # Check if any word in the message matches a valid category
    matching_category = None
    for word in valid_categories:
        if word in message.content.lower():  # Convert to lowercase for case-insensitive matching
            matching_category = word
            break

    if matching_category:
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(matching_category)
        print("API URL:", api_url)  # Debugging line to check the constructed URL
        response = requests.get(api_url, headers={'X-Api-Key': 'syADX+R4WkxmKMstuOE6Gg==ipIiD9ut7tcJ5X4w'})

        if response.status_code == requests.codes.ok:
            quote_data = response.json()
            if quote_data:  # Check if there are quotes available for the specified category
                quote = quote_data[0]["quote"]
                author = quote_data[0]['author']
                await message.channel.send(quote + " -" + author)
            else:
                await message.channel.send("No quotes found for the specified category.")
        else:
            await message.channel.send("Error: Unable to fetch a quote.")
    else:
        await message.channel.send("No valid category found in the message.")


client.run('MTE1NTc0MzQ4NDg3NjE4MTU0NA.G8-Bz_.3WZLzQsS2VjNRBSb2PP_K8TyYiYLkXum7NEVgw')
