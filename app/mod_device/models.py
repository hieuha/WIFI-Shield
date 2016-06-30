from app import app
import netifaces


class Device(object):
    def __init__(self):
        pass


    @staticmethod
    def interfaces():
        lst_interfaces = dict()
        for interface in netifaces.interfaces():
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                lst_interfaces[interface] = link['addr']
        return lst_interfaces
