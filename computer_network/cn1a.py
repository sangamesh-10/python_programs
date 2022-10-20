sdel = "DLESTX"
edel = "DLEETX"
data = input("enter the data...")
data =data.upper()
data1 =data.replace("DLE","DLEDLE")
encoded = sdel+data1+edel
print(encoded)
received = encoded
received = received.removeprefix(sdel)
received = received.removesuffix(edel)
received = received.replace("DLEDLE","DLE")
print(received)