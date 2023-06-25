import requests

for _ in range(10):
    response = requests.get("https://httpbin.org/get", headers={'User-Agent': 'Hello there from pysharper!'})
    print("bob" == "bob")
    print(response.json())
