af = list(b"\x13\x13\x11\x17\x12\x1d\x48\x45\x45\x41\x0b\x26\x2c\x42\x5f\x09\x0b\x5f\x6c\x3d\x56\x56\x1b\x54\x5f\x41\x45\x29\x3c\x0b\x5c\x58\x00\x5f\x5d\x09\x54\x6c\x2a\x40\x06\x06\x6a\x27\x48\x42\x5f\x4b\x56\x42\x2d\x2c\x43\x5d\x5e\x6c\x2d\x41\x07\x47\x43\x5e\x31\x6b\x5a\x0a\x3b\x6e\x1c\x49\x54\x5e\x1a\x2b\x34\x05\x5e\x47\x28\x28\x1f\x11\x26\x3b\x07\x50\x04\x06\x04\x0d\x0b\x05\x03\x48\x77\x0a")
flag = "r"
char = "r"
for stuff in af:
  flag += chr(ord(char) ^ stuff)
  char = flag[-1]
  
print(flag)
