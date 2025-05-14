import requests
url='https://alu-intranet.hbtn.io/status'
#	Retrieve data
the_data = requests.get(url)
print("Body response:")
print("\t- type:", type(the_data.text))
print("\t- content:", the_data.text)
