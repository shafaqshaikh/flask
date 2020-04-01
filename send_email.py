import smtplib
from email.mime.text import MIMEText

def send_email(customer , dealer , rating , comments):
	port =2525
	smtp_server = 'smtp.mailtrap.io'
	login ='c6d21609d64f89'
	password ='7e841803229895'
	message =f"<h3>New Feedback Submissions</h3><ul><li>customer : { customer }</li><li>Dealer : { dealer }</li><li>Comments: { comments  }</li><li>Rating : { rating  }</li></ul>"
	send_mail = 'email1@example.com'
	receive_mail ='email2@example.com'
	msg =MIMEText(message , 'html')
	msg['subject'] ='Lexus Feedback'
	msg['from'] = send_mail
	msg['to'] =	receive_mail

	#send mail
	with smtplib.SMTP(smtp_server , port) as server:
		server.login(login , password)
		server.sendmail(send_mail , receive_mail)
