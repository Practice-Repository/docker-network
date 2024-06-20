import requests

url = "http://" + input("http://[ ]:8080/\n") + ":8080/"

try:
    response = requests.get(url)

except:
    print("リクエストに失敗しました")
    print("リクエストURLが間違っているか、サーバーが起動していない可能性があります")
    exit()

if response.status_code == 200:
    print("リクエストに成功しました")
    print(response)
    print(response.json())

else:
    print("リクエストに失敗しました")
    print(response)
