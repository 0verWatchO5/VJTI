
#  local_24[0] = 0x39
#   local_24[1] = 0x4d
#   local_24[2] = 0x4a
#   local_24[3] = 0x45
#   local_20 = 0x68
#   local_1f = 0x2f
#   local_1e = 0x27
#   local_1d = 0x35
#   local_1c = 0x4c
#   local_1b = 0x38
#   local_1a = 0x49
#   local_19 = 0x44
#   local_18 = 0x59
#   local_17 = 0x56
#   local_16 = 0x31
#   local_15 = 0x5b
#   local_14 = 0x60
#   local_13 = 0x32
#   local_12 = 0x68
#   local_11 = 0x4e
#   local_10 = 0x57
#   local_f = 0x34
#   local_e = 0x4a
#   local_d = 0x61
#   local_c = 0x53
#   local_b = 0x69
#   local_a = 0x43
#   local_9 = 0

#  local_3f[0] = 0x6d
#   local_3f[1] = 0x74
#   local_3f[2] = 0x7b
#   local_3f[3] = 0x70
#   local_3b = 0x13
#   local_3a = 0x66
#   local_39 = 0x78
#   local_38 = 0x79
#   local_37 = 0x7c
#   local_36 = 0x6e
#   local_35 = 0x7a
#   local_34 = 0x1b
#   local_33 = 1
#   local_32 = 0x66
#   local_31 = 99
#   local_30 = 4
#   local_2f = 0x53
#   local_2e = 0x7c
#   local_2d = 0x2b
#   local_2c = 0x1c
#   local_2b = 0xe
#   local_2a = 100
#   local_29 = 0x7d
#   local_28 = 0x50
#   local_27 = 99
#   local_26 = 0x27
#   local_25 = 0x3e
#   local_a3[0] = '\0'

def solve_password():
    # Values from the binary
    local_24 = [0x39, 0x4d, 0x4a, 0x45, 0x68,0x2f,0x27,0x35,0x4c,0x38,0x49,0x44,0x59,0x56,0x31,0x5b,0x60,0x32,0x68,0x4e,0x57,0x34,0x4a,0x61,0x53,0x69,0x43,0]  # First 4 bytes
    local_3f = [0x6d, 0x74, 0x7b, 0x70, 0x13,0x66,0x78,0x79,0x7c,0x6e,0x7a,0x1b,1, 0x66,99,4,0x53,0x7c,0x2b,0x1c,0xe,100,0x7d,0x50,99,0x27,0x3e]  # First 4 bytes
    
    # Calculate first few characters of password
    password = ""
    for i in range(min(len(local_24), len(local_3f))):
        char = local_24[i] ^ local_3f[i]
        password += chr(char)
        print(f"Position {i}: {local_24[i]:02x} ^ {local_3f[i]:02x} = {char:02x} ('{chr(char)}')")
    
    return password

print("Calculating password characters...")
password = solve_password()
print(f"\nFirst few characters of password: {password}")