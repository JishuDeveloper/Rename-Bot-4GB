import time, datetime
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.database import find_one, used_limit
from helper.database import daily as daily_
from datetime import datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.database import daily as daily_
from helper.date import check_expi
from helper.database import uploadlimit, usertype




@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - \
        int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date_.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    user = _newus["usertype"]
    ends = _newus["prexdate"]
    if ends:
        pre_check = check_expi(ends)
        if pre_check == False:
            uploadlimit(message.from_user.id, 2147483652)
            usertype(message.from_user.id, "Free")
    if ends == None:
        text = f"<b>User ID :</b> <code>{message.from_user.id}</code> \n<b>Name :</b> {message.from_user.mention} \n\n<b>🏷 Plan :</b> {user} \n\n✓ Upload 2GB Files \n✓ Daily Upload : {humanbytes(limit)} \n✓ Today Used : {humanbytes(used)} \n✓ Remain : {humanbytes(remain)} \n✓ Timeout : 2 Minutes \n✓ Parallel process : Unlimited \n✓ Time Gap : Yes \n\n<b>Validity :</b> Lifetime"
    else:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text = f"<b>User ID :</b> <code>{message.from_user.id}</code> \n<b>Name :</b> {message.from_user.mention} \n\n<b>🏷 Plan :</b> {user} \n\n✓ High Priority \n✓ Upload 4GB Files \n✓ Daily Upload : {humanbytes(limit)} \n✓ Today Used : {humanbytes(used)} \n✓ Remain : {humanbytes(remain)} \n✓ Timeout : 0 Second \n✓ Parallel process : Unlimited \n✓ Time Gap : Yes \n\n<b>Your Plan Ends On :</b> {normal_date}"

    if user == "Free":
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
    else:
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ Cancel ✖️", callback_data="cancel")]]))





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
