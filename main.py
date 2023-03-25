import telebot
import requests
id = 2
API = "http://194.87.23.99:12332/api/Books/ "
API_KEY = "6091755530:AAF7Gdxl-x3Hms5gy-6xV2VBkFj4Yqxu_-s"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler()
def ping(message):

  if message.text == "/ping" :

    bot.reply_to(message, "کد اشتراک را وارد کنید")
    message.text == 0
  print(message.text)
  if message.text != "/ping":

    sh = (message.text)
    print(sh)
    print(type(sh))
    if sh == "2":
      info(message, sh)
    else:
      bot.send_message(message.chat.id, "کد وارد شده صجیج نیست")



def info(message,sh):
  print("kelash rosi \nbomb shimiai")
  API_URL = API + sh
  print(API_URL)
  response = requests.get(API_URL)
  API_DATA = response.json()
  id = API_DATA['id']
  liter = API_DATA['liter']
  status = API_DATA['status']
  bat = API_DATA['bat']
  online = ""
  matn  = f"اطلاعات شما به صورت زیر است----> \n با شماره اشتراک دستگاه:  {id} \n مقدار اب مصرفی تا کنون به لیتر: {liter}\n مقدار اخرین وضیعت شارژ باطری: {bat}\n وضیعت روشن یا خاموش بودن دستگاه  : {status}"
  if status == True :
    online == "online"
  else :
    online == "ofline"


   # description = API_DATA['description']
  bot.send_message(message.chat.id,matn)
  print(online)






@bot.message_handler()
def greet(message):
  bot.send_message(message.chat.id, message.text)
bot.polling()


