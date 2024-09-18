import discord
from discord.ext import commands
from commands import bot
from settings import token

# Botun hazır olduğunu gösteren mesaj
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} olarak giriş yaptı.")

# Discord botunu başlat
bot.run(token)