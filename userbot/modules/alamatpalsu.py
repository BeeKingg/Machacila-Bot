import json
import urllib.request


from userbot.events import register
from userbot import CMD_HELP


# Port By @VckyouuBitch From GeezProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    result["type"]
    resut["country_code"]
    result["region_name"]
    result["city"]
    result["zip"]
    result["latitude"]
    result["longitude"]
    await event.edit(
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{king1}</code>\n<b>Country code:- </b> <code>{king2}</code>\n<b>State name :-</b><code>{king3}</code>\n<b>City name :- </b><code>{king4}</code>\n<b>zip :-</b><code>{king5}</code>\n<b>Latitude:- </b> <code>{king6}</code>\n<b>Longitude :- </b><code>{king7}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update({
    "alamatpalsu":
    "•CMD: `.ip`\
    \n•Penjelasan: Memberikan detail tentang alamat ip."


})
