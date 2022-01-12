```
https://httpie.io/
https://httpie.io/docs
```

`http [flags] [METHOD] URL [ITEM [ITEM]]`

```
# Custom HTTP method, HTTP headers and JSON data:
http PUT pie.dev/put X-API-Token:123 name=John

# Submitting forms:
http -f POST pie.dev/post hello=World

http -v pie.dev/get
http --offline pie.dev/post hello=offline
http -a USERNAME POST https://api.github.com/repos/httpie/httpie/issues/83/comments body='HTTPie is awesome! :heart:'
http pie.dev/post < files/data.json
http --download pie.dev/image/png
http --session=logged-in -a username:password pie.dev/get API-Key:123
http https://api.github.com/search/repositories q==httpie per_page==1
```

```
git clone https://github.com/apolzek/api-books-dotnet.git
cd api-books-dotnet
docker-compose up -d
```

```
curl -X GET "http://0.0.0.0:4000/api/Books" -H  "accept: text/plain"
http GET "http://0.0.0.0:4000/api/Books" accept:text/plain
```