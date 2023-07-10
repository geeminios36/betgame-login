import requests


class sendMsgTelegram:
    def __init__(self):
        self.sendToTelegram()

    def sendToTelegram(self, message=''):
        namTong = '1245659348'
        haiNam = '6333280693'
        chatIDs = [haiNam, namTong]

        apiToken = '6357041989:AAGNt8SDNZqZDr90pRTv-afZzjeyDQPugzw'
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        # apiURL = f'https://api.telegram.org/bot{apiToken}/getUpdates'
        # response = requests.post(apiURL, json={'offset' :0})
        try:
            if message != '':
                for chatID in chatIDs:
                    response = requests.post(
                        apiURL, json={'chat_id': chatID, 'text': message})
                    print(response.text)
        except Exception as e:
            print(e)
