from tkinter import *
import xml.etree.ElementTree as et


def main():
    tree = et.parse("ipv4_to_ipv6.xml")
    xmlroot = tree.getroot()
    subnets = {}
    for child in xmlroot.findall('subnet'):
        subnets[child.get('ipv4')] = child[0].text
    gui(subnets)


class gui():

    def __init__(self, subnets):
        self.subnets = subnets
        self.root = Tk()

        self.ipv4Entry = Entry(self.root)
        self.ipv4Entry.pack(side=LEFT)


        self.convertButton = Button(self.root, text="convert to ipv6")
        self.convertButton.bind("<Button-1>", self.ipv4toipv6)
        self.convertButton.pack(side=LEFT)

        self.ipv6Output = Entry(self.root, width=30)
        self.ipv6Output.pack(side=LEFT)

        self.root.mainloop()

    def ipv4toipv6(self, event):
        ipv4 = str(self.ipv4Entry.get())
        self.ipv6Output.delete(0, END)

        multi = 1
        netid=0
        while ipv4[-1] != ".":
            raw = int(ipv4[-1])
            netid += raw * multi
            ipv4 = ipv4[:-1]
            multi *= 10
        netid6 = (str(hex(netid)))[2:]
        if len(netid6) < 2:
            netid6 = "0" + netid6
        ipv4 = ipv4 + "xxx"
        try:
            ipv6 = self.subnets[ipv4]
            ipv6 = ipv6[:-2] + netid6
        except KeyError:
            ipv6 = "No known IPv4/IPv6 relationship"

        self.ipv6Output.insert(0, ipv6)

if __name__ == '__main__':
    main()
