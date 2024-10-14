from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

bot = Client(
      name="Adult Kingdom",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)


print("Bot was Started")

bot.run()
