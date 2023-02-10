import imaplib
import email
import os
import base64
import re

svdir = '/home/wst/Desktop/python-projects/download attachments' 

email_user='samalin555@gmail.com'
email_pass='ygaomoyakiuczzdi'

mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_user,email_pass)
mail.select('Inbox')
typ,data=mail.search(None,'All')
mail_id=data[0]
id_list=mail_id.split()
last_id=id_list[-1]
final=last_id.split()

#pick the last inbox mail
result,data=mail.search(None,'ALL')
ids=data[0]
id_list=ids.split()
latest_email_id=id_list[-1]
typ, messageParts=mail.fetch(latest_email_id,('RFC822'))
for response in messageParts:
    if isinstance(response,tuple):
         msg = email.message_from_bytes(response[1])
         

         From=msg["From"]
         pick_mail = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", From)
        
#finish

for part in final:
    typ,data=mail.fetch(part,'(RFC822)')

    raw_email=data[0][1]
    #print(raw_email)
    #for response_part in data:
        #if isinstance(response_part, tuple):
            #msg = email.message_from_string(response_part[1].decode('utf-8'))
            #email_subject = msg['subject']
            #email_from = msg['attachment']
            #print ('From : ' +str(email_from)+ '\n')
            #print ('Subject : ' + email_subject + '\n')
            #print(msg.get_payload(decode=True))
    raw_email_string=raw_email.decode('utf-8')
    email_message=email.message_from_string(raw_email_string)
    

    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('content-Disposition') is None:
            continue
        fileName=part.get_filename()
        #print(fileName)
        
        
        if fileName is not None: 
            sv_path = os.path.join(svdir, fileName) 
            if not os.path.isfile(sv_path):
                fp = open(sv_path, 'wb')
                
                fp.write(part.get_payload(decode=True))
                
                fp.close()
                

