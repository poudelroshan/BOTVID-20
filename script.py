import scrape, botvid, user_database, authenticate
from datetime import datetime

Alert1 = "You received the message above because you have subscribed for periodic notifications from me. The subscription lasts for 24 hours before Facebook unsubscribes you automatically."
Alert2 = "If you want to keep receiving messages from me, you will need to send me 'subscribe' every 24 hours. Sorry for this hassle, but this is one of Facebook's Privacy Policies"

def send_message():
    now = datetime.now()
    counter_mins = now.minute
    counter_hours = now.hour
    if (counter_hours % 2 == 0 and counter_mins == 42):
        for users in user_database.get_users():
            botvid.send_message(users, botvid.get_message())
            botvid.send_message(users, Alert1)
            botvid.send_message(users, Alert2)
            print("Sent automated update message to user: ", users)
    
    print("Data base updated at: ", now)
    

if __name__ == '__main__':
    scrape.corona() #update database
    send_message()

    
