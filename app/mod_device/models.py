from app import app
import netifaces
import subprocess

class Device(object):
    def __init__(self):
        self.list_interfaces = dict()

    def interfaces(self):
        for interface in netifaces.interfaces():
            try:
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    self.list_interfaces[interface] = link['addr']
            except Exception, e:
                pass
        return self.list_interfaces

    def battery(self):
        pass

    def check_internet(self):
        try:
            output = subprocess.Popen(["/bin/ping", "-c 1", "google.com"], stdout=subprocess.PIPE).communicate()
            output = str(output[0]).strip()
            if "" == output:
                return False
            return True
        except:
            return False