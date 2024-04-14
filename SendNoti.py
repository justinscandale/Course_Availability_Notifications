from smtplib import SMTP #email library

#email details: send notification from _fromEmail, secure app password _mypassword 
_fromEmail = "from_email_example@gmail.com"
_mypassword = "place_secure_password_here"

def send_email(subject,body,toEmail):
    #construct email message
    message = f"Subject: {subject}\n\n{body}"

    #connect to SMTP server, configured for gmail
    _server = SMTP("smtp.gmail.com",587)
    _server.starttls()

    #login to server
    _server.login(_fromEmail, _mypassword)

    #send email
    _server.sendmail(_fromEmail,toEmail,message)

    #quit server
    _server.quit()

    print("Email Succesfully Sent!")