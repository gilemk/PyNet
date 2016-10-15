#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

def main():
    cfg = CiscoConfParse('cisco_ipsec.txt')
    crypto_not_AES = cfg.find_objects_wo_child(r"^crypto map CRYPTO", r"set transform-set AES")
    print "Crypto maps not using AES:"
    for line in crypto_not_AES:
        transform_set = line.re_search_children(r"transform")[0].text.split()[-1]
        print line.parent.text + ">>>>> " + transform_set

if __name__ == "__main__":
    main()

          
