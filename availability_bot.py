import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Custom emoji IDs (you'll need to replace these with your server's emoji IDs)
EMOJI_MAP = {
    "ON": "<:ON:1472893645505167441>",
    "OFF": "<:OFF:1472893946274381854>",
    "T7": "<:T7:1472892621360726158>",
    "T8": "<:T8:1472891599448182845>",
    "T9": "<:T9:1472891320900259981>",
    "T10": "<:T10:1472887599898296360>",
    "T11": "<:T11:1472885123182628946>",
    "T12": "<:T12:1472884916655099986>",
    "41D": "<:41D:1472894922636918827>",
    "60D": "<:60D:1472895311474331709>"
}

# Message sequence with reactions
MESSAGE_SEQUENCE = [
    {"text": "# Weekend Availability", "wait": 5, "reactions": []},
    {"text": "# <t:1771272900:t> - <t:1771275600:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771275600:t> - <t:1771279200:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771279200:t> - <t:1771282800:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771282800:t> - <t:1771286400:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771286400:t> - <t:1771290000:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771290000:t> - <t:1771293600:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771293600:t> - <t:1771297200:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771297200:t> - <t:1771300800:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771300800:t> - <t:1771218000:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771218000:t> - <t:1771221600:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771221600:t> - <t:1771225200:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771225200:t> - <t:1771228800:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771228800:t> - <t:1771232400:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771232400:t> - <t:1771236000:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771236000:t> - <t:1771239600:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771239600:t> - <t:1771243200:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771243200:t> - <t:1771246800:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771246800:t> - <t:1771250400:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771250400:t> - <t:1771254000:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771254000:t> - <t:1771257600:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771257600:t> - <t:1771261200:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771261200:t> - <t:1771264800:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771264800:t> - <t:1771268400:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": "# <t:1771268400:t> - <t:1771272900:t>", "wait": 5, "reactions": ["ON", "OFF", "T7", "T8", "T9", "T10", "T11", "T12", "41D", "60D"]},
    {"text": """Please take the time <@&1260319763742326947> to complete your availability for this upcoming weekend below you'll find the following reactions meaning.  
<:ON:1472893645505167441> - Will be online during that time
<:OFF:1472893946274381854> - Will be offline during that time
<:T7:1472892621360726158> - Troop tier T7 (K21 and below)
<:T8:1472891599448182845> - Troop tier T8 (K22-25)
<:T9:1472891320900259981> - Troop tier T9 (K26-K29)
<:T10:1472887599898296360> - Troop tier T10 (K30-K33)
<:T11:1472885123182628946> - Troop tier T11 (K34-K39)
<:T12:1472884916655099986> - Troop tier T12 (K40)
<:41D:1472894922636918827> - Dragon 41+ (Can join on SOP Rallies)
<:60D:1472895311474331709> - Dragon 60+ (Can reinforce SOPs)""", "wait": 0, "reactions": []}
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready to use in servers.')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Check if the message is "Run Availability"
    if message.content.strip() == "Run Availability":
        print(f"Triggered by {message.author} in {message.channel}")
        
        # Delete the trigger message
        await message.delete()
        
        # Execute the sequence
        for step in MESSAGE_SEQUENCE:
            # Send the message
            sent_message = await message.channel.send(step["text"])
            
            # Add reactions if specified
            for reaction_name in step["reactions"]:
                try:
                    # Try to add custom emoji
                    emoji_string = EMOJI_MAP.get(reaction_name, reaction_name)
                    await sent_message.add_reaction(emoji_string)
                except discord.errors.HTTPException as e:
                    print(f"Failed to add reaction {reaction_name}: {e}")
                except Exception as e:
                    print(f"Error adding reaction {reaction_name}: {e}")
            
            # Wait before next message
            if step["wait"] > 0:
                await asyncio.sleep(step["wait"])
        
        print("Availability sequence completed!")
    
    # Process other commands
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    # Get token from environment variable
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    if not TOKEN:
        print("ERROR: DISCORD_TOKEN not found in .env file!")
        print("Please create a .env file with your bot token.")
        exit(1)
    
    bot.run(TOKEN)
