import io
import os
import getpass

bs = io.BytesIO(b"THis is a byte stream,\nDo you understand? And this is --> \x01 <-- ctrl A i.e ^A character")
print(bs.getvalue())
print(bs.closed)
bs.close()
print(bs.closed)

with io.BytesIO(b"THis is a second byte stream,\nDo you understand? And this is --> \x01 <-- ctrl A i.e ^A character") as bs1:
    print(bs1.getvalue())

print(bs1.closed)

print("end of code")

print("\n=====================================================================================================\n")

ss = io.StringIO("THis is a byte stream,\nDo you understand? And this is --> \x01 <-- ctrl A i.e ^A character")
print(ss.getvalue())
print(ss.closed)
ss.close()
print(ss.closed)

with io.StringIO("THis is a second byte stream,\nDo you understand? And this is --> \x01 <-- ctrl A i.e ^A character") as ss1:
    print(ss1.getvalue())

print(ss1.closed)

print("end of code")