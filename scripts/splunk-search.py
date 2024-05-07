import splunklib.client as client


# credentials:
URL = "[prd-p-ohwzh.splunkcloud.com]"
USER_NAME = "sc_admin"
PASSWORD = "password"
PORT = '8089'

try:
    service = client.connect(host=URL, port=PORT, username=USER_NAME, password=PASSWORD)
    print(str(service))
except Exception as e:
    print("Exception occurred " + str(e))


for app in service.apps:
    print(app.name)





