"""
Regular Expression Group Capturing and Back Referencing!
"""

import re

with open(r"C:\Users\adars\Desktop\random.txt", "r") as handle1:
    content1 = handle1.read()
    print("Actual Content:\n", content1,"\n####################################################\n")

    print("obtaining the phone numbers in the format: 123-xxx-1234")
    print("---------------------------------------------------------")
    redact_ph = re.sub(r"(\d{3})-\d{3}-(\d{4})", r"\1-xxx-\2", content1)
    print(redact_ph)

    print("obtaining date format from mm dd yyyy to mm dd, yyyy")
    print("-------------------------------------------------------")
    mm_dd_yyyy = re.sub(r"(\d{1,2})\s?([a-zA-Z]{3})\s?(\d{4})", r"\2 \1, \3", content1)
    print(mm_dd_yyyy)


"""
Output:
``````
Actual Content:
 19 Jan 1965
Judy Foster
912-576-7052

02 Aug 1984
John Nash
717-852-7391

30 Jun 1989
Baba Sikandar
750-715-7178

####################################################

obtaining the phone numbers in this format 123-xxx-1234
---------------------------------------------------------
19 Jan 1965
Judy Foster
912-xxx-7052

02 Aug 1984
John Nash
717-xxx-7391

30 Jun 1989
Baba Sikandar
750-xxx-7178

obtaining date format from mm dd yyyy to mm dd, yyyy
-------------------------------------------------------
Jan 19, 1965
Judy Foster
912-576-7052

Aug 02, 1984
John Nash
717-852-7391

Jun 30, 1989
Baba Sikandar
750-715-7178

"""
