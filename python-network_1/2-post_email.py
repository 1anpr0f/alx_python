import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    e_mail=sys.argv[2]
    respose=requests.post(url,data=e_mail)
    print(respose.text)