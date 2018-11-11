from argparse import ArgumentParser
from requests import post


def arg_parse():
    global token, chat, message, mode, preview, photo, caption, video, audio, file, send
    switches = ArgumentParser()
    group = switches.add_mutually_exclusive_group(required=True)
    group.add_argument("-M", "--message", help="Text message")
    group.add_argument("-P", "--photo", help="Photo path")
    group.add_argument("-V", "--video", help="Video path")
    group.add_argument("-A", "--audio", help="Audio path")
    group.add_argument("-F", "--file", help="File path")
    switches.add_argument("-t", "--token", required=True, help="Telegram bot token")
    switches.add_argument("-c", "--chat", required=True, help="Chat to use as recipient")
    switches.add_argument("-m", "--mode", help="Text parse mode - HTML/Markdown", default="Markdown")
    switches.add_argument("-p", "--preview", help="Disable URL preview - yes/no", default="yes")
    switches.add_argument("-C", "--caption", help="Media/Document caption")

    args = vars(switches.parse_args())
    token = args["token"]
    chat = args["chat"]
    message = args["message"]
    photo = args["photo"]
    video = args["video"]
    audio = args["audio"]
    file = args["file"]
    mode = args["mode"]
    preview = args["preview"]
    caption = args["caption"]

    if message is not None:
        send = "text"
    elif photo is not None:
        send = "photo"
    elif video is not None:
        send = "video"
    elif audio is not None:
        send = "audio"
    elif file is not None:
        send = "file"


def send_message():
    params = (
        ('chat_id', chat),
        ('text', message),
        ('parse_mode', mode),
        ('disable_web_page_preview', preview)
    )
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    post(url, params=params)


def send_photo():
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'photo': (photo, open(photo, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendPhoto"
    post(url, files=files)


def send_video():
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'video': (video, open(video, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendVideo"
    post(url, files=files)


def send_audio():
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'audio': (audio, open(audio, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendAudio"
    post(url, files=files)


def send_file():
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'document': (file, open(file, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendDocument"
    post(url, files=files)


arg_parse()

if send == "text":
    send_message()
elif send == "photo":
    send_photo()
elif send == "video":
    send_video()
elif send == "audio":
    send_audio()
elif send == "file":
    send_file()
else:
    print("Error!")
