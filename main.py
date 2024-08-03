import discord
from discord.ext import commands
import random
from model import get_class
import os
import requests

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
async def checkanimals(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="animals.h5", labels_path="animals.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")




@bot.command()
async def checkchess(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="chess.h5", labels_path="chess.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")



@bot.command()
async def checkflowers(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="flowers.h5", labels_path="flowers.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")





@bot.command()
async def checkgarbage(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="garbage.h5", labels_path="garbage.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")





@bot.command()
async def checkgame(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="game.h5", labels_path="game.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")




@bot.command()
async def checkactivity(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="activity.h5", labels_path="activity.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")





@bot.command()
async def mem(ctx):
    resimler_listesi = os.listdir("gif")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/gif/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem_mc(ctx):
    resimler_listesi = os.listdir("minecraft")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/minecraft/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def mem_vt(ctx):
    resimler_listesi = os.listdir("valorant")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/valorant/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def mem_lol(ctx):
    resimler_listesi = os.listdir("league of legends")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/league of legends/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)    


@bot.command()
async def mem_bs(ctx):
    resimler_listesi = os.listdir("brawl stars")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/brawl stars/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_gta(ctx):
    resimler_listesi = os.listdir("gta v")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/gta v/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_squid(ctx):
    resimler_listesi = os.listdir("squid game")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/squid game/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_troll(ctx):
    resimler_listesi = os.listdir("troll face")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/troll face/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_beast(ctx):
    resimler_listesi = os.listdir("mrbeast")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/mrbeast/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_minion(ctx):
    resimler_listesi = os.listdir("minion")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/minion/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_subway(ctx):
    resimler_listesi = os.listdir("subway surfers")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/subway surfers/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 


@bot.command()
async def mem_among(ctx):
    resimler_listesi = os.listdir("among us")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/among us/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 

@bot.command()
async def mem_roblox(ctx):
    resimler_listesi = os.listdir("roblox")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/roblox/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture) 



@bot.command()
async def mem_genshin(ctx):
    resimler_listesi = os.listdir("genshin impact")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/genshin impact/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)     



@bot.command()
async def mem_sasuke(ctx):
    resimler_listesi = os.listdir("sasuke")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/sasuke/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)     


@bot.command()
async def mem_monkey(ctx):
    resimler_listesi = os.listdir("monkey")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/monkey/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)  


@bot.command()
async def mem_giraffe(ctx):
    resimler_listesi = os.listdir("giraffe")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/giraffe/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)  

@bot.command()
async def mem_laugh(ctx):
    resimler_listesi = os.listdir("laugh")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/laugh/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)  



@bot.command()
async def mem_clash(ctx):
    resimler_listesi = os.listdir("clash royale")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/clash royale/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)  



@bot.command()
async def mem_cyperpunk(ctx):
    resimler_listesi = os.listdir("cyperpunk")
    rastgele_resim = random.choice(resimler_listesi)
    with open(f'STORAGE/cyperpunk/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)          



bot.run('')
