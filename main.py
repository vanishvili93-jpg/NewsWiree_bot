import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://infodevelop.top/click?key=0027c57b554345b8a59d1b4496c31d31", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Las", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Las nu", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Las nu", url="https://infodevelop.top/click?key=0027c57b554345b8a59d1b4496c31d31")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("📰 *Valkommen till Dagens Lasning.*\n\n"
        "Varje dag ett urval av kultur, "
        "resor, mat, vetenskap och teknik "
        "— att lasa i lugn och ro i chatten.\n\n"
        "Tryck pa *Dagens amnen* "
        "for att borja.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Kultur — hoststallningar", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Mat — svenska recept", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Resor — fem gomda byar", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("📋 *Dagens amnen*\n\n"
        "Tre lasningar valda for idag. "
        "Var och en komplett i chatten.\n\n"
        "*Kultur* — hoststallningar: fem "
        "viktiga utstellningar pa svenska museer.\n\n"
        "*Mat* — svenska klassiker: fyra "
        "traditionella recept.\n\n"
        "*Resor* — fem gomda svenska byar "
        "for en hosthelg.\n\n"
        "Tryck pa en rubrik for att oppna artikeln.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("🎨 *Hoststallningar: fem viktiga "
        "utstellningar pa svenska museer*\n\n"
        "Museerna oppnar den nya sasongen.\n\n"
        "*Stockholm — Moderna Museet*\n"
        "En stor retrospektiv av svensk "
        "modernism. Sallsynta verk fran "
        "privata samlingar och opublicerat "
        "arkivmaterial.\n\n"
        "*Goteborg — Goteborgs Konstmuseum*\n"
        "Nordiskt maleri fran sekelskiftet. "
        "Zorn, Larsson och Hill i nytt ljus "
        "med restaurerade masterpiece.\n\n"
        "*Malmo — Moderna Museet Malmo*\n"
        "Samtida fotografi fran Oresundsregionen. "
        "Svartvita reportage om industrins "
        "omvandling.\n\n"
        "*Uppsala — Gustavianum*\n"
        "Vikingaarvet och nya arkeologiska "
        "fynd. Runstenar, smycken och "
        "vardagsforemol fran tusen ar sedan.\n\n"
        "*Kiruna — Ajtte Museum*\n"
        "Samisk kultur och fjallvarlden. "
        "Slojd, renskotsel och berattelser "
        "fran norr.\n\n"
        "_Oppettider pa museernas webbplatser._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("🍳 *Svenska klassiker: fyra "
        "traditionella recept*\n\n"
        "Det svenska koket ar arlikt "
        "och hjartevarmande.\n\n"
        "*Kottbullar*\n"
        "Blandfars, lok, strobrod och "
        "gradde. Steks i smor. Serveras "
        "med potatis, graddsas, lingon "
        "och pressgurka. Den svenska "
        "nationalratten.\n\n"
        "*Artsoppa med pannkakor*\n"
        "Gula arter, flask, lok och "
        "kryddor. Kokas langsamt i timmar. "
        "Serveras pa torsdagar med tunna "
        "pannkakor och sylt.\n\n"
        "*Smorgastarta*\n"
        "Brod, skiktad med raksallad, "
        "agg, skinka och majonnäs. "
        "Dekorerad med rakor och citron. "
        "Festens mittpunkt.\n\n"
        "*Kanelbullar*\n"
        "Vetedeg med smor, kanel och "
        "socker. Rullat, skuret och bakat "
        "till gyllenbrun farg. Bast med "
        "kaffe pa fikarasten.\n\n"
        "_Mangder efter egen smak._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("🏠 *Fem gomda svenska byar "
        "for hosten*\n\n"
        "*Sigtuna (Stockholm)*\n"
        "Sveriges aldsta stad. Runstenar, "
        "sma butiker och Malarstrandens "
        "hostfarger. Lugnt och historiskt.\n\n"
        "*Fjallbacka (Vastra Gotaland)*\n"
        "Fiskelage pa Bohuskusten. Granitklippor, "
        "rakor och Ingrid Bergmans torg. "
        "Hosten ger lugn fran sommartrangseln.\n\n"
        "*Gammelstad (Norrbotten)*\n"
        "Kyrkstad med over 400 stugor fran "
        "1500-talet. UNESCO-varldsarv. "
        "Tyst, rott och vackert.\n\n"
        "*Granna (Jonkoping)*\n"
        "Polkaparkans hemstad vid Vattern. "
        "Fargranna trahus, utsikt over "
        "Visingo och handgjorda polkakarameller.\n\n"
        "*Tanum (Vastra Gotaland)*\n"
        "Hallristningar fran bronsaldern. "
        "UNESCO-varldsarv. Klippor, hav "
        "och tretusen ar gammal konst.\n\n"
        "_Boka boende i forvag._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Ordlista", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Vanliga fragor", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Om oss", callback_data="about"))
    text = ("🏛 *Oversikt*\n\n"
        "Fran denna meny kan du:\n\n"
        "• Lasa *dagens amnen* och vara artiklar.\n"
        "• Blaadra i sektioner: Kultur, "
        "Resor, Mat, Vetenskap.\n"
        "• Kolla ordlistan och vanliga fragor.\n"
        "• Lasa om oss och kontakta redaktionen.\n\n"
        "For hela utgavan, anvand "
        "knappen nedan.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("📖 *Kort ordlista*\n\n"
        "*Redaktion* — teamet som valjer "
        "och forbereder texter.\n\n"
        "*Ledare* — asiktsartikel som "
        "oppnar en sektion.\n\n"
        "*Fotoreportage* — journalistisk "
        "berattelse byggd pa fotografier.\n\n"
        "*Tidlos innehall* — text vars "
        "relevans inte beror pa dagens "
        "nyheter.\n\n"
        "*Korrespondent* — journalist som "
        "rapporterar fran faltet.\n\n"
        "*Spalt* — aterkommande sektion "
        "tillangnad ett specifikt amne.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"))
    text = ("❓ *Vanliga fragor*\n\n"
        "*Ar denna bot officiell?*\n"
        "Dagens Lasning ar ett oberoende "
        "redaktionellt projekt.\n\n"
        "*Hur ofta uppdateras det?*\n"
        "Urvalet fornyas varje sasong.\n\n"
        "*Hur stangar jag av aviseringar?*\n"
        "Fran Telegrams chattinstallningar.\n\n"
        "*Kan jag dela en artikel?*\n"
        "Ja, med Telegrams delningsfunktion.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Om oss", callback_data="about"))
    text = ("✏️ *Kontakt*\n\n"
        "For redaktionell korrespondens:\n"
        "• E-post: redaktion@dagenslakning.se\n\n"
        "*Utgivare*\n"
        "Dagens Lasning AB\n"
        "Drottninggatan 68\n"
        "111 21 Stockholm\n"
        "Sverige\n\n"
        "Lasarsynpunkter pa vardagar.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Oversikt", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"))
    text = ("🏛 *Om Dagens Lasning*\n\n"
        "Dagens Lasning ar ett oberoende "
        "redaktionellt projekt tillangnat "
        "kultur, resor, mat och teknik.\n\n"
        "Redaktionen valjer dagligen "
        "kvalitetsinnehall for en "
        "informerad paus fran vardagen.\n\n"
        "Denna Telegram-utgava ar utformad "
        "for bekvam lasning i chatten.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Dagens amnen", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Valkommen! Tryck pa *Dagens amnen* for att borja.", parse_mode="Markdown", reply_markup=markup)


print("Dagens Lasning Bot is running...")
bot.infinity_polling()
