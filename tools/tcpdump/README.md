# tcpdump

```
# HTTP GET
tcpdump -i any -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'

# HTTP POST:
tcpdump -i any -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504F5354'
```