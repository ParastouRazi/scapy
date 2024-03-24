Here is my tests for scapy with codes and videos
Scapy Arp Scanner

install scapy:
pip install scapy

install pyinstaller to convert python to exe:
pip install pyinstaller

With below command we convert :
pyinstaller -F scapyarp.py

https://github.com/ParastouRazi/scapy/assets/85788536/f1f7a80d-bec9-4578-9883-a1d3bd92140a

compelte video in youtube channel:

https://www.youtube.com/watch?v=EVW0mPw95ko

Scapy Arp spoofing:

https://www.youtube.com/watch?v=It_uqdrjx8U

`pdst` : IP Victim --A

`hwdst` : MAC Victim 

`hwsrc`: MAC Attacker

`Psrc` : IP gatewate (destination for sniffing)--B



`sr()` function is used to send a packet or group of packets when you expect a response back

`srloop()`  will send the L3 packet and continue to resend the packet after each response is received.

`send()` Send packets at Layer 3(Scapy creates Layer 2 header), Does not recieve any packets.

`sendp()` Same as send() but sends packets at Layer 2(Must provide Layer 2 header), Does not recieve any packets


First packet:
pari=IP(dst="192.168.1.162")
pari/=TCP(dport=445)
sr1(pari)


Seconde packet:
pari2=IP(src="192.168.1.62" ,dst="192.168.1.162")
pari2/=TCP(dport=445)
pari2/=Raw(load="Test scapy by parastou Razi")
sr1(pari2)


Arp scan :
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2 ,iface="ens33")
ans.show()


Changing Mac address
p5 = Ether(src="AA:AA:AA:AA:AA:AA")/IP(dst="192.168.1.162")/TCP(dport=1434)
sendp(p5)

Video :




