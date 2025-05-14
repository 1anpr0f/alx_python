import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    e_mail=sys.argv[2]
    data={'data':e_mail}
    respose=requests.post(url,data=data)
    print(respose.text)