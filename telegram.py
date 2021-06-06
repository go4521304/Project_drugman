import telepot
import time
import telegram_conn

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'location':
        info = telegram_conn.request(msg['location']['latitude'], msg['location']['longitude'])
        for i in info:
            sendMessage(chat_id, i)
    else:
        pass

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except Exception as ex:
        print('전송 실패', ex)


check = False
for _ in range(5):
    try:
        bot = telepot.Bot(TOKEN)
        check = True
        break

    except Exception as ex:
        print('텔레그램 연결 실패', ex)
        print('연결 재시도...')
        time.sleep(1)

if check:
    print('연결 성공! 프로그램을 실행합니다')
    bot.message_loop(handle)

    while True:
        time.sleep(10)
    
else:
    print('연결에 실패했습니다.')