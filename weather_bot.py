import telebot
from config import TOKEN
import requests
from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="drivers/chromedriver", 
                          chrome_options=options)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    url = "https://ua.sinoptik.ua/погода-рівне"
    driver.get(url)
    div2 = driver.find_element_by_css_selector('#bd2')
    div2.click()
    # weather = driver.find_element_by_css_selector('div#blockDays')
    temp = driver.find_element_by_css_selector('p.today-temp').text.strip()
    min_temp = driver.find_element_by_css_selector('.temperature .min').text.strip().replace('\n','')

    print(temp)
    bot.send_message(message.chat.id, f'Temp 🌡️:{temp},\nMin temp: {min_temp}')


bot.polling()
