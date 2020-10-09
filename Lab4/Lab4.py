import urllib.parse
import http.client
import time

key = "7481QW0APO2BO2BU"  # Put your API Key here


def lab4():
    email = "conorjohnsonmartin@cmail.carleton.ca"
    myLetter = "C"
    myGroup = "L1_F_4"

    params = urllib.parse.urlencode(
        {"field1": email, "field2": myGroup, "field3": myLetter, "key": key}
    )
    
    headers = {
        "Content-typZZe": "application/x-www-form-urlencoded",
        "Accept": "text/plain",
    }
    
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
        
    except:
        print("connection failed")


if __name__ == "__main__":
    lab4()