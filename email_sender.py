import smtplib, ssl
from color_activity import password, sender_email
def sendemail(OUTPUT_STRING):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    receiver_email = "alexandrei1998@hotmail.it"


    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        try:
            server.sendmail(sender_email, receiver_email, OUTPUT_STRING)
            print('Email sent succesfully ')
        except Exception :
            print('Error with email')
