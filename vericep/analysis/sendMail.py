import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from . import accountInfo


def send_test_mail(email, id):
    msg = MIMEMultipart()
    msg['Subject'] = 'Vericep Analysis Result'
    msg['From'] = accountInfo.mail
    msg['To'] = email

    msgText = MIMEText('<b>Vericep Analysis Result</b>', 'html')
    msg.attach(msgText)

    pdf = MIMEApplication(open("outputs/"+str(id)+".html", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment',
                   filename="analysis.html")
    msg.attach(pdf)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(accountInfo.mail, accountInfo.password)
            smtpObj.sendmail(accountInfo.mail, email, msg.as_string())
    except Exception as e:
        print(e)
