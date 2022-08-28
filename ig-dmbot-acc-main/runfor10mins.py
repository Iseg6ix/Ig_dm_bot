from collections import Counter
import json
import random
from time import sleep
from src.instadm import InstaDM

f = open('infos/accounts.json',)
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

with open('infos/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]

while True:
    if not usernames:
        print('Finished usernames.')
        break

    for account in accounts:
        if not usernames:
            break
        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)
        
        total_usernames = len(usernames)  # rerturn how many accounts to dm
        daily_max = 61

        while total_usernames < daily_max:
            dms_sent = 0
            while dms_sent != 10:
                for i in range(10):
                    if not usernames:
                        break

                    username = usernames.pop()
                    # Send message
                    insta.sendMessage(
                        user=username, message=random.choice(messages))

                    dms_sent += 1
                    print(f"total number of dms sent : {dms_sent}")
            print("10 dms sent! now i'm taking a break for 10 mins")
            dms_sent = 0
            sleep(10)
            
        insta.teardown()
