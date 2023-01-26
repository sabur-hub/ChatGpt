import openai
import telebot
from config import *

bot = telebot.TeleBot(BOT)
openai.api_key = CHAT_GPT


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am a bot that uses the OpenAI API to answer questions. How can I help you today?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    question = message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='> ' + question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response["choices"][0]["text"]
    bot.reply_to(message, answer)


bot.polling()

