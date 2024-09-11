# Import essential libraries: Gradio for UI, smtplib for email, random for random values, and validate_email for email validation

import gradio as gr
import smtplib
import random
from validate_email import validate_email

# Function to validate an email and send an OTP via Gmail if valid

def email_sent(email):
    global otp
    is_valid = validate_email(email, verify=True)
    if is_valid:
        otp=random.randint(100000,999999)
        server = smtplib.SMTP('smtp.gmail.com',587) 
        server.starttls()  
        server.login('sapnakamble1995@gmail.com', 'wwjuavddovmqqddr')
        server.sendmail('sapnakamble1995@gmail.com',email,"Your OTP is - " + str(otp))
        return "OTP Sent!"
    else:
        return "The email is Not valid"
    


# Function to verify the user-provided OTP against the stored OTP, with retry attempts

def verification(user_otp):
    if user_otp == otp:
           return "OTP is Correct!"
    else:
        print("Invalid OTP, Please try again.")
        for i in range(2):
            if otp == user_otp:
                return "OTP is Correct!"
            else:
                return "Invalid OTP, Please try again."

# Create a Gradio interface to input an email and output the result of the email_sent function

email_sent_interface = gr.Interface(fn=email_sent,inputs="text",outputs="text")

# Create a Gradio interface to input number user_otp and output the result of the verification function

verification_interface = gr.Interface(fn=verification,inputs=["number"],outputs="text")

# Create a Gradio TabbedInterface with tabs for email input and OTP verification

demo = gr.TabbedInterface([email_sent_interface, verification_interface], ["enter_email", "enter_otp"])

# Launch the Gradio interface with the tabbed UI

demo.launch(share=True)
