import asyncio
import io
import json
import logging
import os.path
import re
import sqlite3
import sys
import threading
import traceback
from datetime import datetime
from os import system as cmd
from random import choice as ch

import pytz
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from requests import get
from rubika import Client, handlers, methods, models

# اسکی حرام

# کس ننت اسکی بری 

# ساخته شده توسط CipherX

# Rubika : @CipherX

# Telegram : None


logging.basicConfig(level=logging.ERROR)

db = sqlite3.connect('CipherX.db')

#db.execute('CREATE TABLE Answer (chat_id TEXT, matn TEXT, javab TEXT)')

#                                       #


lock     = []
dontlock = []
enemy    = []
wanted   = []
mute     = []
game     = []
grou     = []
run      = []

#                                       #


async def main():
    #session = stringSession.StringSession()
    #session.insert(auth='auth', guid=None, user_agent=None, phone_number=None)
    async with Client(session='CipherX-SELF') as client:
        @client.on(handlers.MessageUpdates())
        async def self(event):
            text = event.raw_text
            if text == None:
                pass
            else:
                objects = event.object_guid
                guid = event.author_guid
                reply = event.reply_message_id
                admin = await client.get_me()
                admins = admin.user.user_guid
                message_id = event.message.message_id
                if text== ".help" and guid == admins:
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        url2 = get("https://api.codebazan.ir/ping/?url=www.google.com").text
                        help_text = f"""
𝘾𝙞𝙥𝙝𝙚𝙧𝙓-𝘽𝙊𝙏 | {url['result']['time']}

├ • ℍ𝕖𝕝𝕡 ↬ (.help) -> دستورات
├ • 𝕄𝕠𝕕𝕖 ↬ (.mode) -> مود ها
├ • 𝕋𝕠𝕠𝕝𝕤 ↬ (.tools) -> ابزار ها
├ • 𝔼𝕟𝕖𝕞𝕪 ↬ (.enemy) -> حالت دشمن


ᴹᵞ ᴵᴰ @{admin.user.username}

𝑃𝐼𝑁𝐺 ↬ {url2} 𝘔𝘴
"""
                    except:
                        pass
                if text == ".mode" and guid == admins:
                    try:
                        await event.reply("""
• 𝙈𝙤𝙙𝙚 𝙈𝙚𝙣𝙪 •

↬ .time   𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت مود تایم
↬ .tag    𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت هشتگ
↬ .emoje  𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت ایموجی
↬ .emset  𝕠𝕟 - 𝕠𝕗𝕗 ->  ست ایموجی
↬ .lock   𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت قفل پی وی
↬ .copy   𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت متن کپی
↬ .seen   𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت سین خودکار
↬ .text1  𝕠𝕟 - 𝕠𝕗𝕗 -> تکست مود  1
↬ .group  𝕠𝕟 - 𝕠𝕗𝕗 -> مدریت گروه
↬ .text2  𝕠𝕟 - 𝕠𝕗𝕗 -> تکست مود  2
↬ .hyper  𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت هایپر
↬ .Typing 𝕠𝕟 - 𝕠𝕗𝕗 ->  حالت تایپ خودکار
↬ .game   𝕠𝕟 - 𝕠𝕗𝕗 -> بازی ج ح
↬ .timep  𝕠𝕟 - 𝕠𝕗𝕗 -> تایم پروف
========================


""")
                    except:
                        pass
                if text == ".tools" and guid == admins:
                    try:
                        await event.reply("""
• 𝙏𝙤𝙤𝙡𝙨 𝙈𝙚𝙣𝙪 •

↬ .font
↬ .ping
↬ .bio
↬ .getlink
↬ .card
↬ .date
↬ .jok
↬ .pin
↬ .upin
↬ .set
↬ .list
↬ .clear
↬ .lock
↬ .for   | ریپلی
↬ .py    | کد پایتون
↬ .rmute | ریپلی
↬ .dmute | ریپلی
↬ .renemy| ریپیلی
↬ .rdel  | ریپلی
↬ .gad   | افزودن به بازی
↬ .rm    | حذف بازیکن از بازی
↬ .msg   | پیام ادمین
↬ .getlink | دریافت لینک گروه
↬ .deleted | حذف 25 ‌پیام اخیر
↬ .answer | افزودن متن به بات
↬ .delanswer | حذف متن از ربات

=================

🔹HELP ANSWER 🔹


⭕ .answer سلام:چطوری

🔹 سلام به عنوان متنی که کاربر میخواد بگه هست
🔹 و
🔹 چطوری به عنوان جواب ربات
🔹 توی هر گروهی بزنید اونجا متن ثبت میشه



⭕ .delanswer سلام

🔹 متنی که قبلا سیو کردیدو پاک میکنه
🔹 داخل همون گروه بزنید که متنو توش زدید

=================
1 - .font [TEXT]

2 - .ping [SITE] google.com

3 - .bio > Bio Random

4 - .card [NUMBER]

5 - .data > Time and Data

6 - .jok > JOK Random

7 - .pin [REPLY]

8 - .unpin [REPLY]

9 - set > SET Group

10 - .list > Llist On Mode

11 - .clear > Clear All Mode On - Off

12 - lock [ON - OFF]

13 - .for [REPLY] > Forwarded Your Post

14 - .py [CODE python Run]

15 - .rmute > Mute Group is @USERNAME

16 - .dmute > unMute Group is @USERNAME

17 - .renemy > Set (Enemy) is [REPLY]

18 - .rdel > unSet (Enemy) is [REPLY]
                        """)
                    except:
                        pass
                if text == ".enemy" and guid == admins:
                    try:
                        await event.reply("""
• 𝙀𝙣𝙚𝙢𝙮 𝙈𝙚𝙣𝙪 •

↬ .senemy -> افزودن به انمی با ایدی
↬ .renemy -> افزودن به انمی با ریپلی
↬ .rdel -> حذف انمی با ریپلی
↬ .mute -> میوت با ایدی
↬ .delenemy -> حذف انمی با ایدی
↬ .delmute -> حذف میوت با ایدی
                        """)
                    except:
                        pass

    #               [  ENEMY  ]                 #

                if text.startswith(".senemy") and guid == admins:
                    command = text.replace(".senemy","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        enemy.append(us.user.user_guid)
                        await event.reply(f"𝙎𝙚𝙏 𝙀𝙚𝙣𝙚𝙢𝙮\n{command}")
                    except:
                        pass
                if guid in enemy:
                    try:
                        with open('Enemy/Fosh', 'r') as foshE:
                            ask = ch(foshE.readlines()).strip()
                            await event.reply(ask)
                    except:
                        pass
                if text.startswith(".delenemy") and guid == admins:
                    command = text.replace(".delenemy","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        enemy.remove(us.user.user_guid)
                        await event.reply(f"𝙀𝙣𝙚𝙢𝙮 𝘿𝙚𝙡𝙚𝙏𝙚𝘿\n{command}")
                    except:
                        await event.reply(f"𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 𝙉𝙤𝙩 𝙁𝙞𝙣𝙙\n{command}")
                if text.startswith(".renemy") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        enemy.append(us.user.user_guid)
                        await event.reply(f"𝙎𝙚𝙏 𝙀𝙚𝙣𝙚𝙢𝙮\n@{us.user.username}")
                    except:
                        pass
                if text.startswith(".rdel") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        enemy.remove(us.user.user_guid)
                        await event.reply(f"𝙀𝙣𝙚𝙢𝙮 𝘿𝙚𝙡𝙚𝙏𝙚𝘿\n@{us.user.username}")
                    except:
                        await event.reply(f"𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 𝙉𝙤𝙩 𝙁𝙞𝙣𝙙\n@{us.user.username}")


            #       [ MODE ]     #

                if os.path.exists("Mode/Bold"):
                    mode = open("Mode/Bold").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"**{text}**") # BOLD MODE
                    except:
                        pass
                if text.startswith(".bold") and guid == admins:
                    command = text.replace(".bold","").strip()
                    if command == "on" or "off":
                        open("Mode/Bold","w").write(command)
                        await event.edit(f"**BOLD** 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Hyper"):
                    mode = open("Mode/Hyper").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "Group":
                            if event.message.reply_to_message_id:
                                us = await client(methods.messages.GetMessagesByID(objects,message_ids=event.message.reply_to_message_id))
                                await event.edit(f"[{text}]({us.messages[0].author_object_guid})")
                            else:
                                await event.edit(f"[{text}]({guid})")
                    except:
                        pass
                if text.startswith(".hyper") and event.type == "Group" and guid == admins:
                    command = text.replace(".hyper","").strip()
                    if command == "on" or "off":
                        open("Mode/Hyper","w").write(command)
                        await event.edit(f"[HyperS]({guid}) 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/copy"):
                    mode = open("Mode/copy").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"`{text}`")
                    except:
                        pass
                if text.startswith(".copy") and guid == admins:
                    command = text.replace(".copy","").strip()
                    if command == "on" or "off":
                        open("Mode/copy","w").write(command)
                        await event.edit(f"`CopyEs` 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Typing"):
                    mode = open("Mode/Typing").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if text:
                            await client(methods.chats.SendChatActivity(objects))
                    except:
                        pass
                if text.startswith(".typing") and guid == admins:
                    command = text.replace(".typing","").strip()
                    if command == "on" or "off":
                        open("Mode/Typing","w").write(command)
                        await event.edit(f"**Typing** 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/TIME"):
                    mode = open("Mode/TIME").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.edit(f"~> {url['result']['time']} <~ \n{text}")
                    except:
                        pass

                if text.startswith(".time") and guid == admins:
                    command = text.replace(".time","").strip()
                    if command == "on" or "off":
                        open("Mode/TIME","w").write(command)
                        await event.edit(f"**TIME** 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Tags"):
                    mode = open("Mode/Tags").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        texts = re.sub(" ","_",text)
                        await event.edit(f"#{texts}")
                    except:
                        pass

                if text.startswith(".tag") and guid == admins:
                    command = text.replace(".tag","").strip()
                    if command == "on" or "off":
                        open("Mode/Tags","w").write(command)
                        await event.edit(f"#TAGS 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Emoje"):
                    mode = open("Mode/Emoje").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        items = open("Mode/SetEm").read()
                        await event.edit(f"{text} {items}")
                    except:
                        pass
                if text.startswith(".emoje") and guid == admins:
                    command = text.replace(".emoje","").strip()
                    if command == "on" or "off":
                        open("Mode/Emoje","w").write(command)
                        await event.edit(f"**EMOJES**😐🗿 𝙈𝙤𝙙𝙚 {command}")
                if text.startswith(".emset"):
                    command = text.replace(".emset", "")
                    open("Mode/SetEm","w").write(command)
                    await event.edit(f"𝙀𝙢𝙤𝙅𝙚𝙨 𝙎𝙚𝙏 {command}")

                if os.path.exists("Mode/:)"):
                    mode = open("Mode/:)").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"{text} `:)`")
                    except:
                        pass
                if text.startswith(".text1") and guid == admins:
                    command = text.replace(".text1","").strip()
                    if command == "on" or "off":
                        open("Mode/:)","w").write(command)
                        await event.edit(f":) 𝙈𝙤𝙙𝙚 {command}")
                if os.path.exists("Mode/Seen"):
                    mode = open("Mode/Seen").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "User" or event.type == "Group":
                            try:
                                await event.seen()
                            except:
                                pass
                    except:
                        pass
                if text.startswith(".seen") and guid == admins:
                    command = text.replace(".seen","").strip()
                    if command == "on" or "off":
                        open("Mode/Seen","w").write(command)
                        await event.edit(f"**SEEN** 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Game"):
                    mode = open("Mode/Game").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        if event.type == "Group":
                            try:
                                if event.object_guid in grou:
                                    if text == "بپرس":
                                        print(f"{objects} => {text}")
                                        if guid in game:
                                            with open('game.txt', 'r') as games:
                                                ask = ch(games.readlines()).strip()
                                                await event.reply(ask)
                            except:
                                pass
                    except:
                        pass
                if text.startswith(".game") and guid == admins:
                    command = text.replace(".game","").strip()
                    if command == "on" or "off":
                        open("Mode/Game","w").write(command)
                        await event.edit(f"**GAMES** 𝙈𝙤𝙙𝙚 {command}")

                if text == ".gad" and guid == admins:
                    try:
                        grou.append(objects)
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        game.append(us.user.user_guid)
                        await event.delete_messages()
                        await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› به بازی اضافه شد

برای پرسش از کلمه ( بپرس ) استفاده کنید
    """,reply_to_message_id=event.message.reply_to_message_id))
                    except:
                        pass

                if text == ".rm" and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        game.remove(us.user.user_guid)
                        await event.delete_messages()
                        await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› از بازی حذف شد
    """,reply_to_message_id=event.message.reply_to_message_id))
                    except:
                        pass

                if text.startswith("کی کونیه") and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"این [ {name}]({random.member_guid}) کونیه 🚶‍♂️😂")

                    except:
                        pass

                if text.startswith("کی خره") and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"این [ {name}]({random.member_guid}) خره 😂😐")

                    except:
                        pass
                if text == "کی با کی رل میزنه" or text == "کیا رل میزنن" or text == "کی با کی رل میزنع" or text == "کی باع کی رل میزنع" and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        for i in range(2):
                            random = ch(dialogs.in_chat_members)
                            random1 = ch(dialogs.in_chat_members)
                            name = random.first_name
                            name1 = random1.first_name
                        if name == name1:
                            await event.delete_messages()
                        else:
                            await event.reply(f"""
این [ {name}]({random.member_guid})

با این [ {name1}]({random1.member_guid})

رل میزنه ❤️🗿
                        """)
                    except:
                        pass

                if text == "کی کیو میکنه" or text == "کی میکنه" or text == "کی اون یکیو میکنه" or text == "کی کیو میکنع" and guid == admins:
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        for i in range(2):
                            random = ch(dialogs.in_chat_members)
                            random1 = ch(dialogs.in_chat_members)
                            name = random.first_name
                            name1 = random1.first_name
                        if name == name1:
                            await event.delete_messages()
                        else:
                            await event.reply(f"""
این [ {name}]({random.member_guid})

اینو میکنه [ {name1}]({random1.member_guid}) 💦

                        """)
                    except:
                        pass

                if text == "کی بام رل میزنه" or text == "کی باهام رل میزنع" or text == "کی باهام رل میزنه" or text == "کی رل میزنه" or text == "کی بام رل میزنع":
                    try:
                        dialogs = await client(methods.groups.GetGroupAllMembers(group_guid= event.object_guid ,search_text=None, start_id=None))
                        random = ch(dialogs.in_chat_members)
                        name = random.first_name
                        await event.reply(f"این [ {name}]({random.member_guid}) باهات رل میزنه")
                    except:
                        pass

                if os.path.exists("Mode/text2"):
                    mode = open("Mode/text2").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        await event.edit(f"{text} `:/`")
                    except:
                        pass
                if text.startswith(".text2") and guid == admins:
                    command = text.replace(".text2","").strip()
                    if command == "on" or "off":
                        open("Mode/text2","w").write(command)
                        await event.edit(f":/ 𝙈𝙤𝙙𝙚 {command}")

                if os.path.exists("Mode/Lock"):
                    mode = open("Mode/Lock").read()
                else:
                    mode = "off"
                if mode == "on":
                    if event.type == "User" and not guid == admins:
                        salm = dontlock.count(event.object_guid)
                        if salm == 1:
                            pass
                        else:
                            lock.append(event.object_guid)
                            us = await client(methods.users.GetUserInfo(event.object_guid))
                            t = lock.count(event.object_guid)
                            if t == 1:
                                await event.reply(f"• 𝘾𝙞𝙥𝙝𝙚𝙧𝙓-𝘽𝙊𝙏 •\nاخطار (1/5) ❌\n\nکاربر @{us.user.username}\nاز ارسال پیام خودداری کنید. در غیر این صورت شما بلاک خواهید شد.")
                            if t == 2:
                                await event.reply(f"• 𝘾𝙞𝙥𝙝𝙚𝙧𝙓-𝘽𝙊𝙏 •\nاخطار (2/5) ❌\n\nکاربر @{us.user.username}\nاز ارسال پیام خودداری کنید. در غیر این صورت شما بلاک خواهید شد.")
                            if t == 3:
                                await event.reply(f"• 𝘾𝙞𝙥𝙝𝙚𝙧𝙓-𝘽𝙊𝙏 •\nاخطار (3/5) ❌\n\nکاربر @{us.user.username}\nاز ارسال پیام خودداری کنید. در غیر این صورت شما بلاک خواهید شد.")
                            if t == 4:
                                await event.reply(f"• 𝘾𝙞𝙥𝙝𝙚𝙧𝙓-𝘽𝙊𝙏 •\nاخطار (4/5) ❌\n\nکاربر @{us.user.username}\nاز ارسال پیام خودداری کنید. در غیر این صورت شما بلاک خواهید شد.")
                            if t == 5:
                                await event.reply(f"کاربر @{us.user.username}\nبه دلیل ارسال پیام مکرر بلاک شد.")
                                await client(methods.users.SetBlockUser(event.object_guid))
                if text.startswith(".lock") and guid == admins:
                    command = text.replace(".lock","").strip()
                    if command == "on" or "off":
                        open("Mode/Lock","w").write(command)
                        await event.edit(f"**LOCK** 𝙈𝙤𝙙𝙚 {command}")
                if text.startswith("Unlock") and guid == admins:
                    try:
                        dontlock.append(objects)
                        us = await client(methods.users.GetUserInfo(objects))
                        await event.edit(f"کاربر [ @{us.user.username} ]\nمیتوانید پیام ارسال کنید .")
                    except:
                        pass
                if text.startswith("Lock") and guid == admins:
                    try:
                        dontlock.remove(objects)
                        await event.delete_messages()
                    except:
                        pass
                if text.startswith(f"@{admin.user.username}") and event.type == "Group":
                    try:
                        await event.reply(f"[Bal ?]({guid})")
                        await client(methods.messages.ForwardMessages(objects, admin.user.user_guid, message_ids=event.message_id))
                    except:
                        pass

    #           [ Group ]       #


                if text.startswith(".set") and guid == admins:
                    try:
                        open("Mode/Set","w").write(event.object_guid)
                        await event.edit("𝙂𝙧𝙤𝙪𝙥 𝙎𝙚𝙏 𝙏𝙤𝙤𝙡𝙨 ✔️")
                    except:
                        pass

                if text.startswith(".group") and guid == admins:
                    try:
                        command = text.replace(".group","").strip()
                        open("Mode/Group","w").write(command)
                        await event.edit(f"𝙂𝙧𝙤𝙪𝙥 𝙈𝙤𝘿𝙚 {command}")
                    except:
                        pass
                if os.path.exists("Mode/Group"):
                    mode = open("Mode/Group").read()
                else:
                    mode = "off"
                if mode == "on":
                    try:
                        chat_id = open("Mode/Set").read()
                        if objects == chat_id:

                            if event.find_keys(keys=['event_data']):
                                try:
                                    if event.message.event_data.type == "RemoveGroupMembers":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
کاربر [ {us.user.first_name}]({us.user.user_guid})
از گروه بن شد .
    """)
                                    if event.message.event_data.type == "AddedGroupMembers":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        groups = await client(methods.groups.GetGroupInfo(event.object_guid))
                                        #print(group.jsonify(indent=2))
                                        await event.reply(f"""
کاربر [ {us.user.first_name}]({us.user.user_guid})
به گروه ما خوش اومدی .
    """)
                                    if event.message.event_data.type == "LeaveGroup":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
داش [{us.user.first_name}]({us.user.user_guid})
ب کیرم ک لف دادی :/
                                        """)
                                    if event.message.event_data.type == "JoinedGroupByLink":
                                        us = await client(methods.users.GetUserInfo(event.peer_objects[0].object_guid))
                                        await event.reply(f"""
کاربر [{us.user.first_name}]({us.user.user_guid})
به گروه ما خوش اومدی .

                                        """)
                                except:
                                    pass
                            g = re.findall(r"https://rubika.ir/joing/\w{32}",text)
                            for gr in g:
                                await event.delete_messages()
                            c = re.findall(r"https://rubika.ir/joinc/\w{32}",text)
                            for cr in c:
                                await event.delete_messages()
                    except:
                        pass

                if text.startswith("اخطار") and event.type == "Group" and guid == admins:
                    try:

                        command = text.replace("اخطار","").strip()
                        await event.delete_messages()
                        info = await client(methods.messages.GetMessagesByID(objects,event.message.reply_to_message_id))
                        us = await client(methods.users.GetUserInfo(info.author_object_guid))
                        wanted.append(us.user.user_guid)
                        total = wanted.count(us.user.user_guid)
                        if total == 1:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› دلیل : {command}


››› شما [ 1/3 ] اخطار دریافت کردید.
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 2:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› دلیل : {command}


››› شما [ 2/3 ] اخطار دریافت کردید.
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 3:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› دلیل : {command}


››› شما [ 3/3 ] اخطار دریافت کردید.

›››› به دلیل دریافت [ 3 ] اخطار میوت میشوید
    """,reply_to_message_id=event.message.reply_to_message_id))
                                mute.append(us.user.user_guid)
                            except:
                                pass
                    except:
                        pass
                if text.startswith("حذف اخطار") and guid == admins:
                    try:
                        info = await client(methods.messages.GetMessagesByID(objects,event.message.reply_to_message_id))
                        us = await client(methods.users.GetUserInfo(info.author_object_guid))
                        wanted.remove(us.user.user_guid)
                        total = wanted.count(us.user.user_guid)

                        if total == 0:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› اخطار های شما [ 0/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 1:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› اخطار های شما [ 1/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 2:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› اخطار های شما [ 2/3 ]
    """,reply_to_message_id=event.message.reply_to_message_id))
                            except:
                                pass
                        if total == 3:
                            try:
                                await client(methods.messages.SendMessage(objects,message=f"""
› کاربر [ {us.user.first_name}]({us.user.user_guid})

›› اخطار های شما [ 3/3 ]

››› به همین دلیل شما اخراج میشوید .
    """,reply_to_message_id=event.message.reply_to_message_id))

                            except:
                                pass
                    except:
                        pass
                if text.startswith(".mute ") and guid == admins:
                    command = text.replace(".mute","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        mute.append(us.user.user_guid)
                        await event.reply(f"𝙈𝙪𝙏𝙚 𝙎𝙚𝙏\n{command}")
                    except:
                        pass
                if guid in mute:
                    try:
                        if event.type == "Group":
                            us = await client(methods.users.GetUserInfo(event.message.author_object_guid))
                            await event.delete_messages()
                            print(f"{us.user.first_name} \033[32mPAK \033[35mSHOD => \033[31m {text}")
                    except:
                        pass
                if text.startswith(".delmute ") and guid == admins:
                    command = text.replace(".delmute ","").strip()
                    try:
                        ids = command.replace("@","").strip()
                        us = await client(methods.extras.GetObjectByUsername(ids))
                        mute.remove(us.user.user_guid)
                        await event.reply(f"𝙈𝙪𝙏𝙚 𝘿𝙚𝙡𝙚𝙏𝙚𝘿\n{command}")
                    except:
                        pass
                if text.startswith(".rmute") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        mute.append(us.user.user_guid)
                        await event.reply(f"𝙈𝙪𝙏𝙚 𝙎𝙚𝙏\n@{us.user.username}")
                    except:
                        pass
                if text.startswith(".rdmute") and guid == admins:
                    try:
                        ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                        us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                        mute.remove(us.user.user_guid)
                        await event.reply(f"𝙈𝙪𝙏𝙚 𝘿𝙚𝙡𝙚𝙏𝙚𝘿\n@{us.user.username}")
                    except:
                        pass


    #               [ TOOLS ]         #


                if text.startswith("اد") and guid == admins:
                    try:
                        if event.type == "Group":
                            ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                            us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                            await client(methods.groups.SetGroupAdmin(objects,us.user.user_guid,access_list=['PinMessages','DeleteGlobalAllMessages']))
                            await event.reply(f"[ {us.user.first_name}]({us.user.user_guid}) اد شدی 🌖💫")
                    except:
                        pass

                if text.startswith(".id") and guid == admins:
                    try:
                        if event.type == "Group":
                            ids = await client(methods.messages.GetMessagesByID(objects,message_ids=reply))
                            us = await client(methods.users.GetUserInfo(ids.author_object_guid))
                            await event.edit(f"`{us.user.user_guid}`\n[ {us.user.first_name}]({us.user.user_guid})")
                        if event.type == "User":
                            us = await client(methods.users.GetUserInfo(objects))
                            await event.edit(f'`{us.user.user_guid}`')
                    except:
                        pass

                if text.startswith(".getlink") and guid == admins:
                    try:
                        if event.type == "Group":
                            links = await client(methods.groups.GetGroupLink(objects))
                            await event.reply(f"""
لینک گروه 🌖💫

**LINKS** {links.join_link}
    """)
                    except:
                        pass

                if text.startswith(".info") and guid == admins:
                    try:
                        groups = await client(methods.groups.GetGroupInfo(objects))
                        if groups.group.event_messages == True:
                            texts = "Yes"
                        else:
                            texts = "No"
                        await event.edit(f"""
• 𝔊𝔯𝔬𝔲𝔓 𝔇𝔞𝔱𝔞 •

ℕ𝕒𝕄𝕖: {groups.group.group_title}
𝕄𝕖𝕞𝕓𝕖𝕣𝕤: {groups.group.count_members}
𝔻𝕖𝕤𝕔𝕣𝕚𝕡𝕥𝕚𝕠𝕟: {groups.group.description}
𝕋𝕖𝕩𝕥 𝔻𝕠𝕟𝕥 𝕊𝕖𝕖𝕟: {groups.chat.count_unseen}
𝔸𝕔𝕔𝕖𝕤𝕤 𝕄𝕖𝕤𝕤𝕒𝕘𝕖: {texts}
𝕊𝕝𝕠𝕨 𝕄𝕠𝕕𝕖: {groups.group.slow_mode}s
    """)
                    except:
                        pass
                if text.startswith(".ping") and guid == admins:
                    try:
                        ping = get(f"https://api.codebazan.ir/ping/?url=www.{text.replace('.ping ','').strip()}").text
                        await event.edit(f"𝙋𝙞𝙣𝙂𝙨 𝙎𝙞𝙏𝙚 : {ping}𝗠𝘀")
                    except:
                        pass
                if text.startswith(".bio") and guid == admins:
                    try:
                        url = get("https://api.codebazan.ir/bio/").text
                        await event.edit(f"• 𝘽𝙞𝙤 𝙍𝙖𝙣𝘿𝙤𝙢 • \n{url}")
                    except:
                        pass

                if text.startswith(".font ") and guid == admins:
                    try:
                        url = get(f"https://api.codebazan.ir/font/?text={text.replace('.font','')}").json()
                        await event.edit(f"\n".join(list(url["result"].values())[:110]))
                    except:
                        pass
                if text.startswith(".date") and guid == admins:
                    try:
                        url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
                        await event.edit(f"""
• 𝔗𝔦𝔐𝔢𝔖 𝔇𝔞𝔗𝔢 •

𝕋𝕚𝕞𝔼𝕤: {url['result']['time']}
𝔻𝕒𝕋𝕖: {url['result']['date']}
𝔽𝕒𝕤𝕝: {url['result']['fasl']}
𝕄𝕒𝕙: {url['result']['mahname']}
𝕎𝕖𝕖𝕜ℕ𝕒𝕞𝕖: {url['result']['weekname']}

                    """)
                    except:
                        pass
                if text.startswith(".list") and guid == admins:
                    try:
                        hyper = open("Mode/Hyper").read()
                        copy  = open("Mode/copy").read()
                        Group = open("Mode/Group").read()
                        Lock  = open("Mode/Lock").read()
                        Tags  = open("Mode/Tags").read()
                        Text2 = open("Mode/text2").read()
                        TIME  = open("Mode/TIME").read()
                        Bold  = open("Mode/Bold").read()
                        seens = open("Mode/Seen").read()
                        games = open("Mode/Game").read()

                        tping = open("Mode/Typing").read()
                        await event.edit(f"""
• 𝗠𝗲𝗻𝘂 𝗟𝗶𝘀𝘁 •

𝙷𝚢𝚙𝚎𝚛: {hyper}
𝙲𝚘𝚙𝚢: {copy}
𝙶𝚛𝚘𝚞𝚙: {Group}
𝙻𝚘𝚌𝚔: {Lock}
𝚃𝚊𝚐𝚜: {Tags}
𝚃𝚎𝚡𝚝𝟸: {Text2}
𝚃𝚒𝙼𝚎: {TIME}
𝙱𝚘𝚕𝚍: {Bold}
**SEEN**: {seens}
**Typing**: {tping}
    """)
                    except:
                        pass
                if text.startswith(".clear"):
                    try:
                        hyper = open("Mode/Hyper","w").write("off")
                        copy  = open("Mode/copy","w").write("off")
                        Group = open("Mode/Group","w").write("off")
                        Lock  = open("Mode/Lock","w").write("off")
                        Tags  = open("Mode/Tags","w").write("off")
                        Text2 = open("Mode/text2","w").write("off")
                        TIME  = open("Mode/TIME","w").write("off")
                        Bold  = open("Mode/Bold","w").write("off")
                        seens = open("Mode/Seen","w").write("off")
                        games = open("Mode/Game","w").write("off")
                        tping = open("Mode/Typing","w").write("off")
                        await event.edit(f"""
• Clear All Methods CIPHER-X


• Successfully •

• 𝗠𝗲𝗻𝘂 •

𝙷𝚢𝚙𝚎𝚛: off
𝙲𝚘𝚙𝚢: off
𝙶𝚛𝚘𝚞𝚙: off
𝙻𝚘𝚌𝚔: off
𝚃𝚊𝚐𝚜: off
𝚃𝚎𝚡𝚝𝟸: off
𝚃𝚒𝙼𝚎: off
𝙱𝚘𝚕𝚍: off
**SEEN**: off
**Typing**: off
""")

                    except:
                        pass
                if text.startswith(".for"):
                    dialogs = await client(methods.chats.GetChats(start_id=None))
                    if dialogs.chats:
                        total = len(dialogs.chats)
                        successful = 0
                        unsuccessful = 0
                        message = await event.reply(f'تعداد {total} چت پیدا شد شروع فرایند ارسال ...')
                        for index, dialog in enumerate(dialogs.chats, start=1):
                            if methods.groups.SendMessages in dialog.access:
                                try:
                                    if event.type == "Group" or event.type == "User":
                                        await event.forwards(dialog.object_guid, message_ids=event.reply_message_id)
                                        successful += 1

                                except Exception:
                                    unsuccessful += 1

                                progress = '|'
                                filled = int(index * 15 / total)
                                progress += '█' * filled
                                progress += '-' * (15 - filled)
                                progress += '| ▅▃▁'
                                progress += f' [{int(index * 100 / total):,}%]'

                                await message.edit(
                                    f'تعداد {index:,} چت از {total:,} چت بررسی شده است'
                                    f'\nموفق : {successful:,}\nناموفق: {unsuccessful:,}\n\n{progress}'
                                )
                    else:
                        await event.reply('در جستجوی چت ها با شکست مواجعه شد')
                if text.startswith(".run") and guid == admins:
                    try:
                        run.append(objects)
                        await event.reply(event)

                    except:
                        print("ERR line 958")
                if objects in run:
                    try:
                        print(event)
                    except:
                        print("ERR")
                if text.startswith(".sid"):
                    command = text.replace(".sid","").strip()
                    await client(methods.settings.UpdateUsername(username=command))
                    await event.reply(f"**SET Your ID** -> `{command}`")

                if text.startswith(".py") and guid == admins:
                    Code = text.replace(".py\n","")
                    old_stderr = sys.stderr
                    old_stdout = sys.stdout
                    redirected_output = sys.stdout = io.StringIO()
                    redirected_error = sys.stderr = io.StringIO()
                    stdout, stderr, exc = None, None, None
                    async def aexec(code, event):
                        exec(
                        f"async def __aexec(event, client): "
                        + "\n chatid = event.object_guid"
                        + "".join(f"\n {l}" for l in code.split("\n")),
                        )
                        return await locals()['__aexec'](event,client)
                    try:
                        returned = await aexec(Code,event)
                    except Exception:
                        exc = traceback.format_exc()
                    stdout = redirected_output.getvalue().strip()
                    stderr = redirected_error.getvalue().strip()
                    sys.stdout = old_stdout
                    sys.stderr = old_stderr
                    evaluation = exc or stderr or stdout or returned
                    try:
                        if evaluation:
                            await event.edit("**Query**🔹 \n\n"
                            f"{Code}\n"
                            "\n**Result** 🔺 \n\n"
                            f"{evaluation}"
                            "")
                        else:
                            await event.edit("**Query**:\n\n"
                            f"{Code}"
                            "\nResult: \nNo Result Returned/False")
                    except Exception as err:
                        await event.edit("**Query** 🔷\n"
                        f"{Code}"
                        "\nException 🔺\n"
                        f"{err}")
                if text.startswith(".answer") and guid == admins:
                    try:
                        command = text.replace(".answer", "").strip()
                        MyA = command.split(":")
                        db.execute('INSERT INTO Answer (chat_id, matn, javab) VALUES (?, ?, ?)', (event.object_guid, MyA[0], MyA[1]))
                        db.commit()
                        await event.reply(f'🔹 متن جدید با موفقیت افزوده شد 🔹\n🔺 متن :‌ {MyA[0]}\n🔺 جواب : {MyA[1]}')
                    except:
                        pass
                data_Answer = db.execute('SELECT * FROM Answer').fetchall()
                for OyA in data_Answer:
                    if text == OyA[1] and event.object_guid in OyA[0]:
                        if event.type == "Group" and not guid == admins:
                            await event.reply(OyA[2])


                if text.startswith('.delanswer') and guid == admins:
                    try:
                        command = text.replace(".delanswer", "")
                        db.execute(f'DELETE from Answer WHERE matn = "%s" ' %command)
                        db.commit()
                        await event.reply("🔹 کلمه مورد نظر پاک شد 🔹")
                    except:
                        pass
                if text.startswith('.listanswer') and guid == admins:
                    try:
                        Lists = db.execute('SELECT * FROM Answer').fetchall()
                        for LiA in Lists:
                            matn = LiA[1]
                            javab = LiA[2]
                            await event.edit(f'🔹 لیست پاسخ ها 🔹\n\nمتن : {matn}\nجواب : {javab}')
                    except:
                        pass
                if text.startswith(".Shot") and guid == admins:
                    try:
                        command = text.replace(".Shot", "")
                        await client.sendImage(event.object_guid, url=f'https://api.otherapi.tk/carbon?type=create&code={command}')
                    except:
                        pass
                if text.startswith('.deleted') and guid == admins:
                    try:
                        message_ids_dele = await client(methods.messages.GetMessages(event.object_guid, sort='FromMax',min_id=None, max_id=None, type=None))
                        for item_deleted in message_ids_dele.messages:
                            await client(methods.messages.DeleteMessages(event.object_guid, message_ids=item_deleted.message_id))
                        await event.reply('🔹 %s پیام اخیر پاک شد 🔹' %25)
                    except:
                        pass
                if text.startswith('.msg') and guid == admins:
                    try:
                        site = get('http://cipherx0991505.blogfa.com/post/2')
                        soup = BeautifulSoup(site.content, 'html.parser')
                        matn = soup.find('div', {'class':'postcontent'})
                        textApp = matn.find('p').text
                        await event.reply(f'🔹 مسیج ادمین 🔹\n\n🔰 {textApp}')
                        open('Mode/Status', 'w').write(textApp)
                    except:
                        pass

                if text.startswith('.prof') and guid == admins:
                    try:
                        open('Image/TimeOn', 'w').write(text.replace('.prof', '').strip())
                        await event.edit(f"**TIME PROFILE** __{text.replace('.prof', '')}__")
                    except:
                        pass
                if os.path.exists('Image/TimeOn'):
                    mode = open('Image/TimeOn').read()
                else:
                    mode = 'off'
                if mode == 'on':
                    ir = pytz.timezone("Asia/Tehran")
                    time = f"""{datetime.now(ir).strftime("%H:%M")}"""
                    if os.path.exists('Image/Time'):
                        time_old = open('Image/Time').read()
                    if time_old == time:
                        pass
                    else:
                        open('Image/Time', 'w').write(time)
                        font = ImageFont.truetype(f"Image/digital.ttf", 199)
                        img = Image.open('Image/time.jpg')
                        draw = ImageDraw.Draw(img)
                        draw.text((130, 480),f"~~ {time} ~~", font=font)
                        img.save('Image/timeLock.jpg')
                        file = await client.upload(file='Image/timeLock.jpg')
                        file_id = file.file_id
                        c = await client(methods.chats.GetAvatars(admins))
                        avatar_id = c.avatars[0].avatar_id
                        await client(methods.chats.DeleteAvatar(admins, avatar_id))
                        await client(methods.chats.UploadAvatar(admins, main_file_id=file_id, thumbnail_file_id=file_id))
                else:
                    pass
        await client.run_until_disconnected()

asyncio.run(main())
