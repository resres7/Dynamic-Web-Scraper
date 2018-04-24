# Scraping twitch chat
import socket
import twitch_chat, tools_twitch

class Start_srv():
    #Launch 
    def __init__(self, *, tcp_ip="localhost", tcp_port="40001"):
        self.sock = socket.socket(socket.AF_INET, 
                                  socket.SOCK_STREAM)
        self.sock.bind(('localhost', 40001))
        self.sock.listen(5)
        self.clients = tools_twitch.Clients()
        self.chats = {}


    def start_listen(self):
        """Start listening clients
        """
        while True:
            conn, addr = self.sock.accept()
            try:
                if addr not in self.clients: 
                    self.clients.new_cln(addr, [])
                    print(f"{addr} was be connected")
                    data = self.get_answer(conn)
                    *modes, channel = data.split()
                    self.clients.add_modes(addr, modes)
                    set_chat_new_channel()
                simple_answer(conn, addr, data)
            finally:
                conn.close()

    #def read_modes(self, addr, *modes):
    #    for mode in modes:
    #        self.clients.add_mode(addr, mode)

    def set_chat_new_channel(self, steps=0, *, 
                             channel=None, nonstop=True):
        try:
            self.chats[channel] = twitch_chat.Look_at_chat(steps, 
                                  addr=addr, channel=channel, 
                                  nonstop=nonstop)
        except Exception as e:
            print(e, "\nRaised exception in cls 'Start_srv'", 
                     " -> mtd 'get_chat_for_new_cln'")


    def del_chat_cln(self, channel=None):
        del self.chats[channel]
        print(f"Channel {channel} was been deleted")

    
    def what_send(self, addr):
        #dont work 
        return b"U send me " + self.recive[addr] + \
               b" i dont know waht it is"
    
    def get_answer(self, conn):
        data = b""
        while True:
            data += conn.recv(1024)
        return data
    

if __name__ == "__main__":
    srv = Start_srv()
    srv.start_listen()
