import urllib.request
# import urllib.parse
url ='https://alu-intranet.hbtn.io/status'
"""This line creates a Request object for the given url. But it does NOT actually send the request yet."""
response = urllib.request.Request(url)
"""send the request"""
resp=urllib.request.urlopen(response)
respdata = resp.read()#reads the response

print(respdata)