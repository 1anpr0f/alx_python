import requests
import sys
if __name__ == '__main__':
    url=sys.argv[1]
    the_data=requests.get(url)
    print(the_data.request.get('X-Request-Id'))