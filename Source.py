import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def main():
    url = input("Type here the url of the cookie jar!: ")
    s = requests.session()
    s.get(url)
    cookies = s.cookies.get_dict()
    with open('cookies.txt', 'w') as f:
        f.write(str(cookies))

def send():
    smtp_port = 587                 
    smtp_server = "smtp.gmail.com"  

    email_from = input("Type here your mail: ")
    x = input("Type here the receiver mail: ")
    email_list = [x]

    pswd = input("Type here the app password of your account: ")

    subject = "cookies"

    def send_emails(email_list):

        for person in email_list:
            body = f"""
            Here is my precious cookies!
            """
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            filename = "cookies.txt"

            attachment= open(filename, 'rb')  

            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

            text = msg.as_string()

            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_from, pswd)
            print()

            print(f"Sending cookies to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"Cookies sent to: {person}")
            print()

        TIE_server.quit()

    send_emails(email_list)

def quit():
    print("Cookie Monster is sad now :(")
    exit(0)

while True:
    f = input("> ")

    if f == "cookies":
        print("Awakening the Cookie Monster...")
        time.sleep(2)
        main()
    
    elif f == "send--":
        print("Packing cookies...")
        time.sleep(2)
        send()
        
    elif f == "q":
        quit()

    elif f == "!help":
        print("""for storing cookies type cookies,
for mailing cookies to yourself type send--,
to quit type q...""")

    else:
        print("¿¿¿cookie monster can't understand what the fuck are you saying???")