#jkeibler913@gmail.com  - email
#$Piproj35  - email password
# cbav ssng tlvl sqpy   - email app password
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
current_time = datetime.now()

email_sender = 'jkeibler913@gmail.com'
email_password = 'cbav ssng tlvl sqpy'
email_reciever = 'rliddick@southhills.edu'
email_recipients = ['keibler.joshua@gmail.com', 'cotto06@southhills.edu','npage@southhills.edu',]

#Sending the subject of the Email
subject = 'Security Alert! Trap Triggered!'

#Setting the body of the email
body = f"""
Hello Valued Customer,

This is TripSys, your favorite home/business security system! We are contacting you to inform you of some activity.

Our system has picked up some activity that had triggered the alarm. This happened on {current_time.strftime('%d/%m/%Y')}, at {current_time.strftime('%H:%M:%S')}.

While we are not able to verify who or what triggered it, we encourage you to look into it, investigate, or possibly report to the police if it was clayton!

Disclaimer: This is an automated email message. 

Your local security system,
- TripSys
"""

#Defineing some parts of the email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

#Being more secure so everyone is happy
context = ssl.create_default_context()
#Sending emails to one person individually 
#with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#    smtp.login(email_sender, email_password)
#    smtp.sendmail(email_sender, email_reciever,em.as_string())
    
#Trying to use a loop to send to a list of emails
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    for reciever in email_recipients:
        smtp.sendmail(email_sender, reciever, em.as_string())
