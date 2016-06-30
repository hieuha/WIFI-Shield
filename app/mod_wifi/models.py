from app import app
from wifi import Cell, Scheme


class Wifi:
    def __init__(self):
        self.ssid = ""
        self.password = ""
        self.interface = app.config["INTERFACE"]
        self.networks = {"ssid": [], "message": None, "error": False}
        self.cells = None

    def scan(self):
        message = None
        error = False
        network = list()
        try:
            self.cells = Cell.all(self.interface)
            for n in self.cells:
                ssid = n.ssid
                if ssid is not None and ssid != "":
                    network.append(ssid)
            self.networks["ssid"] = network
        except Exception, e:
            self.networks["message"] = e
            self.networks["error"] = True
        return self.networks

    def connect(self):
        cell = None
        message = None
        error = False
        if self.ssid != "":
            for i,v in enumerate(self.cells):
                if v.ssid == self.ssid:
                    cell = self.cells[i]
                    break
        if cell:
            scheme = None
            if cell.encrypted:
                if self.password != "":
                    scheme = Scheme.for_cell(self.interface, "home", cell, passkey=self.password)
            else:
                scheme = Scheme.for_cell(self.interface, "home", cell)
            if scheme:
                try:
                    scheme.delete()
                    scheme.save()
                    try:
                        scheme.activate()
                        message = "OK"
                        error = False
                    except Exception, e:
                        message = e
                        error = True
                except Exception, e:
                    message = e
                    error = True

        return message, error
