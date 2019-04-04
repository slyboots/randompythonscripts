#! /usr/local/bin/python3
import sys

def ms_domain_with_dashes_MX_token(domain):
    delimiter = '0'
    token = domain
    hyphen_replace_token = ''
    # split domain in to chunks of 4 chars
    chunk_size = 4
    chunks = [token[i:i+chunk_size] for i in range(0, len(token), chunk_size)]
    # transform the hyphens (their position) in the domain name to an alphanumerical character string
    skip_count = 0
    int_of_a = ord('a') # get the decimal value of the letter 'a' as start value
    for chunk in chunks:
        digit = int_of_a
        for i in range(chunk_size):
            if chunk[i] == '-':
                digit += pow(2, i)
        if int_of_a == digit: # if the value is a it means no hyphen was found
            skip_count += 1
            continue
        if skip_count != 0:
            hyphen_replace_token = hyphen_replace_token + skip_count
        hyphen_replace_token = hyphen_replace_token + chr(digit)
        skip_count = 0 # rewind skip count
    if len(hyphen_replace_token) > 0:
        token = token + (delimiter + hyphen_replace_token)
    token = token.replace('-','')
    token = token.replace('.','-')
    return token

ms_domain_with_dashes_MX_token(sys.argv[1])
