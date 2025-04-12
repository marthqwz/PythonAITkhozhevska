   #https://t.me/PythonAITkhozhevskabot
from googletrans import Translator
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bs4 import BeautifulSoup
import requests

#
translator = Translator()
film_names = []
film_desc = []


def get_film_data():
    url = "https://uaserials.pro/films/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    soup_list_href = soup.find_all('a', {"class": "short-img img-fit"})
    links_list = [href['href'] for href in soup_list_href]

    names = []
    descs = []

    for link in links_list:
        req = requests.get(link)
        soup1 = BeautifulSoup(req.text, features="html.parser")
        name = soup1.find('span', {"class": "oname_ua"})
        desc = soup1.find('ul', {"class": "short-list fx-1"})
        if name and desc:
            names.append(name.text)
            descs.append(desc.text)

    return names, descs


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привіт, {update.effective_user.first_name}!')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not film_names:
        await update.message.reply_text("дані не завантажені. використай /updatefilms.")
        return

    for i in range(len(film_names)):
        text = f"{film_names[i]}\n{film_desc[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("команди:\n/hello\n/film\n/translate <текст>\n/updatefilms")

async def updatefilms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global film_names, film_desc
    await update.message.reply_text("оновлення списку фільмів...")
    film_names, film_desc = get_film_data()
    await update.message.reply_text("список фільмів оновлено!")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = " ".join(context.args)
        translated = translator.translate(text, dest='en')
        await update.message.reply_text(f"переклад: {translated.text}")
    else:
        await update.message.reply_text("введи текст: /translate твій текст")


app = ApplicationBuilder().token("7549089537:AAE2t-FFiRU8G5vDueW81_xVV3kTEx4lPb8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("translate", translate))
app.add_handler(CommandHandler("updatefilms", updatefilms))

app.run_polling()