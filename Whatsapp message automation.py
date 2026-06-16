from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = #account_sid_from_twilio
auth_token = #auth_token_from_twilio

Client = Client(account_sid,auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = Client.messages.create(
            from_='whatsapp:#whatsaap_no_from_twilio()',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID{message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

name = input('Enter the recipient name= ')
recipient_number  = input('Enter the recipient whatsapp number with country code (e.g, +91): ')
message_body = input(f'Enter the message you want to send to {name}:')


date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM IN 24 HOUR FORMAT): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds ()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message schedule to be sent to {name} at {schedule_datetime}')


    time.sleep(delay_seconds)

    send_whatsapp_message(recipient_number,message_body)
