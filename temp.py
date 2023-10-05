# text file handling
# To close a file, we use the close() function in Python. The syntax for the close() function is <file_pointer>.close(<filename>). Closing a file is important as it saves the changes made to the file and frees up the file.
# to open a file =>
# <file_object_name> = open(<file_path>)

# The flush() function saves the changes made to the file. The difference between flush() and close() is that flush() doesn’t close the file.
# <file_object_name>.close()
# <file_object_name>.flush()


# =======================================================================================

# handling http requests
# import requests
# ========================== get an response from https://imgs.xkcd.com/comics/python.png ===============================================

'''(1) playing with the response object'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(site_response)

# output =>
# <Response [200]>


'''(2) playing with the response object content'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(dir(site_response))

# output =>
# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']


'''(3) saves it as comic.png file in the path'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open ('comic.png', 'wb') as file:
# 	file.write(site_response.content)


'''(4) prints the numeric content in the img file'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(site_response.content)

# output => (it's something huge like this text)
# a\xb0]\xa3\x16\x1b\x9d\xfbv\xd0\xf9zG!gp9


'''(5) prints the status code of the response'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(site_response.status_code)

# output => 200 (means ok)
# there are hundreds of other status codes
# 100s are for informal
# 200s are for success
# 300s are for redirects
# 400s are for client side error
# 500s are for server side error


'''(6) ok method return true if the status code of the response is less than 400'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(site_response.ok)

# output =>
# True


'''(6) ok method return true if the ststus code of the response is 200'''
# site_response = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(site_response.ok)


# text1 = 'this is for my love sumona\n'
# text2 = 'this is for my mother\n'
# with open('newfile.txt', 'w') as myfile:
# 	myfile.write(text1)
# with open('newfile.txt', 'w') as myfile2:
# 	myfile2.write(text2)

# myfile = open('newfile.txt')
# file_content = myfile.read()
# print(type(file_content))

#=================================================================================
# import json
# data = json.loads( open('sample.txt', 'r').read() )
# for contest in data['result']:
# 	print(contest['name'], ' - ', contest['startTimeSeconds'])

# output =>
# Codeforces Round (Div. 1)  -  1696755900
# Codeforces Round (Div. 2)  -  1696755900
# Codeforces Round (Div. 1)  -  1696084500
# Codeforces Round (Div. 2)  -  1696084500
# Codeforces Round (Div. 3)  -  1695738900


# import time
# start = time.time()
# # print('starting time =', start)
# for i in range(10000000):		# 0.01694345474243164
# 	pass
# end = time.time()
# print('time span =', end - start)

# import json
# data_dict = json.load(open('info/user_info.json', 'r')) # loading data from json file
# data_str = json.dumps(data_dict, indent=4) # dump as string 
# print(type(data_str))
# print(data_str)

