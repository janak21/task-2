import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sawalejanak5@gmail.com", "luvTol@F*#@213^8&8") 
  
# message to be sent 
message = "Your code is running fine!"
  
# sending the mail 
s.sendmail("sawalejanak5@gmail.com", "jnksawale@gmail.com", message) 
  
# terminating the session 
s.quit()
