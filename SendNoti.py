from smtplib import SMTP #email library

#email details
_fromEmail = "todpicket@gmail.com"
_mypassword = "wlixjllploomvmyw"

def send_email(subject,body,toEmail):
    #construct email message
    message = f"Subject: {subject}\n\n{body}"

    #connect to SMTP server
    _server = SMTP("smtp.gmail.com",587)
    _server.starttls()

    #login to server
    _server.login(_fromEmail, _mypassword)

    #send email
    _server.sendmail(_fromEmail,toEmail,message)

    #quit server
    _server.quit()

    print("Email Succesfully Sent!")