# Discord Availability Bot

This bot automatically posts a series of availability messages with reactions when someone types "Run Availability" in a Discord channel.

## Setup Instructions

### 1. Install Python
Make sure you have Python 3.8 or higher installed on your system.

### 2. Install Required Libraries
Run this command in your terminal:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install discord.py python-dotenv
```

### 3. Create a Discord Bot
1. Go to https://discord.com/developers/applications
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot"
5. Under "Privileged Gateway Intents", enable:
   - MESSAGE CONTENT INTENT
   - SERVER MEMBERS INTENT (optional)
6. Click "Reset Token" and copy your bot token

### 4. Invite Bot to Your Server
1. Go to "OAuth2" → "URL Generator"
2. Select scopes: `bot`
3. Select bot permissions:
   - Send Messages
   - Add Reactions
   - Read Message History
   - Manage Messages (to delete the trigger message)
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

### 5. Configure the Bot
1. Create a file named `.env` in the same folder as `availability_bot.py`
2. Add this line to the `.env` file:
   ```
   DISCORD_TOKEN=your_actual_bot_token_here
   ```
3. Replace `your_actual_bot_token_here` with the token you copied earlier
4. The custom emoji IDs are already configured based on your message

**IMPORTANT:** The `.env` file is ignored by git (listed in `.gitignore`) so your token won't be uploaded to GitHub!

### 6. Run the Bot
```bash
python availability_bot.py
```

You should see: `[BotName] has connected to Discord!`

## Usage

Simply type `Run Availability` in any channel where the bot has permissions, and it will:
1. Delete your trigger message
2. Post "# Weekend Availability"
3. Wait 5 seconds
4. Post each timestamp message with automatic reactions
5. Post the final explanation message with role mention

## Important Notes

- The bot must have permission to:
  - Read messages
  - Send messages
  - Add reactions
  - Manage messages (to delete trigger)
  
- Custom emojis MUST exist in the server where you're using the bot
  - The emoji IDs in your message are already configured
  - If emojis don't work, the bot will print errors in the console

- The trigger is case-sensitive: "Run Availability" (exact match)

## Troubleshooting

**Bot doesn't respond:**
- Check that MESSAGE CONTENT INTENT is enabled in Discord Developer Portal
- Verify the bot has proper permissions in the channel
- Check console for error messages

**Reactions don't appear:**
- Verify custom emojis exist in your server
- Check that emoji IDs match your server's emojis
- Bot needs "Add Reactions" permission

**Token errors:**
- Make sure you copied the entire token
- Token should be in quotes: `TOKEN = 'your.token.here'`

## Security Warning

⚠️ **NEVER share your bot token publicly!** Anyone with your token can control your bot.

⚠️ **NEVER commit your .env file to GitHub!** The `.gitignore` file is set up to prevent this, but double-check before pushing.

## GitHub Setup

When using this bot with GitHub:

1. **Clone the repository** to your local machine
2. **Create the .env file locally** (it won't be in the repo due to .gitignore)
3. **Add your token** to the .env file
4. **Run the bot** locally with `python availability_bot.py`

If you need to run this bot on a server or hosting service:
- Most hosting platforms (Heroku, Railway, etc.) let you set environment variables in their dashboard
- Set `DISCORD_TOKEN` as an environment variable with your bot token
- The bot will automatically use it
