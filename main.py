# from configparser import ConfigParser

import subprocess
from pyvda import AppView, get_apps_by_z_order, VirtualDesktop, get_virtual_desktops

class MakeMaximus:
    def __init__(self, config) -> None:
        self.window_names = ["Main Desktop", "Ramims", "Game Dev", "NWBS Updates"]
        

        self.window_settings = {
            "Main Desktop": {
                "apps": "Any"
                },
            "Ramims": {
                "apps": ["code", "chrome", "cmd"],
                "folder": r"/MummyRach",
                "window_sizes": {
                    "code": (1000, 500),
                    "chrome": (1000, 500),
                    "cmd": (700, 300)
                }
                }
        }

    def create_virtual_desktops(self):
        active_desktops = len(get_virtual_desktops())

        # if active_desktops > 1:
        #     return self.recreate_environments()

        for window_name in self.window_names:
            virtual_desktop = VirtualDesktop.create()
            virtual_desktop.rename(window_name)

    
    def place_apps(self):
        active_desktops = get_virtual_desktops()

        # check for null desktop names
        
        for desktop in active_desktops:
            # print(desktop.name)
            try:
                if self.window_settings[desktop.name]:
                    target_desktop = VirtualDesktop(desktop.number)
                    target_desktop.go()
                    subprocess.Popen(["code"])
                    self.window_settings[desktop.name]
            except KeyError:
                continue




maximus = MakeMaximus("hello")
# maximus.create_virtual_desktops()
maximus.place_apps()

# theconfig = ConfigParser()
# print(theconfig.read("maximus_config.ini")) 
# print(theconfig.sections())