import discord
from discord.ext import commands
from model import get_class
import os, random
import requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''The duck command returns the photo of the duck'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await ctx.send(f'file berhasil disimpan dengan nama {file_name}')
            await ctx.send(f'dapat juga diakses melalui cloud discord di  {file_url}')

            kelas, skor = get_class('keras_model.h5', 'labels.txt', f'./{file_name}')

            if kelas == 'merpati' and skor >= 0.75:
                await ctx.send('dia adalah burung merpati yang selalu dicari dan diburu oleh pemburu untuk dipelihara dan burung ini harga jualnya cukup tinggi untuk sekelas burung untuk dipelihara makanan burung ini adalah pelet burung dan jagung')
            elif kelas == 'pipit' and skor >= 0.75:
                await ctx.send('dia adalah burung pipit yang selalu berkicau di pagi hari dan pergi mencari makan di pagi hari dan di sore hari dan burung ini tidur di malam hari dan makanan burung ini adalah pelet dan jagung')
            else:
                await ctx.send('aku tidak tau itu jenis burung apa!')
    else:
        await ctx.send('kamu tidak melampirkan apa apa!')
