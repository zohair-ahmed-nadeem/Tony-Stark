# Shapater Discord Bot

Shapater is a feature-rich Discord bot designed to enhance server management, moderation, and user interaction. It includes a variety of commands and functionalities to make your Discord experience seamless and enjoyable.

## Features

- **Moderation Tools**: Commands for banning, kicking, muting, and managing roles.
- **Channel Management**: Create, delete, lock, unlock, hide, and show channels.
- **Anti-Spam**: Automatically detects and handles spam messages.
- **Soundboard**: Play sound clips in voice channels.
- **AI Integration**: Ask questions and get responses using Groq's AI.
- **Voice Channel Management**: Mute, deafen, and kick users from voice channels.
- **Auto Role Assignment**: Automatically assign roles to new members or bots.
- **Server Information**: Display detailed server stats and member information.
- **Custom Prefix**: Change the bot's command prefix.
- **Welcome and Leave Messages**: Customizable welcome and leave messages for members.
- **Guild Management**: Manage Free Fire guilds with member profiles and roles.

## Commands

### General Commands
- `>help` - Displays the help menu.
- `>prefix` - Shows the current command prefix.
- `>setprefix <new_prefix>` - Changes the bot's command prefix.

### Moderation Commands
- `>ban <@user> [reason]` - Ban a user from the server.
- `>unban <user_id> [reason]` - Unban a user from the server.
- `>kick <@user> [reason]` - Kick a user from the server.
- `>mute <@user> [duration] [reason]` - Mute a user for a specified duration.
- `>unmute <@user> [reason]` - Unmute a user.

### Channel Management
- `>createchannel <name>` - Create a new text channel.
- `>deletechannel <#channel>` - Delete a text channel.
- `>lockchannel <#channel>` - Lock a channel to prevent messages.
- `>unlockchannel <#channel>` - Unlock a channel.
- `>hidechannel <#channel>` - Hide a channel from everyone.
- `>showchannel <#channel>` - Make a hidden channel visible.

### Anti-Spam
- Automatically detects and handles spam messages.
- `>antispam_enable` - Enable anti-spam.
- `>antispam_disable` - Disable anti-spam.

### Soundboard
- `>sb <clip_name>` - Play a sound clip in a voice channel.
- `>disconnect` - Disconnect the bot from the voice channel.

### AI Integration
- `>ask <query>` - Ask a question and get a response from Groq AI.
- `>ai <query>` - Query Groq AI directly.

### Guild Management
- `>addguild <@members>` - Add members to your Free Fire guild.
- `>myprofile` - View your guild profile.
- `>addguildowner <guild_name> <@owner>` - Add a guild owner.
- `>removeguildowner <@owner>` - Remove a guild owner.

### Auto Role
- `>auto sethuman <role_id>` - Set auto-role for humans.
- `>auto setbot <role_id>` - Set auto-role for bots.
- `>auto clearhuman` - Clear auto-role for humans.
- `>auto clearbot` - Clear auto-role for bots.

### Server Information
- `>serverinfo` - Display detailed server information.
- `>aboutbot` - Show information about the bot.
- `>membercount` - Display the total number of members in the server.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zohair-ahmed-nadeem/Tony-Stark.git
   ```
2. Navigate to the project directory:
  ```
  cd shapater-discord-bot
  ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure the bot by editing the `config.py` file with your bot token and other settings.
5. Run the bot:
   ```
   python main.py
   ```
## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Developed by ZAN ✨
- Powered by Discord.py and Groq AI.
  
## Links
- [Invite the Bot](https://discord.com/oauth2/authorize?client_id=1184035274037137478&permissions=8&integration_type=0&scope=bot)
- [Support Server](https://discord.gg/GXuZVF4573)
