import discord
import asyncio
import random
#import youtube_dl
from discord import activity
# from youtube_dl import * #ydl.py import
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?!",intents =intents)
client = discord.Client(intents=intents)
token = open("distoken.txt", "r").readline()



@client.event
async def on_ready():

    print(client.user.name)
    print('봇 실행 완료')
    game = discord.Game('이떠가 만듦')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

#주고 받기
    if message.content == "테스트":
        await message.channel.send("성공!")
    if message.content == "게이":
        await message.channel.send("아 ㅇㅋ ㅇㅈ")
    if message.content == "져":
        await message.channel.send("라")
    if message.content == "아 뭐하지":
        await message.channel.send("ㄹㅇ")
    if message.content == "이떠봇":
        await message.channel.send("네?")
    if message.content == "이떠 도배했어?":
        await message.channel.send("아니요")
    if message.content == "게임게임게임이것은이스털에그입네다":
        await message.channel.send("이거슨 이스털에그 입니다")
    if message.content == "korea":
        await message.channel.send(":flag_kr:")
    if message.content == "발로":
        await message.channel.send("@발로란트 파티")
    if message.content == "이떠님 생일 축하 드려요":
        await message.channel.send("이떠님 생일 축하 드려요")
#임베드
    
    if message.content == "이떠":
        embed1 = discord.Embed(title="이떠이떠", description="음", color=0x00ff00)
        embed1.set_thumbnail(url="https://i1.ruliweb.com/cmt/21/06/02/179cae51c9c49c106.gif")
        embed1.add_field(name="현제 관심사", value="ㅎㅎ", inline=False)
        embed1.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed1)

    if message.content == "횬만":
        embed2 = discord.Embed(title="hyonmani", description="나는 지금 브론즈 1에있지만 나는 내일 실버를 가고말것이다 라고하면서 못가는게 내 인생이다 그렇지만 친구들이잘해주기때문에 나는 이기고있다 그리고 나는 야쉬아일랜드 라는 가수가 좋아서 거의 맨날 노래를 듣는다 하지만 가끔씩 다른 노래를 듣기도하는데 나는 그래서 기분이 좋아서 춤을 추기도한다 하지만 나는 게임을 할때는 집중을 해서 손에 땀이 많이나기도 하고 oh zoom이 나오기 직전일 떄도있다 하지만 나는 지금 엄청나게 긴 문장을 쓰고있다 그이유는 잉떠가 쓸데없이 긴문장이 좋다고해서 나는 자고있다", color=0x00ff00)
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/874151619380527114/896779330523385866/2021-10-10_030452.png")
        embed2.add_field(name="현제 관심사", value="발로란트", inline=False)
        embed2.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed2)

    if message.content == "학토":
        embed3 = discord.Embed(title="이학토", description="실버 승급 ㄱㅁㅉ", color=0x000000)
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/781728420433231892/1151186241233113291/hakto.png")
        embed3.add_field(name="현제 관심사", value="이떠 제발 승승패패패", inline=False)
        embed3.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed3)

    if message.content  == "윤건":
        embed4 = discord.Embed(title="권윤권", description="치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야 나와줘~치치야", color=0xFFC0CB)
        embed4.set_footer(text="이떠봇 제작사")
        embed4.set_thumbnail(url="https://discord.com/assets/4c1b599b1ef5b9f1874fdb9933f3e03b.png")
        await message.channel.send(embed=embed4)

    if message.content == "예성":
        embed5 = discord.Embed(title="이예성", description="평범한? 예성이다")
        embed5.add_field(name="현제 상태", value="라이덴 존버 4501일차", inline=False)
        embed5.set_footer(text="이떠봇 제작사")
        embed5.set_thumbnail(url="https://cdn.discordapp.com/avatars/556451202150432789/4d7957d3c7d48dc925bd8b7adbce6815.webp?size=128")
        await message.channel.send(embed=embed5)
        
    if message.content == "이겨쓰":
        embed6 = discord.Embed(title='"아 이미 이겼다"', description="이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!이겨쓰!이겨쓰!이겨쓰! 이~겨쓰!", color=0xFF5E00)
        embed6.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed6)

#로블

    if message.content == "로블하실분":
        embed = discord.Embed(title="로블록스", description="누군가가 로블할사람을 모집중 입니다", color=0x000000)
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1131599526001692672/D40KVhLQ_400x400.png")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

    if message.content == "로블할사람":
        embed = discord.Embed(title="로블록스", description="누군가가 로블할사람을 모집중 입니다", color=0x000000)
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1131599526001692672/D40KVhLQ_400x400.png")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

    if message.content == "로블 ㄱ?":
        embed = discord.Embed(title="로블록스", description="누군가가 로블할사람을 모집중 입니다", color=0x000000)
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1131599526001692672/D40KVhLQ_400x400.png")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

#롤 

    if message.content == "롤하실분":
        embed = discord.Embed(title="League of Legends", description="누군가가 롤할사람을 모집중 입니다", color=0xF3E83F)
        embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)



    if message.content == "롤할사람":
        embed = discord.Embed(title="League of Legends", description="누군가가 롤할사람을 모집중 입니다", color=0xF3E83F)
        embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

    if message.content == "롤하실?":
        embed = discord.Embed(title="League of Legends", description="누군가가 롤할사람을 모집중 입니다", color=0xF3E83F)
        embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

    if message.content == "롤 ㄱ?":
        embed = discord.Embed(title="League of Legends", description="누군가가 롤할사람을 모집중 입니다", color=0xF3E83F)
        embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

    if message.content == "롤ㄱ?":
        embed = discord.Embed(title="League of Legends", description="누군가가 롤할사람을 모집중 입니다", color=0xF3E83F)
        embed.set_thumbnail(url="https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg")
        embed.set_footer(text="이떠봇 제작사")
        await message.channel.send(embed=embed)

#확률
    
    if message.content == "운세":
        ran = random.randint(0,2)
        if ran == 0:
            luck = "나쁨"
        if ran == 1:
            luck = "보통"
        if ran == 2:
            luck = "좋음"
        await message.channel.send(luck)

    if message.content == "롤":
        ran = random.randint(0,1)
        if ran == 0:
            game = "일겜"
        if ran == 1:
            game = "칼바"
        await message.channel.send(game)

    if message.content == "발로란트":
        ran = random.randint(0,2)
        if ran == 0:
            luck = "일반"
        if ran == 1:
            luck = "스돌"
        if ran == 2:
            luck = "데스메치"
        if ran == 3:
            luck = "이벤트"
        await message.channel.send(luck)

    if message.content == "라인":
        ran = random.randint(0.4)

    if message.content == "스펠":
        ran = random.randint(0,1)
        ran2 = random.randint(0,6)
        while ran == ran2:
            ran = random.randint(0,1)
            ran2 = random.randint(0,6)
        if ran == 0:
            luck = "점멸"
        if ran == 1:
            luck = "유체화"
        if ran2 == 0:
            luck2 = "점멸"
        if ran2 == 1:
            luck2 = "유체화"
        if ran2 == 2:
            luck2 = "점화"
        if ran2 == 3:
            luck2 = "힐"
        if ran2 == 4:
            luck2 = "탈진"
        if ran2 == 5:
            luck2 = "강타"
        if ran2 == 6:
            luck2 = "정화"
        end = luck + ", " + luck2
        await message.channel.send(end)

    if message.content == "게임":
        ran = random.randint(0,9)
        if ran == 0:
            game = "로블"
        if ran == 1:
            game = "롤"
        if ran == 2:
            game = "마크"
        if ran == 3:
            game = "SCP"
        if ran == 4:
            game = "하지마셈 ㅋ"
        if ran == 5:
            game = "블서"
        if ran == 6:    
            game = "raft"
        if ran == 7:
            game = "배그"
        if ran == 8:
            game = "롤체"
        if ran == 9:
            game = "발로"
        if ran == 10:
            game == "굳굳덕"
        await message.channel.send(game)

    if message.content == "반반":
        ran = random.randint(0,1)
        if ran == 0:
            game = "게임1"
        if ran == 1:
            game = "게임2"
        await message.channel.send(game)
    
    if message.content == "전화":
        ran = random.randint(0,1)
        if ran == 0:
            game = "ㄱ"
        if ran == 1:
            game = "ㄴ"
        await message.channel.send(game)

    if message.content == "탈옥시도":
        ran = random.randint(0,99)
        if ran == 0:
            tal = "탈옥 성공!"
        if ran >= 1:
            tal = "탈옥 실패"
        await message.channel.send(tal)
        

        

    

#노래
"""
@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
"""

client.run(token)
