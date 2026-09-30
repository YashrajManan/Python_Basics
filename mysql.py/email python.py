# email python

import smtplib
from email.message import EmailMessage

sender_email = "Yashraj.7156@gmail.com"
receiver_email = "yashraj90009@gmail.com"
password = "isrh xvdg iwzz yvkc" 



# subject = "Test Email"
# body = "this is a test email sent from python"

# message = f"""\
# subject:{subject}
# {body}
# """
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit() 