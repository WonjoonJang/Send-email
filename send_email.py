import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("이메일 내용입니다.") # type your e-mail

message["Subject"] = "제목입니다." # type your subject
message["From"] = "___" # type your e-mail address
message["To"] = "___" # type recipient e-mail

with open("aaa.png","rb") as image: # aaa.png is an example
    image_file = image.read()

image_type = imghdr.what('aaa',image_file) # aaa is example
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("___","___") # type your e-mail and password

sendEmail("___") # type your e-mail
smtp.quit()
