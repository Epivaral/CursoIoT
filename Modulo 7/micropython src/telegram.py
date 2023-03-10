import urequests

def send_to_telegram(message):

    apiToken = '6031609600:AAHR8ZT8Svj7jSIggKLksWj3a-Xc0VFn2dY'
    chatID = '1531744252'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = urequests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)