import configparser

config = configparser.ConfigParser()

config.read("config.ini")

for key in config["DEV"]:
    print(key)
