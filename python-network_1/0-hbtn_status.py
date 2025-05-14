import requests
url='https://alu-intranet.hbtn.io/status'
#	Retrieve data
the_data = requests.get(url)
print(the_data.text)
print(the_data.status_code)
