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
        #c_data = sum([1 for cln in self.cln if cln])
        out_str = []
        for cln in self.clns:
            out_str.append(cln + ": " + " ".join(self.clns[cln]))
        return "\n".join(out_str)

    def get_data(self, addr):
        return self.clns.get(addr)



if __name__ == "__main__":
    clns = Clients()
    addrs = "12345", "23111", "1241241"
    listofmodes = ["akkasgf_tv","-m", "-n", "-l"]
    for addr in addrs:
        clns.add_args(addr, listofmodes)
    #print("-"*20)
    #print([(addr, mode) for addr in addrs for mode in listofmodes])
    #[clns.add_args(addr, mode) for addr in addrs for mode in listofmodes]

    print(clns)