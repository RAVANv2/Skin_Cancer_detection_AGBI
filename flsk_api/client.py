import requests


my_file = {'src':'./4.jpg'}

ans = requests.post("http://127.0.0.1:5000/", json=my_file)

print(ans.json())
