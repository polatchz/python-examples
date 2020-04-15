#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mail sender

"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Sender and receciver mail adress

msg = MIMEMultipart()

msg['From'] = "Sender Mail"
msg['To'] = "Receiver Mail"

msg['Subject'] = "Subject"

body = "Body"

#adding text to mail
msg.attach(MIMEText(body,'plain'))


#set smtp settings
s = smtplib.SMTP('smtp server',"smtp port")
s.starttls()
s.login("Sender mail","sender password")

text = msg.as_string()

s.sendmail("Sender Mail","Receiver Mail",text)
