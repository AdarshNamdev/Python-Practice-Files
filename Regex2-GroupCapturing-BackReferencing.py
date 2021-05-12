"""
Regular Expression Group Capturing and Back Referencing!
"""

import re

with open(r"C:\Users\adars\Desktop\random.txt", "r") as handle1:
    content1 = handle1.read()
    print("Actual Content:\n", content1,"\n####################################################\n")

    print("obtaining the phone numbers in this format 123-xxx-1234")
    print("---------------------------------------------------------")
    redact_ph = re.sub(r"(\d{3})-\d{3}-(\d{4})", r"\1-xxx-\2", content1)
    print(redact_ph)

    print("obtaining date format from mm dd yyyy to mm dd, yyyy")
    print("-------------------------------------------------------")
    mm_dd_yyyy = re.sub(r"(\d{1,2})\s?([a-zA-Z]{3})\s?(\d{4})", r"\2 \1, \3", content1)
    print(mm_dd_yyyy)
