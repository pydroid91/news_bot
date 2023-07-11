import schedule
import telebot
from news_collection import update_news
from news_collection import LATEST_NEWS, SEND_NEWS, SEND_LINKS
bot = telebot.TeleBot('6066401472:AAGRIbmSMl3fqcwO2YT8TKdeSsAk6oADjmY')
user_id=5123972842

def main():
    update_news()
    MAILING = []
    for source in LATEST_NEWS:
        for i in range(5):
            if LATEST_NEWS[source][i] != None:
                MAILING.append((SEND_NEWS[source][i], SEND_LINKS[source][i]))

    for news in MAILING:
        if news != (None, None):
            bot.send_message(user_id, news[0] + '\n' + news[1])


schedule.every(6).seconds.do(main)
while True:
    schedule.run_pending()

if __name__ == '__main__':
    bot.polling(none_stop=True)
