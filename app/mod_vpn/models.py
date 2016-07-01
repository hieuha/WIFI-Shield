import os
from app import app
from re import search
import ipgetter

VPN_FOLDER = app.config["BASE_DIR"] + "/openvpn/"


def parse_ip(conf):
    if os.path.exists(conf):
        f = open(conf, "r")
        content = f.read()
        try:
            re_ip = search(r'remote(.+?)1194', content)
            ip = str(re_ip.group(1)).strip()
        except Exception, e:
            print e
            ip = None
    return ip


class VPN(object):

    def __init__(self):
        self.vpns = dict()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def status(self):
        pass

    def get_list(self):
        vpn_configs = os.listdir(VPN_FOLDER)
        _vpn = {"conf": None,
               "ip": None,
               "status": None}
        for vpn in vpn_configs:
            conf = VPN_FOLDER + vpn + "/" + "client.ovpn"
            _vpn["conf"] = conf
            _vpn["ip"] = parse_ip(conf)
            self.vpns[vpn] = _vpn
        return self.vpns

    def external_ip(self):
        ip = ipgetter.myip()
        return ip