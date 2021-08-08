import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# Mail Detaylarını oluşturmak.
mail = MIMEMultipart()
mail["From"] = "your_email"
mail["To"] = "target_email"
mail["Subject"] = "Send email with SMTP"

body = """
I send to email with SMTP

Tolgahan Çelik
"""

mail_body = MIMEText(body, "plain")
mail.attach(mail_body)

# Gmail serverlarına bağlanmak.
try:
    mail_server = smtplib.SMTP("smtp.gmail.com", 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login("your_mail", "your_mail_password")

    mail_server.sendmail(mail["From"], mail["To"], mail.as_string())
    mail_server.close()

    print("Mail send successfully.")

except Exception as error:
    sys.stderr.write("Error corrupted while mail sending.")
    sys.stderr.flush()
