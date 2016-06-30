from app import app
import netifaces


class Device(object):
    def __init__(self):
        self.list_interfaces = dict()

    def interfaces(self):
        for interface in netifaces.interfaces():
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                self.list_interfaces[interface] = link['addr']
        return self.list_interfaces

    def battery(self):
        pass