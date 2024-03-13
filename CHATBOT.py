import json 
import requests
import time

a = 1

while a < 5:
    url_webex ="https://webexapis.com/v1/messages"
    
    payload=json.dumps({
        "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNTA1NThkNzAtZTA5Zi0xMWVlLWE0OTMtNzc0NmQ0MjE0NTdi",
        "text": 'Ya ando enviando mensajes',
        "text": "Esta prueba contine envio de mensajes cada 30 segundos"
    
    })
    headers={
        'Authorization': 'Bearer  NjMwODk3ZDItOTYxOS00YWE0LWI2NGUtNGRjNzUyMTBkNzg5ODU4NjE5ZjYtODRm_PF84_86f111f1-d448-4e12-ba22-5d295d6f5cf1',
        'Content-Type': 'application/json'
        }
    requests.request("POST", url_webex,headers=headers, data=payload)
    a =1
    time.sleep(30)
