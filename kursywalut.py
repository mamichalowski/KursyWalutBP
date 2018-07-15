import http.client

conn = http.client.HTTPConnection('api.nbp.pl')

headers = {
    'Accept': "application/xml",
    'Cache-Control': "no-cache",
    'Postman-Token': "0f54923d-d330-4469-994e-6945641faed1"
    }

conn.request("GET", "/api/exchangerates/tables/A", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))