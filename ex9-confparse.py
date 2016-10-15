#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

def main():
    cfg = CiscoConfParse('cisco_ipsec.txt')
    crypto_group2 = cfg.find_objects(r"pfs group2")
    print "PFS group2 found in the following crypto maps:"
    for line in crypto_group2:
        print line.parent.text

if __name__ == "__main__":
    main()

          
