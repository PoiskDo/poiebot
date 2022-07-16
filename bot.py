from cProfile import label
import discord, os, time, asyncio
from discord.ext import commands
from discord.ui import Button
import random
from to import Token

bot=commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.command(aliases=['hi'])
async def 안녕(ctx):
    await ctx.send('안녕하세요.')
@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)
@bot.command()
async def 개발자(cfx):
       await cfx.send('개발자: Poiega#1562')
@bot.slash_command(description="주사위를 굴려봅시다")
async def roll(ctx):
    embed = discord.Embed(title="🎲 주사위를 굴립니다...")
    await ctx.respond(embed=embed)
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    if a > b:
        embed = discord.Embed(title="✅ 성공!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0x42f55d)
        await ctx.respond(embed=embed)
    elif a == b:
        embed = discord.Embed(title="무승부!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0xffffff)
        await ctx.respond(embed=embed)
    elif a < b:
        embed = discord.Embed(title="❌ 실패!", description="봇의 숫자: " + str(a) + " 당신의 숫자: " +  str(b), color=0xff2200)
        await ctx.respond(embed=embed)
bot.run(Token)
