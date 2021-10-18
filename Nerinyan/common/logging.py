import datetime
from colored import fore, back, style

def ConsoleLog(Type = None, Prefix = None, *contents):
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = ""
    Type = Type.lower()

    if Prefix == None:
        if Type == "index" or Type == "normal" or Type == "ok" or Type== "index" or Type == None:
            content += f"{fore.BLACK}{back.CYAN_3} [ INDEX ] {style.RESET}"
        elif Type == "warning" or Type == "war" or "warn":
            content += f"{fore.BLACK}{back.YELLOW_3A} [ WARNING ] {style.RESET}"
        elif Type == "dangerous" or Type == "danger" or "error":
            content += f"{fore.BLACK}{back.RED_3A} [ DANGEROUS ] {style.RESET}"
    else:
        Prefix = Prefix.upper()
        if Type == "index" or Type == "normal" or Type == "ok"or Type== "index" or Type == None:
            content += f"{fore.BLACK}{back.CYAN_3} [ {Prefix} ] {style.RESET}"
        elif Type == "warning" or Type == "war" or "warn":
            content += f"{fore.BLACK}{back.YELLOW_3A} [ {Prefix} ] {style.RESET}"
        elif Type == "dangerous" or Type == "danger" or "error":
            content += f"{fore.BLACK}{back.INDIAN_RED_1A} [ {Prefix} ] {style.RESET}"

    content += f"|{fore.GREY_37}{back.WHITE} {nowtime} {style.RESET}|| "

    for i in contents:
        if i == contents[0]:
            content += fore.LIGHT_YELLOW + i
        else:
            content += f"{fore.LIGHT_YELLOW}, " + i

    print(f"{fore.LIGHT_YELLOW}{content}{style.RESET}")