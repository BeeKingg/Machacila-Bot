# Coded by Koala
# Recode by @mrismanaziz

import time
from userbot import CMD_HELP, bot
from datetime import datetime
from platform import uname
from time import sleep

from userbot import ALIVE_NAME, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


# Feri Ganteng


@register(outgoing=True, pattern="^.ahping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**NGENTOT!! 🚹**\n**SAYA** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@register(outgoing=True, pattern=r"^\.a(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.j(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**UDIN KEPETOK GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!🔥**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.k(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Kontoll SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**LU SEMUA NGENTOT 🔥**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Salam Dulu Biar Sopan**")
    sleep(2)
    await typew.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


# Owner @mixiologist


@register(outgoing=True, pattern="^.usange(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit(
        "**Informasi Dyno ★**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
        f"-> `Penggunaan Dyno` **{ALIVE_NAME}**:\n"
        f" ❉ **10 Jam - "
        f"51 Menit - 0%**"
        "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
        "-> `Sisa Dyno Bulan Ini`:\n"
        f" ❉ **9989 Jam - 9948 Menit "
        f"- 99%**\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )


CMD_HELP.update({
    "tembelan":
    "⚡list⚡`.tembelan` ;⚡list⚡ `.dino`\
    \nPenjelasan: ntahlah gabut doang.\
    \n\n⚡list⚡`.a`\
    \nPenjelasan: cek sendiru kntl\
    \n\n⚡list⚡`.ass`\
    \nPenjelasan: Cek sendiri kntl.\
    \n\n⚡list⚡`.usange`\
    \nPenjelasan: cekk aja sendiri.\
    \n\n⚡list⚡`.k`\
    \nPenjelasan: Cek sendiri Kntll.\
    \n\n⚡list⚡`.j`\
    \nPenjelasan: Cek sendiri kntll.\
    \n\n⚡list⚡`.ahping`\
    \nPenjelasan: buat ping ah ah."
})
