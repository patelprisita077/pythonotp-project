# -*- coding: utf-8 -*-
"""otpcap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Z-X0Tt38Wb7YU35E4_4wGMquh0qka1c
"""

import random

# Function to generate a 6-digit OTP randomly
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP to user's email address (simulated)
def send_otp(email, otp):
    print(f"Simulated: OTP sent to {email}: {otp}")

# Function to prompt user to enter OTP
def enter_otp():
    return input("Please enter the OTP received in your email: ")

# Function to verify if entered OTP matches generated OTP
def verify_otp(otp, entered_otp):
    return otp == entered_otp

def verify_email_otp():
    email = input("Enter your email address: ")
    otp = generate_otp()
    send_otp(email, otp)
    attempts = 3
    while attempts > 0:
        entered_otp = enter_otp()
        if verify_otp(otp, entered_otp):
            print("OTP verification successful. Access granted.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid OTP. {attempts} attempts remaining.")
            else:
                print("Maximum attempts reached. Access denied.")

if __name__ == "__main__":
    verify_email_otp()