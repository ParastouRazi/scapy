from scapy.all import srp,Ether,ARP,conf

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2 ,iface="Wi-Fi")
for s,r in ans:
    print(r.sprintf("%ARP.hwsrc% %ARP.psrc%"))
