
def get_services():
    import subprocess
    import constant
    pid = []
    service = ""
    mini_list = []
    subprocess_Output = subprocess.check_output("tasklist /svc /FO LIST").decode("utf-8")
    tokens = subprocess_Output.strip().split(constant.SPLIT_BY_2NEWLINE)
    count = 0
    s = 0
    for token in tokens:
        outer = token.strip().split(constant.SPLIT_BY_NEWLINE)
        for token in outer:
            outer_tokens = token.strip().split(constant.SPLIT_BY_NEWLINE)
            for token in outer_tokens:

                if "PID" in token:

                    stripped_token = token.strip('PID:         ')
                    pid.append(stripped_token)
                    s = count
                    count += 1
                elif "Services" in token:

                    service = service + token + ","
                elif "Services" not in token:
                    if "Image Name" not in token:
                        if "PID" not in token:
                            service = service + token + ","

    l = service.strip().split('Services:     ')


    
    res = {}
    for key in pid:
        for value in l:
            if value != '':
                res[key] = value
                l.remove(value)
                break





    return res