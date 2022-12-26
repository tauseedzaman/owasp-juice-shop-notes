# Hacking OWASP Juice Shop

## Exploring IDOR

I found this endpoint

```
GET /api/users/{id}
```

which returns any user details by passing its ID,

Request
![request](img/1.png)

response
![alt](img/2.png)

---

```
GET /api/basket/{id}
```

returns the basket based on given id, i am able to get some one else basket

Request
![alt](img/3.png)

Response
![alt](img/4.png)

---

```
DELETE /api/BasketItems/6
```

allows user to delete any item from cart/basket based on its ID,so i am able to delete some one else cart item

Request:

![alt](img/5.png)

Response:
![alt](img/6.png)

---

```
PUT /api/BasketItems/11
```

allows me to encrement the product quantity of someone else cart/basket

Request:
![alt](img/7.png)

Response
![alt](img/8.png)

---
