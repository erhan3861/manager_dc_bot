import discord
from discord.ext import commands
from database import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Kullanıcı ekleme komutu
@bot.command()
async def add_task(ctx, description):
    add_new_task(description)
    await ctx.send(f"{description} konulu görev eklendi.")

@bot.command()
async def delete_task(ctx, task_id):
    if delete_task_with_id(task_id):
        await ctx.send(f"{task_id} nolu görev silindi.")
    else:
        await ctx.send(f"{task_id} nolu görev silinemedi.")

@bot.command()
async def show_tasks(ctx):
    tasks = all_tasks()
    if tasks:
        result = ""
        for task in tasks:
            result += str(task.id) + "\t" + task.description +  "\t" + task.status + "\n"
        await ctx.send("Kayıtlı Görevler Listesi : \n" + result)
    else:
        await ctx.send("Kayıtlı görev bulunamadı.")

@bot.command()
async def complete_task(ctx, task_id):
    if complete_task_with_id(task_id):
        await ctx.send(f"{task_id} nolu görev complete olarak işaretlendi.")
    else:
        await ctx.send(f"{task_id} nolu görev bullunamadı.")



