import json
import http.client

httpbin_org_connection = http.client.HTTPSConnection('httpbin.org')

for _ in range(10):
    httpbin_org_connection.request("GET", "/get", headers={'User-Agent': 'Hello there from pysharper!'})
    response = httpbin_org_connection.getresponse()
    print("bob" == "bob")
    print(json.loads(response.read().decode()))
