# codigo tomado de: https://www.shellhacks.com/python-send-message-to-telegram/

import urequests

def send_to_telegram(message):

    apiToken = '6031609600:AAHR8ZT82j7jSIggKLksWl3a-Xc0VFn1dY'
    chatID = '1631741256'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = urequests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
