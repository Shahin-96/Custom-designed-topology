# -*- coding: utf-8 -*-
"""Networking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tohlkmhBI3soi9FIPNANey_zvgcGS37B
"""

from mininet.net import Mininet
from mininet.node import OVSController
from mininet.node import OVSSwitch
from mininet.node import Host
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import info, setLogLevel

def setup_network():
    # Create Mininet instance
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    C0 = net.addController(name='C0', controller=OVSController, ip='127.0.0.1', protocol='tcp', port=6653)

    info('*** Add switches\n')
    S1 = net.addSwitch(name='S1', cls=OVSSwitch)
    S2 = net.addSwitch(name='S2', cls=OVSSwitch)
    S3 = net.addSwitch(name='S3', cls=OVSSwitch)
    S4 = net.addSwitch(name='S4', cls=OVSSwitch)
    S5 = net.addSwitch(name='S5', cls=OVSSwitch)

    info('*** Add hosts and assign IPs to hosts\n')
    H1 = net.addHost('H1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    H2 = net.addHost('H2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    H3 = net.addHost('H3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    H4 = net.addHost('H4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    H5 = net.addHost('H5', cls=Host, ip='10.0.5.5', defaultRoute=None)
    H6 = net.addHost('H6', cls=Host, ip='10.0.0.6', defaultRoute=None)

    # Host to Switch
    net.addLink(H1, S1, cls=TCLink)
    net.addLink(H2, S2, cls=TCLink)
    net.addLink(H3, S3, cls=TCLink)
    net.addLink(H4, S4, cls=TCLink)
    net.addLink(H5, S4, cls=TCLink)
    net.addLink(H6, S5, cls=TCLink)

    # Switch to Switch
    net.addLink(S1, S2, cls=TCLink)
    net.addLink(S2, S3, cls=TCLink)
    net.addLink(S3, S4, cls=TCLink)
    net.addLink(S3, S5, cls=TCLink)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    for switch in net.switches:
        switch.start([C0])

    # Open CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_network()