import smtplib
import random
import datetime as dt
import pandas
MY_EMAIL='rehabstoreii@gmail.com'
PASSWORD='1234687412345678'

now=dt.datetime.now()
# year=now.year
# if year==2021:
#     print('Wear a face mask')
day_of_the_week=now.weekday()
if day_of_the_week==6:
    day_of_the_week='Sunday'
# print(day_of_the_week)
#
# date_of_birth=dt.datetime(year=1997,month=1,day=15, hour=4)
# print(date_of_birth)

    with open('quotes.txt')as quotes:
        all_quotes=quotes.readlines()
        quote=random.choice(all_quotes)


    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='rehabstore@yahoo.com',
                            msg=F'subject: {day_of_the_week} quote \n\n {quote}')


