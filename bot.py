from cProfile import label
from cgitb import text
import discord, os, time, asyncio
from discord.ext import commands
import random
from game import dice
from to import Token

bot=commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
@bot.command(aliases=['hi'])
async def 안녕(ctx):
    await ctx.send('안녕하세요.')
@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)
@bot.command()
async def 개발자(cfx):
       await cfx.send('개발자: Poiega#1562')
@bot.command()
async def 도린아(cfx):
        await cfx.send('네!')
@bot.command()
async def 도박(cfx):
        await cfx.send('현재 이 기능은 구현 중 입니다.')
@bot.command
async def 개발(cfx):
        await cfx.send('오류: Error 404')
@bot.command()
async def 회원가입(ctx):
    #print(ctx.author.name)
    #print(ctx.author.id)
    if checkName(ctx.author.name, ctx.author.id):
        signup(ctx.author.name, ctx.author.id)
        await ctx.send("회원가입이 완료되었습니다.")
    else:
        await ctx.send("이미 가입하셨습니다.")
@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice
    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "Super Bot의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def leave(ctx):
	await bot.voice_clients[0].disconnect()
@bot.command()
async def reset(ctx):
delete()
@bot.command()
async def 내정보(ctx):
	money, level = userInfo(ctx.author.name, ctx.author.id)
    
    if money == None or level == None:
    	await ctx.send("등록되지 않은 사용자입니다.")
    else:
    	emebed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name="레벨", value = level)
        embed.add_field(name="보유 자산", value = money)
        await ctx.send(embed=embed)
@bot.command()
async def 송금(ctx, user: discord.User, money):
    if checkName(user.name, user.id):
        await ctx.send("등록되지 않는 사용자입니다.")
    else:
        if getMoney(ctx.author.name, ctx.author.id) >= int(money):
            await ctx.send("송금")
        else:
            await ctx.send("돈이 충분하지 않습니다.")
            @bot.command()
async def 송금(ctx, user: discord.User, money):
    if findRow(user.name, user.id) == None:
        await ctx.send("등록되지 않는 사용자입니다.")
    else:
        s_money = getMoney(ctx.author.name, ctx.author.id)
        r_money = getMoney(user.name, user.id)

        if s_money >= int(money):
            remit(ctx.author.name, ctx.author.id, user.name, user.id, money)

            embed = discord.Embed(title="송금 완료", description = "송금된 돈: " + money, color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(getMoney(ctx.author.name, ctx.author.id)))
            embed.add_field(name = ":arrow_forward:", value = "")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(getMoney(user.name, user.id)))
                    
            await ctx.send(embed=embed)
        else:
            await ctx.send("돈이 충분하지 않습니다.")     
@bot.command()
async def 홀짝(ctx, face, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    forecast = coin()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        cur_money = getMoney(ctx.author.name, userRow)
        if int(money) >= 10:
            if cur_money >= int(money):
                if face == "홀" or face == "짝":
                    if forecast == face:
                        result = "성공"
                        _color = 0x00ff56

                        betting = int(money)

                        modifyMoney(ctx.author.name, userRow, 0.5*betting)
                    else:
                        result = "실패"
                        _color = 0xFF0000

                        betting = int(money)
                        
                        modifyMoney(ctx.author.name, userRow, -int(betting))
                        addLoss(ctx.author.name, userRow, int(betting))

                    embed = discord.Embed(title = "홀짝게임 결과", description = result, color = _color)
                    embed.add_field(name = "배팅금액", value = betting, inline = False)
                    embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("홀 또는 짝을 입력하세요")
            else:
                await ctx.send("돈이 부족합니다. 현재자산: " + str(cur_money))
        else:
            await ctx.send("10원 이상만 배팅 가능합니다.")
    else:
        await ctx.send("홀짝게임은 회원가입 후 이용 가능합니다.")
@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, money, loss = userInfo(userRow)
        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = "레벨", value = level)
        embed.add_field(name = "보유 자산", value = money)
        embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)
@bot.command()
async def 정보(ctx, user: discord.User):
    userExistance, userRow = checkUser(user.name, user.id)

    if not userExistance:
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, money, loss = userInfo(userRow)
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = "레벨", value = level)
        embed.add_field(name = "보유 자산", value = money)
        embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)   
@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss = userInfo(userRow)

        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = "레벨", value = level)
        embed.add_field(name = "경험치", value = exp)
        embed.add_field(name = "보유 자산", value = money, inline = False)
        embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)

@bot.command()
async def 정보(ctx, user: discord.User):
    userExistance, userRow = checkUser(user.name, user.id)

    if not userExistance:
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        
        embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
        embed.add_field(name = "레벨", value = level)
        embed.add_field(name = "경험치", value = exp)
        embed.add_field(name = "보유 자산", value = money, inline = False)
        embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)
@bot.event
async def on_message(message):
	if message.author == bot.user:
    	return
    print("levelup!")
    await bot.process_commands(message)      

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    userExistance, userRow = checkUser(message.author.name, message.author.id)
    channel = message.channel
    if userExistance:
        levelUp, lvl = levelupCheck(userRow)
        
        if levelUp:
            embed = discord.Embed(title = "레벨업", description = None, color = 0x00A260)
            embed.set_footer(text = message.author.name + "이 " + str(lvl) + "레벨 달성!")
            await channel.send(embed=embed)
        else:
            addExp(userRow, 1)

    await bot.process_commands(message)
    @bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        userNum = checkUserNum()
        embed = discord.Embed(title="유저 정보", description = ctx.author.name, color = 0x62D0F6)
        embed.add_field(name = "레벨", value = level)
        embed.add_field(name = "경험치", value = str(exp) + "/" + str(level*level + 6*level))
        embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
        embed.add_field(name = "보유 자산", value = money, inline = False)
        embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

        await ctx.send(embed=embed)
@bot.command()
async def 랭킹(ctx):
    rank = ranking()
    embed = discord.Embed(title = "레벨 랭킹", description = None, color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            lvl = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="레벨: "+str(lvl), inline=False)

    await ctx.send(embed=embed)    
bot.run(Token)
