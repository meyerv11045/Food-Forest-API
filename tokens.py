from configparser import ConfigParser
import requests
from endpoints import BASE_URL, LOGIN_ENDPOINT

CONFIG_FILE = 'config.ini'

def read_login():
    parser = ConfigParser()
    parser.read(CONFIG_FILE)
    section = 'login'

    if parser.has_section(section):
        return {
            'email': parser.get(section,'email'),
            'password': parser.get(section,'password')
        }
    else:
        raise Exception(f'{section} not found in {CONFIG_FILE}')

def get_new_token(login):
    url = BASE_URL + LOGIN_ENDPOINT
    response = requests.post(url,data=login)
    response.raise_for_status()
    return response.json()['token']

def write_new_token():
    parser = ConfigParser()
    parser.read(CONFIG_FILE)
    section = 'tokens'

    if parser.has_section(section):
        login = read_login()
        token = get_new_token(login)
        parser.set(section,'access',token)
    else:
        raise Exception(f'{section} not found in {CONFIG_FILE}')
    
def read_token():
    parser = ConfigParser()
    parser.read(CONFIG_FILE)
    section = 'tokens'
    if parser.has_section(section):
        return parser.get(section,'access')
    else:
        raise Exception(f'{section} not found in {CONFIG_FILE}')

if __name__ == '__main__':
    write_new_token()