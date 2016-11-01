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


register()
