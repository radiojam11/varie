if __name__ == "__main__":
    from urllib.request import urlopen
    import re
    req= urlopen("https://api.openweathermap.org/data/2.5/onecall?lat=42.706924&lon=11.133615&appid=32612558ca8be0629d3b5036523578da&lang=it")
    print(req.read())
    pattern = re.compile(r'href="(.*?)"')
    fd = open("wiki.txt", "w")
    payload = req.read().decode(encoding = 'utf-8')
    fd.write(payload)
    print("sono dopo la conversione\n\n\n\n\n\n")
    print(payload)
    print(pattern)

    fd.close()



"""  
Rispescia Gr
lat = 42.706924
lon = 11.133615
#appID = a672259c17fee6645bcd1953cf9e66c1
appID = 32612558ca8be0629d3b5036523578da

https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={appID}&lang=it&units=metric
-------------------------
&exclude={part}

current
minutely
hourly
daily
alerts
-------------------------
&units=metric

api.openweathermap.org/data/2.5/onecall?lat=30.489772&lon=-99.771335&units=metric
-----------------------
&lang=it

http://api.openweathermap.org/data/2.5/onecall?lat=30.489772&lon=-99.771335&lang=zh_cn


"""