import socket
import threading





def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))

        if result==0:
            print(f"[+] Port {port} is OPEN")

        s.close()
    except:   
        pass


def start_scanner(target_ip):
    print(f"Scanning target: {target_ip}")
    print("=============================")


    threads = []

    for port in range(1, 501):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()
    

    print("==============================")
    print("Scan Completed. ")

# 
print('''
=========================================================================
=========================================================================
 ____                 _      ____                                      
 |  _ \  ___   _ __  | |_   / ___|   ___  __ _  _ __   _ __    ___  _ __ 
 | |_) |/ _ \ | '__| | __|  \___ \  / __|/ _` || '_ \ | '_ \  / _ \| '__|
 |  __/| (_) || |    | |_    ___) || (__| (_| || | | || | | ||  __/| |   
 |_|    \___/ |_|     \__|  |____/  \___|\__,_||_| |_||_| |_| \___||_|   

 [ https://github.com/White20devilera/Simple-Port-Scanner ] 
      
=========================================================================
      ''')

target = input("Enter the ip : ")
start_scanner(target)