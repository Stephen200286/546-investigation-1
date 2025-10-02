import pandas as pd
import subprocess
import sys
import re

def split_pcap_by_host(ips, pcap):
    for ip in ips:
        cmd = "tcpdump -nn -r {pcap} host {ip} -w splits/{ip}.pcap".format(pcap=pcap, ip=ip)
        subprocess.Popen(cmd.split())

def create_httplogs(ips, pcap):
    for ip in ips:
        cmd = "tcpdump -nn -r {pcap} host {ip} and port 80 -w httplogs/{ip}.pcap".format(pcap=pcap, ip=ip)
        subprocess.Popen(cmd.split())

#df = pd.read_csv("ips.csv", dtype="object")
#split_pcap_by_host(df["IP"], "investigation1.pcap")

#df = pd.read_csv("ShieldBase-Clients.csv", dtype="object")
#create_httplogs(df["IP"], "investigation1.pcap")

df = pd.read_csv("ShieldBase-RD.csv", dtype="object")
create_httplogs(df["IP"], "investigation1.pcap")
