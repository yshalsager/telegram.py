from argparse import ArgumentParser

from requests import post


def arg_parse():
    global token, chat, message, mode, preview, photo, gif, caption, video, audio, voice, file, send
    switches = ArgumentParser()
    group = switches.add_mutually_exclusive_group(required=True)
    group.add_argument("-M", "--message", help="Text message")
    group.add_argument("-P", "--photo", help="Photo path")
    group.add_argument("-G", "--gif", help="GIF Photo path")
    group.add_argument("-V", "--video", help="Video path")
    group.add_argument("-A", "--audio", help="Audio path")
    group.add_argument("-O", "--voice", help="Voice path")
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
    gif = args["gif"]
    video = args["video"]
    audio = args["audio"]
    voice = args["voice"]
    file = args["file"]
    mode = args["mode"]
    preview = args["preview"]
    caption = args["caption"]

    if message is not None:
        send = "text"
    elif photo is not None:
        send = "photo"
    elif gif is not None:
        send = "gif"
    elif video is not None:
        send = "video"
    elif audio is not None:
        send = "audio"
    elif voice is not None:
        send = "voice"
    elif file is not None:
        send = "file"


def send_message():
    global r, status, response
    params = (
        ('chat_id', chat),
        ('text', message),
        ('parse_mode', mode),
        ('disable_web_page_preview', preview)
    )
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    r = post(url, params=params)
    status = r.status_code
    response = r.reason


def send_photo():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'photo': (photo, open(photo, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendPhoto"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def send_gif():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'animation': (gif, open(gif, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendAnimation"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def send_video():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'video': (video, open(video, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendVideo"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def send_audio():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'audio': (audio, open(audio, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendAudio"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def send_voice():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'voice': (voice, open(voice, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendVoice"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def send_file():
    global r, status, response
    files = {
        'chat_id': (None, chat),
        'caption': (None, caption),
        'parse_mode': (None, mode),
        'document': (file, open(file, 'rb')),
    }
    url = "https://api.telegram.org/bot" + token + "/sendDocument"
    r = post(url, files=files)
    status = r.status_code
    response = r.reason


def req():
    if send == "text":
        send_message()
    elif send == "photo":
        send_photo()
    elif send == "gif":
        send_gif()
    elif send == "video":
        send_video()
    elif send == "audio":
        send_audio()
    elif send == "voice":
        send_voice()
    elif send == "file":
        send_file()
    else:
        print("Error!")


def req_status():
    if status == 200:
        print("Message sent")
    elif status == 400:
        print("Bad recipient / Wrong text format")
    elif status == 401:
        print("Wrong / Unauthorized token")
    else:
        print("Unknown error")
    print("Response: " + response)


arg_parse()
req()
req_status()
