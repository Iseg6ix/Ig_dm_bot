# Instagram DM bot
(THIS IS A MODIFIED VERSION OF THE BOT JUST IMPLEMENTING TIME FACTOR TO PREVENT INSTAGRAM FROM FLAGGING THE USER ACCOUNT AS A SPAM ACCOUNT.
NOTE THIS BOT WAS ORIGINALLY CREATED BY REDIANMARKU https://github.com/redianmarku/ig-dm-bot-acc.git
)

Instagram DM bot with account switcher feature. This bot can send messages automatically in your list of usernames.
It will send DMs and switch account automatically. It will switch account every 10 messages, so this means it will
change account after it sends message to 10 usernames and then it will go to the next account.
The amount of time before the next message is currently set to a random figure between 1-60 minutes. This can be changed
each time you rerun the bot from start. 
The total messages to be sent before logout can also be edited on request.

## Setup Bot

1.  Git clone this repo with this command --> `git clone https://github.com/redianmarku/ig-dmbot-acc`
2.  Install requirements with this command --> `pip install -r requirements.txt`
3.  Open infos folder and fill your infos of accounts in accounts.json file, in messages.txt put your message list and
    in usernames.txt put you username list that you want to send dm.
4.  Run the bot with this command --> `python run.py`

## Donate Here: PayPal --> https://paypal.me/redidev.

Thank You!
