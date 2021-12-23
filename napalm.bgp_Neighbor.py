import json
from napalm import get_network_driver

bgplist = ['10.1.1.1',
           '10.1.1.2',
           '11.11.11.2',
           '12.1.1.2'
           ]

for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'samar', 'samar123')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()
