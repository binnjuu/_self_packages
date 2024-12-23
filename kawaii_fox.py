import time
import sys
import discord
from discord.ext import commands
from discord.ext.commands import Bot

# 開始執行
def start(api_key:str, channel_id:str, message:str, at_user_id:str|None = None):
  """
  向discord指定頻道發送一則訊息,
  api_key: 機器人api key,
  channel_id: 指定頻道id,
  message: 要送出的訊息,

  [可選]at_user_id: 標記一位使用者id
  """
  #client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
  intents=discord.Intents.default()
  intents.message_content = True
  help_command = commands.DefaultHelpCommand(no_category = '指令清單')
  client = commands.Bot(command_prefix="!", intents=intents, )

  @client.event
  #當機器人完成啟動時
  async def on_ready():
    print('目前登入身份：', client.user)
    #遊玩狀態更改
    game = discord.Game("I'm not a Cat!")
    await client.change_presence(status=discord.Status.idle, activity=game)
    
    #發送訊息到特定頻道
    channel = client.get_channel(channel_id)
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S", localtime)

    if at_user_id is not None:
      output_text = f"`[{result}]`\n>> <@>{at_user_id} {message}"
    else:
      output_text = f"`[{result}]`\n>> {message}\n---"

    await channel.send(output_text)

    #關閉程式
    sys.exit(0)

  client.run(api_key)