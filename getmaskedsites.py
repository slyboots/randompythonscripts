# /usr/bin/env python3
import os
import requests

MCP_API=os.getenv('MCP_API')
MCP_API_KEY= os.getenv('MCP_API_KEY')

MCP_QUERY_PARAMS= {
    'ENABLED': True,
    'TEST_SITE': False,
    'fields': ['SITE_DOMAIN']
}

def get_mcp_sites():
    return requests.get(
        MCP_API,
        params=MCP_QUERY_PARAMS,
        auth=requests.auth.HTTPBasicAuth('',MCP_API_KEY)
    )


if __name__ =="__main__":
    sites = get_mcp_sites()
    print(sites.json())
