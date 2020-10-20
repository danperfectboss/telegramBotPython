import requests

def sendMessage():
    id = <ID>
    token = <TOKEN>
    text="Hello World!"
    url= "https://api.telegram.org/bot"+token+"/sendMessage"
    params = {
        'chat_id':id,
        'text': text 
    }
    requests.post(url, params=params)


if __name__ == "__main__":
    sendMessage()