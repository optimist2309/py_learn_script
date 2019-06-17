"""
Python script to send birthday wishes to your friends.
If you want to send birthday wishes at 12:00 am automated just add this script in cron job in linux system.
To storing birthday, names, email-id hard-coded values is used next script I will fetch all the things from api.
"""

from datetime import date
import smtplib

today = date.today()
today_date_in_dd_mm_yyyy_format = today.strftime("%d/%m/%Y")
birthday_date_list = ['16/06/2019', '17/06/2019', '18/06/2019']
friends_name = ['Harish', 'Vishnu', 'Navin']
friends_email_address = ['your_email_id@domain.com', 'your_email_id@domain.com','your_email_id@domain.com']

def email_sender():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your_email_id@domain.com", "your_id_pass")
    SUBJECT = "Happy Bithday"   
    TEXT = "Hi " + friends_name[birthday_date_list_index] + " Wish You Happy Birthday."
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("your_email_id@domain.com", friends_email_address[birthday_date_list_index], message)
    s.quit()
try:
    birthday_date_list_index = birthday_date_list.index(today_date_in_dd_mm_yyyy_format)
    if birthday_date_list_index > 0:
        email_sender()
        print("Birthday wishes sent successfully")
except ValueError:
    print("Today is no birthday.")
    






 




