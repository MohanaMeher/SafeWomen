import requests
 
url = "https://www.fast2sms.com/dev/bulk"
 
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9901404223"
headers = {
 'authorization': "zR5ZTGM0pyFs7akJ3UDIihn24E6oPBNwCvlWQYK8qSxrdcbHjO3IElUVR5juge2dSOWoF8G97fKyQDiB",
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
 }
 
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)