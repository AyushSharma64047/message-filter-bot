# (c) @AbirHasan2005
# I just made this for searching a channel message from inline.
# Maybe you can use this for something else.
# I first made this for @AHListBot ...
# Edit according to your use.
# Edited to take all queries in incoming message, not in inline by @xendaddy

from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(
        "Hi, I can search messages for you! \n\nJust send me some keywords!")


@Bot.on_message(filters.incoming)
async def message_handler(_, event: Message):
    if event.text == '/start':
        return
    answers = 'Results: \n\n'
#     # If Search Query is Empty
#     if event.text == "":
#         await event.answer('')
#         answers.append(
#             InlineQueryResultArticle(
#                 title="This is Inline Messages Search Bot!",
#                 description="You can search Channel All Messages using this bot.",
#                 input_message_content=InputTextMessageContent(
#                     message_text="Using this Bot you can Search a Channel All Messages using this bot.\n\n"
#                                  "Made by @Z_Harbour_bot",
#                     disable_web_page_preview=True
#                 ),
#                 reply_markup=InlineKeyboardMarkup([
#                     [InlineKeyboardButton("Search Here", switch_inline_query_current_chat="")],
#                     [InlineKeyboardButton("Support Group", url="https://t.me/z_harbour"),
#                      InlineKeyboardButton("Bots Channel", url="https://t.me/z_harbour")],
#                     [InlineKeyboardButton("Developer - @Z_Harbour_bot", url="https://t.me/Z_Harbour_bot")]
#                 ])
#             )
#         )
#     # Search Channel Message using Search Query Words
#     else:
    async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):
        if message.text:
            answers += "- `{}` \n".format(message.text.split("\n", 1)[0])
#                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
#                 input_message_content=InputTextMessageContent(
#                     message_text=message.text.markdown,
#                     parse_mode="markdown",
#                     disable_web_page_preview=True
#                 )
#             ))
    try:
        await event.reply_text(answers)
        print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
