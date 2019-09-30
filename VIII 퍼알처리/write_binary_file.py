f = open("data.bin","wb") #b가 매우중요
byte_arr = bytes([255,0,127])
f.write(byte_arr)
f.close()
