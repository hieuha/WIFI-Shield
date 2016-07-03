# WIFI Shield
### Setups
```
sudo -s
cd /opt/
git clone https://github.com/hieuha/WIFI-Shield.git
```

Auto Starting This Program As A Daemon Service
```
crontab -e
@reboot /usr/bin/python /opt/WIFI-Shield/run.py
```

### Enable Network Forwarding
```
sudo -s
echo 1 > /proc/sys/net/ipv4/ip_forward
echo "net.ipv4.ip_forward=1" > /etc/sysctl.conf
sysctl -p
```

### Routing Network With Iptables
```
iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT


iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE
iptables -A FORWARD -i tun0 -o wlan1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan1 -o tun0 -j ACCEPT
```


## Screenshots
![WIFI-Shield](http://i.imgur.com/98zcwlk.png)
![Dashboard](http://i.imgur.com/QZJ0CTq.png)
![Wifi Configuration](http://i.imgur.com/eGtCt1i.png)
