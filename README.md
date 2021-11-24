# pullhacks

Some hacks to make the job easier :trollface:

![https://media.giphy.com/media/ZZeZA5NeC43870bG9U/giphy.gif](https://media.giphy.com/media/ZZeZA5NeC43870bG9U/giphy.gif)

#### DevOps & Infrastructure

Item                              | URL
--------------------------------- | -------------
AWS                               | [access](https://portswigger.net/web-security)
Ansible                           | [access](https://portswigger.net/web-security)
Kubernetes                        | [access](https://portswigger.net/web-security)
Helm                              | [access](https://portswigger.net/web-security)
Linux                             | [access](https://portswigger.net/web-security)
Terraform                         | [access](https://portswigger.net/web-security)
Vault                             | [access](https://portswigger.net/web-security)

#### Programming

Item                              | URL
--------------------------------- | -------------
Design Patterns                   | [access](https://portswigger.net/web-security)
Go                                | [access](https://portswigger.net/web-security)
Python                            | [access](https://portswigger.net/web-security)
ShellScript                       | [access](https://portswigger.net/web-security)
.NET                              | [access](https://portswigger.net/web-security)

#### Databases

Item                              | URL
--------------------------------- | -------------
Elasticsearch :heavy_check_mark:  | [access](https://github.com/apolzek/pullhacks/tree/main/technology-wiki/databases/elasticsearch)
MongoDB                           | [access](https://portswigger.net/web-security)
Postgres                          | [access](https://portswigger.net/web-security)
Redis                             | [access](https://portswigger.net/web-security)

#### CI/CD & Pipeline

Item                              | URL
--------------------------------- | -------------
GoCD                              | [access](https://portswigger.net/web-security)
GitlabCI                          | [access](https://portswigger.net/web-security)
Github actions                    | [access](https://portswigger.net/web-security)
Jenkins                           | [access](https://portswigger.net/web-security)

## :bookmark: Tools

### k3d

```
https://github.com/scaamanho/k3d-cluster

```

### curl

```
curl -w "@curl-format.txt" -o /dev/null -s "http://wordpress.com/"
```

save: curl-format.txt

```

     time_namelookup:  %{time_namelookup}s\n
        time_connect:  %{time_connect}s\n
     time_appconnect:  %{time_appconnect}s\n
    time_pretransfer:  %{time_pretransfer}s\n
       time_redirect:  %{time_redirect}s\n
  time_starttransfer:  %{time_starttransfer}s\n
                     ----------\n
          time_total:  %{time_total}s\n
```

### httpie

```
https://httpie.io/
https://httpie.io/docs


http PUT pie.dev/put X-API-Token:123 name=John
http -f POST pie.dev/post hello=World
http -v pie.dev/get
http --offline pie.dev/post hello=offline
http -a USERNAME POST https://api.github.com/repos/httpie/httpie/issues/83/comments body='HTTPie is awesome! :heart:'
http pie.dev/post < files/data.json
http --download pie.dev/image/png
http --session=logged-in -a username:password pie.dev/get API-Key:123
http https://api.github.com/search/repositories q==httpie per_page==1
```

### k6s

### Tor

```
# Config Tor Terminal Linux
https://justhackerthings.com/post/using-tor-from-the-command-line/
https://webhook.site/

torify curl ifconfig.me
curl ifconfig.me
google-chrome-stable --proxy-server="socks://127.0.0.1:9050
```
