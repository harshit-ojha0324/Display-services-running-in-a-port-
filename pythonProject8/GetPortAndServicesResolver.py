import subprocess
import constant
def get_ports():
    sub_output = subprocess.check_output("netstat -ano").decode('utf-8')

    token = (sub_output.split(constant.SPLIT_BY_2NEWLINE))

    li = []

    li2 = []

    for tokens in token:

        sub_token = tokens.split(constant.SPLIT_BY_NEWLINE)

        for item in sub_token:

            if "ESTABLISHED" in item:      #Get established ports

                li.append(item)

            elif "LISTENING" in item:      #Get listening ports

                li.append(item)
    '''li is a list that stores the string containing ports in format 
      Proto  Local Address          Foreign Address        State           PID'''
    for item in li:

        a = item.split(" ")

        for item in a:

            if (len(item) != 0):

                li2.append(item)
    '''li2 is a list that stores the string containing ports in format(seperately)
    Proto  Local Address          Foreign Address        State           PID'''
    count = 0

    ports = []

    pid = []

    counter = 0

    x = 0 #looping element

    while (x < len(li2)):

        x += 1

        if (x == 1): #"since the first index of ports is 1 and then every 5th element from that is also a port"

            ports.append(li2[x])

            count = x + 5

        elif (count == x): #catch the rest of ports

            ports.append(li2[x])

            count = x + 5

        if (x == 4):  #"since the first index of pid is 1 and then every 5th element from that is also pid"

            pid.append(li2[x])

            counter = x + 5

        elif (x == counter): #catch the rest of pid

            pid.append(li2[x])

            counter = x + 5
    looping_element = -1

    purt = []

    str = ""

    for item in ports:

        s = item

        length = -len(s)

        for looping_element in range(-1, length, -1):

            while s[looping_element] != ":":

                str = str + s[looping_element]

                looping_element -= 1

            purt.append(str[::-1]) #reverse the string

            break

        str = ""

    pids = pid

    res = {} #dictionary having ports as key and pid as index

    for key in purt:

        for value in pids:

            res[key] = value

            pids.remove(value)

            break

    return res
