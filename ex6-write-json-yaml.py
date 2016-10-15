#!/usr/bin/env python
import json
import yaml

def main():
    my_list = range(10)
    my_list.append('Router')
    my_list.append({})
    my_list[-1]['ip address'] = '10.10.10.10'
    my_list[-1]['vendors'] = ['juniper', 'cisco', 'arista']
    my_list.append('Switch')

    with open('test.yml', 'w') as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open('test.json', 'w') as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    main()

          
