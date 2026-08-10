import time, os, webbrowser, sys

print('''███ █   █  ████ █████  ███        ███   ████ ███ █   █  ███  
 █  ██  █ █       █   █   █      █   █ █      █  ██  █ █     
 █  █ █ █  ███    █   █████ ████ █   █  ███   █  █ █ █ █  ██ 
 █  █  ██     █   █   █   █      █   █     █  █  █  ██ █   █ 
███ █   █ ████    █   █   █       ███  ████  ███ █   █  ███  ''')
print("Istagram das pessoas chatas: ")

print("1) Gabriela")
print("2) Rafael")

Name = input("Selecione: ")

if Name == "1":
    print("CARREGANDO....")
    time.sleep(3)
    webbrowser.open("https://www.instagram.com/gabbiisilva_/")

elif Name == "2":
    print("CARREGANDO....")
    time.sleep(3)
    webbrowser.open("https://www.instagram.com/raphaeltorres10/")
else:
    print("RESPOSTA INCORRETA ")
