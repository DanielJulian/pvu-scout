import discord

class DiscordClient(discord.Client):
            
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        """
        if str(message.author) == 'EPIC RPG#4117':
            self.handle_epic_rpg_message(message)
        
        elif "rpg arena" in message.content.strip().lower():
            print(str(message.author) + " created an arena... Joining")
            self.feedback_queue.put("Join Arena")

        elif "rpg miniboss" in message.content.strip().lower():
            print(str(message.author) + " will fight a miniboss... Lets fight!!")
            self.feedback_queue.put("Join Fight")

        elif message.content.startswith("<@&848779233706770483>"): # <@&848779233706770483> is the ID for @EPICARDOS
            self.handle_epicardos_tag(message)

        # Always log my stuff
        if str(message.author) == os.getenv('discord_user_name_and_tag'):
            print("-------------------------------------------------------------------------------------------")
            print(os.getenv('discord_user_name') + " sent a message: " + message.content)
        """

    async def send_message(self, message):
        text_channels = self.guilds[0].text_channels
        for channel in text_channels:
            if channel.id == 734752242053414923:
                await channel.send(message)