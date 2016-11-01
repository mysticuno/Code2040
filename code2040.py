import requests

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
	a string to reverse, reverses it, and posts the result to
	http://challenge.code2040.org/api/validate
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

register()
reverse()