import requests
import json

def register():
	"""
	Makes a POST request to http://challenge.code2040.org/api/register and prints
	the response text
	"""
	url = "http://challenge.code2040.org/api/register"
	data = {"token": "a061df4b77bfec12bc1ec34d70cba02b", \
			"github": "https://github.com/mysticuno/Code2040"}
	res = requests.post(url, data=data)
	print(res.text)

def reverse():
	"""
	Makes a POST request to http://challenge.code2040.org/api/reverse to obtain
	a string to reverse, reverses it, and POSTs the result to
	http://challenge.code2040.org/api/reverse/validate
	"""
	url = "http://challenge.code2040.org/api/reverse"
	data = {"token": "a061df4b77bfec12bc1ec34d70cba02b"}
	res = requests.post(url, data=data)
	reverse = res.text[::-1]
	print(reverse)

	# Post the reversed string
	validate = "http://challenge.code2040.org/api/reverse/validate"
	val_data = {"token": "a061df4b77bfec12bc1ec34d70cba02b",\
				"string": reverse}
	val_res = requests.post(validate, data=val_data)
	print(val_res.text)

def haystack():
	"""
	Makes a POST request to http://challenge.code2040.org/api/haystack to obtain
	a string and a list, finds the index of the string in the list, and POSTs the
	result to http://challenge.code2040.org/api/haystack/validate
	"""
	url = "http://challenge.code2040.org/api/haystack"
	data = {"token": "a061df4b77bfec12bc1ec34d70cba02b"}
	res = requests.post(url, data=data)
	
	res_dict = json.loads(res.text)
	needle, haystack = res_dict['needle'], res_dict['haystack']
	index = haystack.index(needle) #finds first instance of needle
	print(haystack, needle, index)

	validate = "http://challenge.code2040.org/api/haystack/validate"
	val_data = {"token": "a061df4b77bfec12bc1ec34d70cba02b", "needle": index}

	val_res = requests.post(validate, data=val_data)
	print(val_res.text)

def prefix():
	"""
	Makes a POST request to http://challenge.code2040.org/api/prefix to obtain a
	prefix and a list of strings, creates a list of string that do NOT begin with
	that prefix, and POSTs the resulting list, preserving order, to 
	http://challenge.code2040.org/api/prefix/validate
	"""
	url = "http://challenge.code2040.org/api/prefix"
	data = {"token": "a061df4b77bfec12bc1ec34d70cba02b"}
	res = requests.post(url, data=data)
	
	res_dict = json.loads(res.text)
	prefix, array = res_dict['prefix'], res_dict['array']
	print(prefix, array)
	not_prefix = [string for string in array if not string.startswith(prefix)]
	print(not_prefix)

	validate = "http://challenge.code2040.org/api/prefix/validate"
	val_data = {"token": "a061df4b77bfec12bc1ec34d70cba02b", "array": not_prefix}

	val_res = requests.post(validate, json=val_data)
	print(val_res.text)

register()
reverse()
haystack()
prefix()
