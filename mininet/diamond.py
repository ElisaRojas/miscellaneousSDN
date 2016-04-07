#!/usr/bin/python

from mininet.topo import Topo

class DiamondTopo( Topo ):
    "Diamond topology"

    def __init__( self ):
        "Custom diamond topology, with 4 switches and 2 hosts"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        h1 = self.addHost( 'h1' , mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'h2' , mac='00:00:00:00:00:02' )

        #   Add Switches
        s1 = self.addSwitch( 's1' , dpid="0000000000000001" )
        s2 = self.addSwitch( 's2' , dpid="0000000000000002" )
        s3 = self.addSwitch( 's3' , dpid="0000000000000003" )
        s4 = self.addSwitch( 's4' , dpid="0000000000000004" )

        #   Add links between hosts and swiches
        self.addLink( h1, s1 )
        self.addLink( h2, s4 )
        

        #   Add links between switches
        self.addLink( s1, s2 )
        self.addLink( s1, s3 )
        self.addLink( s2, s4 )
        self.addLink( s3, s4 )


topos = { 'diamond': ( lambda: DiamondTopo() ) }