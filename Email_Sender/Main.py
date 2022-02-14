# ---------- * MODULES * ---------- #
from colorama import Fore
import smtplib
import datetime as dt
# --------------------------------- #
data = dt.datetime.now()
# ------------------------------- * BANNER * --------------------------------- #
print(Fore.RED , """

███████ ███    ███  █████  ██ ██              ███████ ███████ ███    ██ ██████  ███████ ██████  
██      ████  ████ ██   ██ ██ ██              ██      ██      ████   ██ ██   ██ ██      ██   ██ 
█████   ██ ████ ██ ███████ ██ ██              ███████ █████   ██ ██  ██ ██   ██ █████   ██████  
██      ██  ██  ██ ██   ██ ██ ██                   ██ ██      ██  ██ ██ ██   ██ ██      ██   ██ 
███████ ██      ██ ██   ██ ██ ███████ ███████ ███████ ███████ ██   ████ ██████  ███████ ██   ██ 
                                                                                                
                                                                                                

""")
# ---------------------------------------------------------------------------- #


# ------- * YOUR ACCOUNT * ----- #
EMAIL = "tom.nix2004@gmail.com"
PASSWORD = "apzpz924@#$"
# ------------------------------ #


# ------------------------ * SMTP * ------------------------ #
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(from_addr=EMAIL,to_addrs="apzpz924@gmail.com", msg="Subject:This is Your Subject!\n\nThis is Your Message in here!")
    print(Fore.YELLOW , "[+]Your Email Send Successfuly At: ",data)
# ---------------------------------------------------------- #
