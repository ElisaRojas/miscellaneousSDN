"""Comb topology
"""

from mininet.topo import Topo

class TriangleTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create triangle topo."

        # Initialize topology
        Topo.__init__(self)

	s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')

	h1 = self.addHost('h1')
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')

	self.addLink(s1, s2)
	self.addLink(s1, s3)
	self.addLink(s2, s3)

	self.addLink(s1, h1)
	self.addLink(s2, h2)
	self.addLink(s3, h3)

topos = { 'triangle': ( lambda: TriangleTopo() ) }

