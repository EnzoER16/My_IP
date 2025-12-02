import socket

def get_ip():
    """
    Returns the IP address of the device.

    Returns:
        str: The public IP address, otherwise the local IP address.
             If no valid IP address is found, returns "Unknown".
             If an error occurs during the process, returns the error message.
    """
    try:
        # creates a udp socket and simulates a connection to google dns to determine the outbound ip
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        try:
            # if above fails, try to obtain ip by resolving the device's hostname
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip if local_ip and local_ip != "127.0.0.1" else "Unknown"
        except Exception as error:
            return str(error)
    except Exception as error:
        return str(error)