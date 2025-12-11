1. Create an SMTP client → `smtplib.SMTP("smtp.gmail.com", 587)`
2. Start TLS → `server.starttls()`
3. Login → `server.login(YOUR_EMAIL, APP_PASSWORD)`
4. Build the email message (MIME)
5. Send it → `server.sendmail(from, to, msg)`
6. Quit → `server.quit()`
