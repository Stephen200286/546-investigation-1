import pandas as pd
import subprocess
import sys
import re

cmd = "tcpdump -nn -q -r splits/{ip}.pcap host {ip}"
count_cmd = ["wc", "-l"]
#df = pd.read_csv("investigation1.csv", dtype="object")


def create_httplogs(ips, pcap):
    for ip in ips:
        cmd = "tcpdump -nn -r {pcap} host {ip} and port 80 -w httplogs/{ip}.pcap".format(pcap=pcap, ip=ip)
        subprocess.Popen(cmd.split())


def split_pcap_by_host(ips, pcap):
    for ip in ips:
        cmd = "tcpdump -nn -r {pcap} host {ip} -w splits/{ip}.pcap".format(pcap=pcap, ip=ip)
        subprocess.Popen(cmd.split())
        

# # of packets sent+recvd
def populate_row(cmd, df, row):
    for i, ip in enumerate(df["IP"]):
        p1 = subprocess.Popen(cmd.format(ip=ip).split(), stdout=subprocess.PIPE)
        df.loc[i, row] = int(subprocess.check_output(count_cmd, stdin=p1.stdout, text=True))


# Total size of data sent 
def populate_row2(cmd1, cmd2, df, row):
    for i, ip in enumerate(df["IP"]):
        p1 = subprocess.Popen(cmd1.format(ip=ip).split(), stdout=subprocess.PIPE)
        # Get just the size in bytes from the output
        df.loc[i, row] = int(re.search(r'\d+', subprocess.check_output(cmd2.split(), stdin=p1.stdout, text=True)).group())


# Generic function that should have been used in place of the two above
def populate_row3(cmd, df, row):
    for i, ip in enumerate(df["IP"]):
        df.loc[i, row] = subprocess.check_output(cmd.format(ip=ip), shell=True, text=True).strip()

                
#populate_row(cmd, df, "# packets (sent and received)")
#
#populate_row2(
#    "tcpdump -nn -r splits/{ip}.pcap -w - host {ip}", 
#    "capinfos -d -M -",
#    df,
#    "total size of data sent",
#)

#create_httplogs(df["IP"], "DixonsHouse.pcap")

#split_pcap_by_host(df["IP"], "investigation1.pcap")

# User agent row
#populate_row3(
#    "tshark -n -r httplogs/{ip}.pcap -Y http.request -T fields -e http.user_agent | sort | uniq",
#    df,
#    "user-agent",
#)
#
# Number of sites row
#populate_row3(
#    "tshark -n -r splits/{ip}.pcap -T fields -e ip.src ip.src!={ip} | sort | uniq | wc -l",
#    df,
#    "number of sites communicated with",
#)
#
## Top site row
#populate_row3(
#    "tshark -n -r splits/{ip}.pcap -T fields -e ip.src ip.src!={ip} | sort | uniq -c | sort -rn | head -n 1",
#    df,
#    "top site",
#)
#
## Http response code row
#populate_row3(
#    "tshark -n -r httplogs/{ip}.pcap -T fields -e http.response.code | sort | uniq | tr '\n' ' '",
#    df,
#    "response codes",
#)
#
#
## Cookie info row
#for i, ip in enumerate(df["IP"]):
#    out = subprocess.check_output(
#        "tshark -r httplogs/{ip}.pcap -T fields -e http.host -e http.cookie -Y http.cookie".format(ip=ip),
#        shell=True,
#        text=True
#    ).strip()
#    if out == "":
#        df.loc[i, "cookie info"] = "no"
#    else:
#        df.loc[i, "cookie info"] = "yes"
#        
#df.to_csv("test.csv")
