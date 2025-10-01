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
