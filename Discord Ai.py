import discord
from discord.ext import commands
import asyncio
import os
import time
import numpy
import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
client = discord.Client()


@client.event
async def on_message(message):
    prefix = message.content
    text = gpt2.generate(sess,
                         length=100,
                         temperature=.7,
                         prefix=prefix,
                         nsamples=1,
                         batch_size=1,
                         return_as_list=True
                         )
    await message.channel.send(text[0])
    if message.content.startswith('hello'):
        await message.channel.send("hi")
    if str(message.channel) != "zoom-codes" and message.content.startswith("https"):
        await message.channel.purge(limit=1)
        await message.channel.purge(limit=1)
        await message.channel.send("Do not send this link in the channel")


Token = 'NzExMzY2OTU4NTIzODc1MzY4.XxZv8A.JAm4o-k-mZHmNCU3-oDKP5TJ34s'
client.run(Token)
