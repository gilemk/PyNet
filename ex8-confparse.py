#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

def main():
    cfg = CiscoConfParse('cisco_ipsec.txt')
    crypto_cfg = cfg.find_objects(r"^crypto map CRYPTO")
    for i in crypto_cfg:
        print i.text
        for child in i.children:
            print child.text

if __name__ == "__main__":
    main()

          
