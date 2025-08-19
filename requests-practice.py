import requests

#r = requests.get('https://xkcd.com/353/')

#print(dir(r))       # shows the attributes and methods that can be accessed
#print(help(r))       # detailed explanation of the object
#print(r.text)

# image url to practice downloading an image
r = requests.get('https://imgs.xkcd.com/comics/python.png')     
#print(r.content)    # this outputs the bytes from the image url
# with open('comic.png', 'wb') as f:  # wb means write bytes
#     f.write(r.content)
# print(r.status_code)       # site response. Output: 200 (Ok)
# print(r.headers)      # headers that come back with the response

##### Advanced features of the requests library
payload = {'page': 2, 'count': 25}
# GET METHOD
r = requests.get('https://httpbin.org/get', params = payload)   # adding "https://httpbin.org/get?page=2&count=25" directly is prompted to errors, that's why we use payload as a dictionary

# print(r.text)
# print(r.url)

# POST METHOD
payload = {'username': 'jimena', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data = payload)   # from get to post, from params to data
# print(r.text)       # json response back from the http bin website
# print(r.json())     # json is a method. It creates a python dictionary from that json response

# it can me captured in a variable (dictionary object)
r_dict = r.json()   
# it allows us to access its elements
#print(r_dict['form'])   # Output: {'password': 'testing', 'username': 'jimena'}

## Basic Auth methods
# Passing credentials for basic authentication
r = requests.get('https://httpbin.org/basic-auth/jimena/testing', auth=('jimena', 'testing'))
#print(r.text)
print(r)    # Output: <Response [200]> --> Ok
# r = requests.get('https://httpbin.org/basic-auth/jimena/testing', auth=('jimenall', 'testing')) # testing an unauthorized credential
# print(r)    # Output: <Response [401]> --> unauthorized response code (which means its working!)

# using timeout 
# r = requests.get('https://httpbin.org/delay/1', timeout=3)
# print(r)
# r = requests.get('https://httpbin.org/delay/6', timeout=3)
# print(r)