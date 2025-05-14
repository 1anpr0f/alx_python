import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    respose=requests.get(url)
    respose_status = respose.status_code
    if respose_status >= 400:
        print(f'Error code:{respose_status}')
    else:
        print(respose.text)