# telegram.py
A slim script, written in python, allows you to send messeges via your telegram bot.

Inspired from [telegram.sh](https://github.com/fabianonline/telegram.sh/)

## Bot configuration

* Create a bot at telegram:
  * Search for the user `@botfather` at telegram and start a chat with him.
  * Use the `/newbot` command to create a new bot. BotFather will give you a
    token. Keep this.
* Use your telegram client to send a message to your new bot. Any message
    will do.

## Using the script

* Get the latest copy of `telegram.py` and run it with:
  * The required arguments: `(-t TOKEN | -c CHAT)` and one of the follwing options `(-M MESSAGE | -P PHOTO | -V VIDEO | -A AUDIO | -F FILE)`
  * Optional arguments: `(-p yes/no)` to disable/enable URL preview. `(-c TEXT)` to add a caption with Media/Documents.
* The default prase mode is `Markdown`. If you want to use HTML use the flag `(-m HTML)`

## Some examples of usage:

- Sending normal text:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -M "Hello"`

- Sending markdown text:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -M "*Hello*"`

- Sending HTML text:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -M "<b>Hello</b>" -m HTML`

- Sending link with preview:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -M "this is a [link](https://github.com/yshalsager/telegram.py)" -p no`

- Sending link without preview:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -M "This is a [link](https://github.com/yshalsager/telegram.py)"`

- Sending photo:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -P avatar.png`

- Sending photo with caption:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -P avatar.png -C "Logo"`

- Sending photo with HTML caption:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -m HTML -P avatar.png -C "<b>Logo</b>"`

- Sending video:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -V video.mp4`

- Sending audio:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -A audio.mp3`

- Sending file:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -F file.zip`

- Sending file with HTML caption:

`python telegram.py -t xxxxx:xxxxx -c @TestChannel -m HTML -F file.rar -C "<b>File</b>"`

## Using the binary:

A Linux binary version of this script is available on [releases](https://github.com/yshalsager/telegram.py/releases), compiled with [pyinstaller](https://www.pyinstaller.org/).

