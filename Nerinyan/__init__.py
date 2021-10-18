import pathlib
import sys
import logging as syslog

from colored import fore, back, style
from Nerinyan.common import glob, logging
from Nerinyan.modules import config

loggingFormat = fore.BLACK + back.GREEN_YELLOW + " [ %(levelname)s ] " + style.RESET + "|" + fore.GREY_37 + back.WHITE + " %(asctime)s " + style.RESET + "|| %(message)s"

syslog.basicConfig(
    format=loggingFormat,
    level=syslog.INFO)
LOGGER = syslog.getLogger(__name__)

def ASCII_ART():
    print(fore.LIGHT_BLUE, " _   _           _                         ")
    print(fore.LIGHT_BLUE, "| \ | |         (_)                        ")
    print(fore.LIGHT_BLUE, "|  \| | ___ _ __ _ _ __  _   _  __ _ _ __  ")
    print(fore.LIGHT_BLUE, "| . ` |/ _ \ '__| | '_ \| | | |/ _` | '_ \ ")
    print(fore.LIGHT_BLUE, "| |\  |  __/ |  | | | | | |_| | (_| | | | |")
    print(fore.LIGHT_BLUE, "\_| \_/\___|_|  |_|_| |_|\__, |\__,_|_| |_|")
    print(fore.LIGHT_BLUE, "                          __/ |            ")
    print(fore.LIGHT_BLUE, "                         |___/             ")
    print(style.RESET,       "============================================\n")

def CONFIG_LOADER():
    conf = config.config(str(glob.BASEROOT) + "/config.ini")
    if conf.default:
        logging.ConsoleLog("warn", "config", "config.ini is not found. A default one has been generated.")
        sys.exit()
    if not conf.checkConfig():
        logging.ConsoleLog("warn", "config", "Invaild config.ini. Please configure it properly")
        logging.ConsoleLog("warn", "config", "Delete config.ini to generate a default one.")
        sys.exit()

    glob.OSU_ACCOUNT = {
        "id": conf.config['osu!']['Id'],
        "password": conf.config['Password'],
        "api_key": conf.config['ApiKey']
    }
    glob.SQL_HOST = conf.config['db']['host']
    glob.SQL_USER = conf.config['db']['username']
    glob.SQL_PASS = conf.config['db']['password']
    glob.SQL_DB = conf.config['db']['database']

    if any(not i for i in [glob.OSU_ACCOUNT, glob.SQL_HOST, glob.SQL_USER, glob.SQL_PASS, glob.SQL_DB]):
        logging.ConsoleLog("danger", 'config', "Config load Failed.")
        sys.exit()

ASCII_ART()
glob.BASEROOT = pathlib.Path(__file__).parent.parent
CONFIG_LOADER()