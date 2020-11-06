# This is a sample Python script.
import discord
import logging
import secret


class MyClient(discord.Client):
    pre = '.'

    async def on_ready(self):
        print('We have logged in as {0.user}!'.format(client))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('.hello'):
            await message.channel.send('Hello!')

        print('Message from {0.author}: {0.content}'.format(message))


if __name__ == '__main__':
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    client = MyClient()
    client.run(secret.token)
