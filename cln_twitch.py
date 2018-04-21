import time, socket, sys
import tools_twitch
 
class Client_twitch_chat:
    def __init__(self, *, tcp_ip="localhost", tcp_port=40001):
        if len(sys.argv) == 1:
            self.channel = sys.argv[1]
        elif len(sys.argv) == 2 and sys.argv[1].startswith("-"):
            self.modes = sys.argv[1]
            self.channel = sys.argv[2]
        else:
            raise ValueError("""Must be 1 or 2 (optionally) args
                                first: channal or modes
                                second: channel
                                Exepmles:
                                    >>> python cn_twitch -sv myfavoritstreamer
                                    >>> python cn_twitch myfavoritstreamer
                            """)
        self.sock = socket.socket(socket.AF_INET, 
                                  socket.SOCK_STREAM)
        self.sock.connect((tcp_ip, tcp_port))

    @tools_twitch.only_once
    def first_request(self, channel):
        self.sock.send("firstconnect\n", self.channel.decode("utf-8"))
        data = self.sock.recv(1024)
        print(f"srv ansvered {data}")
        self.sock.close()
        return data


if __name__ == "__main__":
    cln = Client_twitch_chat()
    cln.send_request()

