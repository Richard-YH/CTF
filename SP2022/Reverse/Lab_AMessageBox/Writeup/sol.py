enc_flag = [0xB5,0xE5,0x8D,0xBD,0x5C,0x46,0x36,0x4E,0x4E,0x1E,0xE,0x26,0xA4,0x1E,0xE,0x4E,0x46,0x6,0x16,0xAC,0xB4,0x3E,0x4E,0x16,0x94,0x3E,0x94,0x8C,0x94,0x8C,0x9C,0x4E,0xA4,0x8C,0x2E,0x46,0x8C,0x6C]

def ROL(data, shift, size=8):
    shift %= size 
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)

def ROR(data, shift, size=8):
    shift %= size 
    body = data >> shift
    remains = (data << (size - shift)) - (body <<size)
    return (body + remains)

FLAG = ""
for i in range(len(enc_flag)):
    FLAG+= str(chr(ROR(enc_flag[i]^0x87,3)))
print(FLAG)
