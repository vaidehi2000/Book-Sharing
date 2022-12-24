def validate_ip(ip):
    for i in ip:
        try:
            int(i)
        except ValueError:
            return False
    return True


def validate_port(port):
    try:
        int(port)
    except ValueError:
        return False
    return True


def validate_ip_port(PORT, HOST):
    RETURN_HOST = HOST
    RETURN_PORT = PORT
    IP_VALIDATION = True
    PORT_VALIDATION = False
    if HOST == "0":
        IP_VALIDATION = True
        RETURN_HOST = "localhost"
    else:
        IP_VALIDATION = validate_ip(HOST)
    IP_VALIDATION = True
    PORT_VALIDATION = validate_port(PORT)
    if IP_VALIDATION and PORT_VALIDATION:
        return True, RETURN_HOST, RETURN_PORT
    else:
        return False, None, None
