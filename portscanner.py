import ipaddress
import socket
import termcolor
import os

os.system("clear")
print (termcolor.colored(("\n----------------------------------------------------"), 'blue'))
print (termcolor.colored(("\n---------     P O R T    S C A N N E R     ---------"), 'blue'))
print (termcolor.colored(("\n----------------------------------------------------\n"), 'blue'))

def scan(target, ports):
    print(termcolor.colored(('\n' + '[*] Starting Scan For ' + str(target) + '\n'), 'green'))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored(("[+] Port Opened " + str(port)) , 'green'))
        sock.close()
    except:
        print(termcolor.colored(("[-] Port Closed " + str(port)) , 'red'))

targets = input("[*] Enter Targets To Scan ( Split them by , ) : ")
ports = int(input("[*] Enter How Many Ports You Want To Scan : "))
if ',' in targets:
    print ("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(''), ports)
else:        
    scan(targets,ports)
