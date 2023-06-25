import timeit


def test_before():
    imports = "import requests"
    code = """
for _ in range(10):
    response = requests.get("https://httpbin.org/get", headers={'User-Agent': 'Hello there from pysharper!'})
    print("bob" == "bob")
    print(response.json())
"""

    return timeit.timeit(setup=imports, stmt=code, number=1)


def test_after():
    imports = "import http.client\nimport json"
    code = """
httpbin_org_connection = http.client.HTTPSConnection('httpbin.org')

for _ in range(10):
    httpbin_org_connection.request("GET", "/get", headers={'User-Agent': 'Hello there from pysharper!'})
    response = httpbin_org_connection.getresponse()
    print("bob" == "bob")
    print(json.loads(response.read().decode()))

"""

    return timeit.timeit(setup=imports, stmt=code, number=1)


result_before = test_before()
result_after = test_after()

print(f"Before pysharper {result_before}")
print(f"After pysharper {result_after}")
