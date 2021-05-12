
"""
Find all the IP addresses from the txt file and store them in table
"""


from prettytable import PrettyTable
import re

with open(r"D:\PythonProgram\FileHandling\mbox-short.txt", 'r') as handle:
    #IPAddress = []
    ipTable = PrettyTable()
    line_num = 1
    ipTable.field_names= ["#", "Line from txt file", "IP Address"]

    for line in handle:
        line = line.rstrip()
        IPAddress = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line)

        if len(IPAddress) < 1:
            continue

        else:
            ipTable.add_row([line_num, line, " ".join(IPAddress)])
            line_num += 1


print(ipTable)

ababab
