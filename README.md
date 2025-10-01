# Commands used so far
* Rank files in splits by size
```console
ls -lSh splits/
```
* Rank files from 172.* network in splits by size
```console
ls -lSh splits/ | grep 172
```
tshark -r 20180905_083022.pcap -Y "tcp.port == 514" -T fields -e ip.src -e ip.dst | sort | uniq -c | sort -nr | head
- shows 
