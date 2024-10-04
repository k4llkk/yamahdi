# JoKeRUB module for purging unneeded messages(usually spam or ot).
import re
from asyncio import sleep

from telethon.errors import rpcbaseerrors
from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterEmpty,
    InputMessagesFilterGeo,
    InputMessagesFilterGif,
    InputMessagesFilterMusic,
    InputMessagesFilterPhotos,
    InputMessagesFilterRoundVideo,
    InputMessagesFilterUrl,
    InputMessagesFilterVideo,
    InputMessagesFilterVoice,
)

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "utils"

purgelist = {}

purgetype = {
    "ب": InputMessagesFilterVoice,
    "م": InputMessagesFilterDocument,
    "ح": InputMessagesFilterGif,
    "ص": InputMessagesFilterPhotos,
    "l": InputMessagesFilterGeo,
    "غ": InputMessagesFilterMusic,
    "r": InputMessagesFilterRoundVideo,
    "ق": InputMessagesFilterEmpty,
    "ر": InputMessagesFilterUrl,
    "ف": InputMessagesFilterVideo,
    # "ك": search
}

# Other functions...

@l313l.ar_cmd(
    pattern="تنظيف(?:\s|$)([\s\S]*)",
    command=("تنظيف", plugin_category),
    info={
        "header": "لـحذف الـرسائل .",
        "description": "•  Deletes the x(count) amount of messages from the replied message\
        \n•  If you don't use count then deletes all messages from the replied messages\
        \n•  If you haven't replied to any message and used count then deletes recent x messages.\
        \n•  If you haven't replied to any message or havent mentioned any flag or count then doesnt do anything\
        \n•  If flag is used then selects that type of messages else will select all types\
        \n•  You can use multiple flags like -gi 10 (It will delete 10 images and 10 gifs but not 10 messages of combination images and gifs.)\
        ",
        "الاضافه": {
            "البصمات": "لحـذف الرسائل الـصوتية.",
            "الملفات": "لحـذف الملفات.",
            "المتحركه": "لحـذف المتحـركه.",
            "الصور": "لحـذف الـصور",
            "الاغاني": "لحـذف الاغاني",
            "الملصقات": "لحـذف الملصقات",
            "الروابط": "لحـذف الروابط",
            "الفديوهات": "لحـذف الفـيديوهـات",
            "كلمه": " لحذف جميع النصوص التي تحتوي هذه الكلمه في الكروب",
        },
        "ااستخدام": [
            "{tr}تنظيف <الاضافه(optional)> <count(x)> <reply> - to delete x flagged messages after reply",
            "{tr}تنظيف <الاضافه> <رقم> - لحذف رسائل الاضافه",
        ],
        "examples": [
            "{tr}تنظيف 40",
            "{tr}تنظيف -المتحركه 40",
            "{tr}تنظيف -كلمه الجوكر",
        ],
    },
)
async def fastpurger(event):  # sourcery no-metrics
    "To purge messages from the replied message"
    chat = await event.get_input_chat()
    msgs = []
    count = 0
    input_str = event.pattern_match.group(1)
    ptype = re.findall(r"-\w+", input_str)
    try:
        p_type = ptype[0].replace("-", "")
        input_str = input_str.replace(ptype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await event.delete()
    reply = await event.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in purgetype:
                        async for msg in event.client.iter_messages(
                            event.chat_id,
                            limit=int(input_str),  # تعديل هنا
                            offset_id=reply.id - 1,
                            reverse=True,
                            filter=purgetype[ty],
                        ):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await event.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await event.client.delete_messages(chat, msgs)
                    elif ty == "كلمه":
                        error += f"\n᯽︙ الاضافه خـطأ"
                    else:
                        error += f"\n\n᯽︙ `{ty}`  : هـذه أضافـة خاطئـة "
            else:
                count += 1
                async for msg in event.client.iter_messages(
                    event.chat_id,
                    limit=int(input_str),  # تعديل هنا
                    offset_id=reply.id,
                    reverse=True,
                ):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await event.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await event.client.delete_messages(chat, msgs)
        # باقي الكود...
