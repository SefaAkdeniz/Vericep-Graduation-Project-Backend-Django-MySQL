import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ismailsefa.akdnz@gmail.com',
    to_emails='ismailsefa.akdnz@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = SendGridAPIClient('api-key')
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
