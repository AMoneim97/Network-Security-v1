import socket,os,subprocess,subprocess,sys
from tqdm import tqdm
print("""\
 █████╗ ███╗   ███╗ ██████╗ ███╗   ██╗███████╗██╗███╗   ███╗ █████╗ ███████╗
██╔══██╗████╗ ████║██╔═══██╗████╗  ██║██╔════╝██║████╗ ████║██╔══██╗╚════██║
███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╗  ██║██╔████╔██║╚██████║    ██╔╝
██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔══╝  ██║██║╚██╔╝██║ ╚═══██║   ██╔╝ 
██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗██║██║ ╚═╝ ██║ █████╔╝   ██║  
╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝     ╚═╝ ╚════╝    ╚═╝ 
Network Security Script v1
© 2021 Ahmad abd-elMoneim
github:ahmadabdalmoneim
Linkedin:@amoneim97
""")
print('''\
    0- Exit
    1- Scan UP hosts
    2- Scan Open Ports
    3- ARP spoofing 
    4- DHCP snopping 
     ''')
f = open("Output.txt",'a+')
choice = int(input("Please enter your choice number: "))
if choice == 0:
    exit
elif choice == 1:
    d1,d2,d3,d4 = input ("Enter first IP of the network: ").split('.')
    for host in tqdm(range(1,254)):
        ping = str(os.popen('ping -n 1 {}.{}.{}.{}'.format(d1,d2,d3,host)).read())
        result = ping.find("Destination host unreachable.")
        if result<0:
            print ("{}.{}.{}.{} is up ".format(d1,d2,d3,host),file=f)
    f.close()
elif choice == 2:    
    common_ports = { 21, 22, 23, 25, 53, 69, 80, 88, 109, 110,123, 137, 138, 139, 143, 156, 161, 389, 443, 
    445, 500, 546, 547, 587, 660, 995, 993, 2086,2087, 2082, 2083, 3306, 8443, 10000}
    target = str(input ("Enter Targer IP or Domain: "))
    for port in tqdm(common_ports):
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target,port))
        if result == 0 :
            print(port,':',socket.getservbyport(port),' Open',file=f)
    f.close()
    sock.close() 
else:
    print ("Check your choice again")
    