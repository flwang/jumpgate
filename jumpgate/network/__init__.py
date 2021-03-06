

def add_endpoints(disp):
    # V2 API - http://api.openstack.org/api-ref-networking.html

    disp.add_endpoint('v2_networks', '/v2.0/networks.json')
    disp.add_endpoint('v2_subnets', '/v2.0/subnets.json')
    disp.add_endpoint('v2_subnet', '/v2.0/subnets/{subnet_id}')
