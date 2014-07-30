"""Custom topologies for Mininet

author: Brandon Heller (brandonh@stanford.edu)

To use this file to run a RipL-specific topology on Mininet.  Example:

  sudo mn --custom ~/ripl/ripl/mn.py --topo ft,4
"""

from ripl.dctopo import FatTreeTopo #, VL2Topo, TreeTopo
from mininet.topolib import FatTreeTopo1

topos = { 'ft': FatTreeTopo,
          'fattree': FatTreeTopo1}
#,
#          'vl2': VL2Topo,
#          'tree': TreeTopo }
