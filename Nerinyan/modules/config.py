import os
import configparser

class config:
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.default = True
        self.fileName = file
        if os.path.isfile(self.fileName):
            self.config.read(self.fileName, encoding="utf-8")
            self.default = False
        else:
            self.generateConfig()
            self.default = True

    def checkConfig(self, parsedConfig=None):
        if parsedConfig is None:
            parsedConfig = self.config
        
        try:
            parsedConfig.get("osu!", "Id")
            parsedConfig.get("osu!", "Password")
            parsedConfig.get("osu!", "ApiKey")
            
            parsedConfig.get("db", "host")
            parsedConfig.get("db", "username")
            parsedConfig.get("db", "password")
            parsedConfig.get("db", "database")
            return True
        except configparser.Error:
            return False
    
    def generateConfig(self):
        f = open(self.fileName, "w", encoding="utf-8")

        self.config.add_section("osu!")
        self.config.set("osu!", "Id", "CHANGE_HERE")
        self.config.set("osu!", "Password", "CHANGE_HERE")
        self.config.set("osu!", "ApiKey", "CHANGE_HERE")

        self.config.add_section("db")
        self.config.set("db", "host", "localhost")
        self.config.set("db", "username", "CHANGE_HERE")
        self.config.set("db", "password", "CHANGE_HERE")
        self.config.set("db", "database", "CHANGE_HERE")

        self.config.write(f)
        
        f.close()