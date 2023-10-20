# from configparser import ConfigParser

import subprocess
import os
from configparser import ConfigParser
from pyvda import AppView, get_apps_by_z_order, VirtualDesktop, get_virtual_desktops

class MakeMaximus:
    def __init__(self, config) -> None:
        self.config = config
        self.config_parser = ConfigParser()
        self.config_parser.read(self.config)
        

        # set default settings
        setattr(self, "default_settings", self.config_parser["DefaultSettings"])

        self.desktops_only = [desktop for desktop in self.config_parser.sections() if desktop.startswith("Desktop.")]

        for desktop_name in self.desktops_only:
            setattr(
                self, 
                desktop_name.split(".")[-1], 
                self.config_parser["Desktop." + desktop_name.split(".")[-1]]
            )
        
    def create_virtual_desktops(self):
        active_desktops = len(get_virtual_desktops())
        
        print(len(get_virtual_desktops()))
        for desktop in get_virtual_desktops():
            try:
                if getattr(self, desktop.name):
                    self.desktops_only.pop(self.desktops_only.index("Desktop." + desktop.name))
                
            except AttributeError:
                continue
        print(len(get_virtual_desktops()))
        #if active_desktops > 1:
        #     return self.recreate_environments()
        
        for window_name in self.desktops_only:
            virtual_desktop = VirtualDesktop.create()
            virtual_desktop.rename(self.config_parser[window_name]["desktop_name"])

    
    def place_apps(self):
        active_desktops = get_virtual_desktops()

        # check for null desktop names
        
        for desktop in active_desktops:
            # print(desktop.name)
            try:
                if getattr(self, desktop):
                    target_desktop = VirtualDesktop(desktop.number)
                    target_desktop.go()
                    os.system("start cmd.exe")
            except KeyError:
                continue




maximus = MakeMaximus("maximus_config.ini")
maximus.create_virtual_desktops()
#maximus.place_apps()
