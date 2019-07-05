from tkinter import *
import xml.etree.ElementTree as et


def main():
    tree = et.parse("ipv4_to_ipv6.xml")
    xmlroot = tree.getroot()
    subnets = {}
    for child in xmlroot.findall('subnet'):
        subnets[child.get('ipv4')] = child[0].text
    interface = gui(subnets)


class gui():

    def __init__(self, subnets):
        self.subnets = subnets
        self.root = Tk()

        self.num1Entry = Entry(self.root)
        self.num1Entry.pack(side=LEFT)

        # Label(self.root, text="+").pack(side=LEFT)

        # self.num2Entry = Entry(self.root)
        # self.num2Entry.pack(side=LEFT)

        self.equalButton = Button(self.root, text="convert to ipv6")
        self.equalButton.bind("<Button-1>", self.get_sum)
        self.equalButton.pack(side=LEFT)

        self.sumEntry = Entry(self.root, width=30)
        self.sumEntry.pack(side=LEFT)

        self.root.mainloop()

    def get_sum(self, event):
        ipv4 = str(self.num1Entry.get())
        self.sumEntry.delete(0, END)

        multi = 1
        sum = 0
        netid = 0
        while ipv4[-1] != ".":
            raw = int(ipv4[-1])
            sum += raw * multi
            # sum+=raw
            ipv4 = ipv4[:-1]
            multi *= 10
        netid = sum
        netid6 = str(hex(netid))
        netid6 = netid6[2:]
        if len(netid6) < 2:
            netid6 = "0" + netid6
        ipv4 = ipv4 + "xxx"
        try:
            ipv6 = self.subnets[ipv4]
            ipv6 = ipv6[:-2] + netid6
        except KeyError:
            ipv6 = "No known IPv4/IPv6 relationship"

        self.sumEntry.insert(0, ipv6)


main()
