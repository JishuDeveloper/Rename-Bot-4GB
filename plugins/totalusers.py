from config import *
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
from helper.database import botdata, find_one, total_user,getid
from helper.progress import humanbytes

token = BOT_TOKEN
botid = token.split(':')[0]




@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["users"]))
async def users(client,message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    id = str(getid())
    ids = id.split(',')
    
    await message.reply_text(f"<b>⚡️ Total User :</b> {total_user()}\n\n<b>⚡️ Total Renamed File :</b> {total_rename}\n<b>⚡ Total Size Renamed :</b> {humanbytes(int(total_size))}", quote=True, reply_markup= InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Close 🦋", callback_data="cancel")]])
        )
	
    
    
@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["allids"]))
async def allids(client,message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    id = str(getid())
    ids = id.split(',')
    
    await message.reply_text(f"<b>⚡️ All IDs :</b> {ids}\n\n<b>⚡️ Total User :</b> {total_user()}\n\n<b>⚡️ Total Renamed File :</b> {total_rename}\n<b>⚡ Total Size Renamed :</b> {humanbytes(int(total_size))}", quote=True, reply_markup= InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Close 🦋", callback_data="cancel")]])
        )






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
