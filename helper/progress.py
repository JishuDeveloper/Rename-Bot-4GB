import math
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.0) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        filled_blocks = math.floor(percentage / 5)
        empty_blocks = 20 - filled_blocks

        progress_bar = "■" * filled_blocks + "□" * empty_blocks

        tmp = PROGRESS_BAR.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time if estimated_total_time != '' else '0 s',
            progress_bar
        )
        
        cancel_button = InlineKeyboardButton("✖️ Cancel ✖️", callback_data="cancel")

        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",
                reply_markup=InlineKeyboardMarkup([[cancel_button]])
            )
        except Exception:
            pass


def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (str(days) + "d, ") if days else ""
    ) + (
        (str(hours) + "h, ") if hours else ""
    ) + (
        (str(minutes) + "m, ") if minutes else ""
    ) + (
        (str(seconds) + "s, ") if seconds else ""
    ) + (
        (str(milliseconds) + "ms, ") if milliseconds else ""
    )
    return tmp[:-2]


PROGRESS_BAR = """\
{5}

<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
