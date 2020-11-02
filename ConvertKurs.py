


from bs4 import BeautifulSoup
import requests

##### list nama bank
url_bank = "https://kurs.web.id/"
data_bank = requests.get(url_bank)
out = BeautifulSoup(data_bank.content,"html.parser")
Bank_list = []
Bank_list_final = []
find_bank = out.find_all("ul",class_="menu-list")
for i in find_bank:
    Bank_list.append(i.text.split())
for i in Bank_list[0]:
    Bank_list_final.append(i)
print(Bank_list_final)

###### list currency
nama_bank = input("Masukkan nama bank : ")
while nama_bank.upper() not in Bank_list_final:
    print(f"{nama_bank} not found ! ")
    nama_bank = input("Masukkan nama bank : ")
if nama_bank.upper() in Bank_list_final:
    url_curr = f"https://kurs.web.id/bank/{nama_bank.upper()}"
    data_curr = requests.get(url_curr)
    out_curr = BeautifulSoup(data_curr.content,"html.parser")
    #print(out.prettify)
    find_curr = out_curr.find_all("abbr")
    curr_list_final = []
    for i in find_curr:
        curr_list_final.append(i.text[1:4])
    print(curr_list_final)

##### CONVERT
opsi = input("1(IDR to ASING)/2(ASING to IDR) : ")
opsi_list = ["1","2"]
while opsi not in opsi_list:
    print(f"{opsi} not found !")
    opsi = input("1(IDR to ASING)/2(ASING to IDR) : ")

asing = input("Input mata uang asing : ")
while asing.upper() not in curr_list_final:
    print(f"{asing} not found ! ")
    asing = input("Input mata uang asing : ")

if opsi == "1":
    while True :
        try :
            token = "qYmRGJFBlGvChwoKKu68umcs8S09eVCmBohqptFd"
            url = f"https://api.kurs.web.id/api/v1?token={token}&bank={nama_bank.lower()}&matauang={asing.lower()}" 
            data = requests.get(url)
            output = data.json()
            dana = int(input(f'Masukkan nilai IDR : '))
            while dana < 0 :
                print(f"INPUT POSITIVE NUMBER")
                dana = int(input(f'Masukkan nilai IDR : '))
            if dana >= 0 :
                convert_idr = dana/output['beli']
                print(f'Nilai uang anda {dana:,} IDR dan {convert_idr:,} {asing.upper()}')
                break
        except :
            print("INPUT NUMBER ! ")
elif opsi == "2":
    while True:
        try :
            token = 'qYmRGJFBlGvChwoKKu68umcs8S09eVCmBohqptFd'
            url = f"https://api.kurs.web.id/api/v1?token={token}&bank={nama_bank.lower()}&matauang={asing.lower()}" 
            data = requests.get(url)
            output = data.json()
            dana = int(input(f'Masukkan nilai {asing.upper()} : '))
            while dana < 0 :
                print(f"INPUT POSITIVE NUMBER")
                dana = int(input(f'Masukkan nilai IDR : '))
            if dana >= 0:
                convert_asing = dana*output['jual']
                print(f'Nilai uang anda {dana:,} {asing.upper()} dan {convert_asing:,} IDR')
                break
        except :
            print("INPUT NUMBER ! ")






