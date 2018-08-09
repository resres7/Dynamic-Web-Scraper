from collections import defaultdict

class Clients:
    def __init__(self):
        self.clns = defaultdict(list)

    def new_cln(self, addr, data):
        self.clns[addr] = data

    def add_args(self, addr, modes):
        for mode in modes:
            self.clns[addr].append(mode)
        print(f"For {addr} was added "+ " ".join(modes))
    
    def __str__(self):
        out_str = []
        for cln in self.clns:
            out_str.append(cln + ": " + " ".join(self.clns[cln]))
        return "\n".join(out_str)

    def get_data(self, addr):
        return self.clns.get(addr)

    def del_cln(self, addr):
        try:
            del self.clns[addr]
            print(f"Client {addr} was deleted")
            return True
        except Exception as e:
            print("~"*20,f"\nClient {addr} CANT be deleted\n", e, "\n")



if __name__ == "__main__":
    clns = Clients()
    addrs = "12345", "23111", "1241241"
    listofmodes = ["akkasgf_tv","-m", "-n", "-l"]
    for addr in addrs:
        clns.add_args(addr, listofmodes)
    print(clns)
    clns.del_cln(addrs[-1])
    print(clns)
