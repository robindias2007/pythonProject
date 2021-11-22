import smtplib

sender_email = "robindias2007@gmail.com"
sender_password = "9773809775"
receiver_email = input(str("Enter email address of the person you want to send to: \n"))
message = input(str("Please enter the message you want to send to: \n"))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
print("Login successful")
server.sendmail(sender_email, receiver_email, message)
print("Message sent successfully")