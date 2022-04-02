import os
import sys
import configparser
 
config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)
 
 
def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix
 
 
def my_prefix():
    try:
        prefix = get_prefix()
    except configparser.NoSectionError:
        config.add_section("prefix")
        config.set("prefix", "prefix", "!")
        with open(config_path, "w") as config_file:
            config.write(config_file)
        prefix = "!"
    return prefix