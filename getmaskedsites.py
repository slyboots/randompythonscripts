# /usr/bin/env python3
import os
import json
import requests
START_FROM = int(os.getenv('START_FROM', default=0))
MCP_API=os.getenv('MCP_API')
MCP_API_KEY= os.getenv('MCP_API_KEY')
MCP_QUERY_PARAMS= {
    'ENABLED': True,
    'TEST_SITE': False,
    'fields': ['SITE_DOMAIN']
}

VALID_RESPONSE_HEADERS = {
    'X-Powered-By': 'Otter-Pops'
}

def get_mcp_sites():
    return requests.get(
        MCP_API,
        params=MCP_QUERY_PARAMS,
        auth=requests.auth.HTTPBasicAuth('',MCP_API_KEY)
    ).json()


def valid_headers(headers):
    return headers.get('X-Powered-By') == VALID_RESPONSE_HEADERS.get('X-Powered-By')


def check_sites():
    sites = get_mcp_sites()
    total = len(sites)
    index = START_FROM
    message = ""
    if START_FROM != 0:
        sites = sites[START_FROM:]
    for site in sites:
        index += 1
        print(f"checking site {++index}/{total}...", end='\r', flush=False)
        domain = site['SITE_DOMAIN']
        try:
            response = requests.get(
                f"http://{domain}",
                allow_redirects=True
            )
            headers = response.headers
            if valid_headers(headers):
                pass
            else:
                message = message + f"Invalid headers for {domain}: {json.dumps(dict(response.headers))}\n"
        except requests.exceptions.ConnectionError as err:
            pass
        except requests.exceptions.TooManyRedirects as err:
            pass
    print("")
    print(message)


if __name__ =="__main__":
    check_sites()
