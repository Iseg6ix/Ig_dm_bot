import random
import json
import time
from src.instadm import InstaDM

f = open('infos/accounts.json', )
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

with open('infos/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]

while True:
    total_usernames = len(usernames)  # return how many accounts to dm
    total_dms = 0
    print(f"Total usernames to dm: {total_usernames}")

    if not usernames:
        print('Finished usernames.')
        break

    for account in accounts:
        if not usernames:
            break
        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)

        stop_conditional = 0
        daily_max = 60
        random_time = random_time = random.randint(2, 4)
        while stop_conditional != total_usernames or daily_max:
            try:
                dms_sent_for_this_session = 0
                while dms_sent_for_this_session != 2:
                    if not usernames:
                        break

                    username = usernames.pop()
                    # Send message
                    insta.sendMessage(
                        user=username, message=random.choice(messages))
                    time.sleep(random_time)

                    dms_sent_for_this_session += 1
                    total_dms += 1
                    stop_conditional += 1
                    print(f'DMs sent for this session : {dms_sent_for_this_session}')
                    print(f"total number of dms sent : {total_dms}")

                else:
                    print(f"{total_dms} dms sent! i'm going to rest for {random_time} seconds!")
                    remaining_dms = total_usernames - stop_conditional
                    print(f"stop after {total_usernames} dms, remaining dms to be sent = {remaining_dms}")
            except stop_conditional == total_dms:
                break
        insta.teardown()
