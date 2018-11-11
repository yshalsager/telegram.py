# telegram.py
A slim script, written in python, allows you to send messeges via your telegram bot.

## Bot configuration

* Create a bot at telegram:
  * Search for the user `@botfather` at telegram and start a chat with him.
  * Use the `/newbot` command to create a new bot. BotFather will give you a
    token. Keep this.
* Use your telegram client to send a message to your new bot. Any message
    will do.

## Using the script
* Get the latest copy of `telegram.py` and run it with these arguments:
`telegram.py -t TOKEN -c CHAT -M MESSAGE`
* The default prase mode is `Markdown`. If you want to use HTML use the flag `-m HTML`
