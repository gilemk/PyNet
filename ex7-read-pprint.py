#!/usr/bin/env python2
import json
import yaml
from pprint import pprint

def output(my_list, type_of_file):
        print '\n'
        print "#" * len(type_of_file)
        print type_of_file
        print "#" * len(type_of_file)
        print '\n'
        pprint(my_list)

def main():
    with open('test.yml', 'r') as f:
        output((yaml.load(f)), "YAML file")
        
    with open('test.json', 'r') as f:
        output((json.load(f)), "JSON file")

if __name__ == "__main__":
    main()

          
