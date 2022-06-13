# tcpdump

```
# HTTP GET
tcpdump -i any -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'

# HTTP POST:
tcpdump -i any -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504F5354'
```

```
netstat -ltnp | grep -w ':<PORT>' 
netstat -ltnp | grep -w ':<80>' 

lsof -i :<PORT>
lsof -i :53

fuser 80/tcp


nc -vl 2222
# fuser 2222/tcp
ps -p 173667 -o comm=


sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo ss -tulpn | grep LISTEN
sudo lsof -i:<PORT>
sudo nmap -sTU -O <IP>
sudo lsof -i -P -n
sudo ss -tulwn


netstat -tulpn
```
