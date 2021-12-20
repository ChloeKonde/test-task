from email.message import EmailMessage
import smtplib

def sent_email(to, subject, body):
    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    # to = 'konde.chloe@gmail.com'
    # subject = 'OMG Super Important Message'
    # body = "frogge party at 4 am\n\n"

    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['To'] = to

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.close()

        print ("Email sent!")
    except:
        print('Something went wrong...')

