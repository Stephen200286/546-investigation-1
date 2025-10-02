Note: `splits/` and `httplogs` were generated with `script.py`.

# Commands used so far
* Rank files in splits by size
```console
ls -lSh splits/
```
* Rank files from 172.* network in splits by size
```console
ls -lSh splits/ | grep 172
```
* Rank files from 172.16.7.* (ShieldBase-Clients) by size
```console
ls -lSh splits/ | grep 172.16.7
```
* Rank files from 172.16.6.* (ShieldBase-RD) by size
```console
ls -lSh splits/ | grep 172.16.6
```
*Finding domains accessed via HTTP/+s
tshark -r 20180905_083022.pcap -Y "http.request" -T fields -e http.host   | sort | uniq -c | sort -rn
```
*finding the IP's that have touched the domain Squirldirectory.com and outputted it to a file
$ tshark -r 20180905_083022.pcap -Y '(http.host == "squirreldirectory.com") || (dns.qry.name == "squirreldirectory.com") || (ssl.handshake.extensions_server_name == "squirreldirectory.com")' -T fields -e ip.src -e ip.dst | tr '\t' '\n' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort | uniq -c | sort -rn > squirrel_ips_counts.txt
```
