from argparse import ArgumentParser
from requests import post

switches = ArgumentParser()
switches.add_argument("-t", "--token", required=True, help="Telegram bot token")
switches.add_argument("-c", "--chat", required=True, help="Chat to use as recipient")
switches.add_argument("-m", "--mode", help="HTML/Markdown", default="Markdown")
switches.add_argument("-M", "--message", required=True, help="The message to send")
args = vars(switches.parse_args())
token = args["token"]
chat = args["chat"]
message = args["message"]
mode = args["mode"]

params = (
    ('chat_id', chat),
    ('text', message),
    ('parse_mode', mode),

)
url = "https://api.telegram.org/bot" + token + "/sendMessage"
req = post(url, params=params)
