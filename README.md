# Hacking OWASP Juice Shop

## Exploring IDOR
I found this endpoint
```
/api/users/{id}
```
which returns any user details by passing its ID,

Request
![request](img/1.png)

response
![alt](img/2.png)

---

```
/api/basket/{id}
```
returns the basket based on given id, i am able to get some one else basket

Request
![alt](img/3.png)

Response
![alt](img/4.png)

---

#   o w a s p - j u i c e - s h o p - n o t e s 
 
 