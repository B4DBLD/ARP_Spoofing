import subprocess
import sys

def detect_arp_spoof(router_ip):
    try:
        command = f"bettercap -eval \"net.sniff on\""
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print("\nDeteniendo el detector de ARP Spoofing")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python detect_arp_spoof.py <IP_Router>")
        sys.exit(1)

    router_ip = sys.argv[1]

    detect_arp_spoof(router_ip)
