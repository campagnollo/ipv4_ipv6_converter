"""Program to convert IPv4 subnets to known IPv6 subnets based on relationships presented by an XML file. """

from tkinter import *
import xml.etree.ElementTree as et


def main():
    tree = et.parse("ipv4_to_ipv6.xml")
    xmlroot = tree.getroot()
    subnets = {}
    for child in xmlroot.findall('subnet'): #Pull XML into a dictionary
        subnets[child.get('ipv4')] = child[0].text
    gui(subnets)


class gui():

    def __init__(self, subnets):
        self.subnets = subnets
        self.root = Tk()

        self.ipv4Entry = Entry(self.root) #prep space for IPv4 entry
        self.ipv4Entry.pack(side=LEFT)


        self.convertButton = Button(self.root, text="convert to ipv6") #conversion activation
        self.convertButton.bind("<Button-1>", self.ipv4toipv6)
        self.convertButton.pack(side=LEFT)

        self.ipv6Output = Entry(self.root, width=30) #space for IPv6 output
        self.ipv6Output.pack(side=LEFT)

        self.root.mainloop()

    def ipv4toipv6(self, event):
        ipv4 = str(self.ipv4Entry.get()) #Capture IPv4 entry
        self.ipv6Output.delete(0, END) #clear IPv6 output space

        multi = 1 #multiplier for decimal number placement
        netid=0 #holder for the last octet of the IPv4 address
        while ipv4[-1] != ".": #strip the last octet of each number until "." is reached
            raw = int(ipv4[-1])
            netid += raw * multi
            ipv4 = ipv4[:-1]
            multi *= 10
        netid6 = (str(hex(netid)))[2:] #convert the decimal number to hex
        if len(netid6) < 2: #if the hex output only produces a single character, add a '0' in the front
            netid6 = "0" + netid6
        ipv4 = ipv4 + "xxx" #add 'xxx' to enable search in the dictionary
        try:
            ipv6 = self.subnets[ipv4]
            ipv6 = ipv6[:-2] + netid6
        except KeyError: #error if the IPv4/IPv6 relationship can't be found.
            ipv6 = "No known IPv4/IPv6 relationship"

        self.ipv6Output.insert(0, ipv6) #send the IPv6 result to the output

if __name__ == '__main__':
    try:
        assert sys.version_info[0]>=3
    except AssertionError:
        print("Incorrect interpreter being run. Please use Python 3.x or higher")
        exit()
    main()
