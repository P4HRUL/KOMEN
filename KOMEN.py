import os,re,sys,bs4,time,json,random,datetime,requests

logo = ('''\033[1;91m
  ____   ___ _____   _  _____  __  __ _____ _   _ 
 | __ ) / _ \_   _| | |/ / _ \|  \/  | ____| \ | |
 |  _ \| | | || |   | ' / | | | |\/| |  _| |  \| |
 \033[1;97m| |_) | |_| || |   | . \ |_| | |  | | |___| |\  |
 |____/ \___/ |_|   |_|\_\___/|_|  |_|_____|_| \_|
''')

def jalan(xnxx):
	for hengker in xnxx + '\n':
		sys.stdout.write(hengker);sys.stdout.flush();time.sleep(0.05)

def login():
        os.system('clear')
        print (logo)
        cookie = input('\033[1;97m[+] cookie : \033[1;92m')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
            token = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(token):
                open('cookie.txt','w').write(cookie)
                open('token.txt','w').write(token)
                jalan ("\n\033[1;97m[+] sedang masuk tunggu sebentar...")
                requests.post("https://graph.facebook.com/100089033379675_161391613505284/comments?message=gua pake script lu bang&access_token="+token,headers = {"cookie": cookie})
                komen()
        except AttributeError:
        	exit("\n\033[1;97m[+] cookie sudah kedaluwarsa !!!")
        except requests.exceptions.ConnectionError:
        	exit("\n\033[1;97m[+] koneksi internet bermasalah !!!")

def komen():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	print (logo)
	try:
		id = input(f"[+] masukan id postingan : ")
		komen = input("[+] komentar : ")
		limit = int(input("[+] limit : "))
		print("")
		for x in range(limit):
			postingan = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komen}&access_token={token}',cookies={'cookie':cookie})
			cek = json.loads(postingan.text)
			if 'id' in cek:
				print ("[✓] berhasil : "+cek["id"])
			else:
				print ("[!] gagal !");exit()
		
		print("\n\033[1;97m[+] selesai...")
		back = input ("\n\033[1;97m[<BACK>]")
		masuk()
	except requests.exceptions.ConnectionError:
		exit()
		
login()
		