import smtplib

server = None
print("Starting....!")
try:
    # Replace with actual SMTP server and port for your email provider
    server = smtplib.SMTP('smtp.hostinger.com', 465)  
    server.ssl()  # For providers that require TLS; use server.ssl() for SSL if needed
    #server.starttls()  # For providers that require TLS; use server.ssl() for SSL if needed
    server.login('support@sterlingspecialisthospitals.com', '123@Qwertyqwerty123')
    print("Login successful")
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")
except smtplib.SMTPConnectError as e:
    print(f"Connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Ending....!")
    if server:
        server.quit()
