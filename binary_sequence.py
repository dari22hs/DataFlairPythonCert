"""
Binary Sequence Types

#* bytes and bytearray:
    are built-in types that help manipulate binary data.
#* memoryview:
    makes use of the buffer protocol to access memory of other binary objects without needing to replicate them.
"""
# msg = "Welcome to my new file"
# arr = bytes(msg, 'utf-8')
# print(arr)
# print(type(arr))

# print(bytes(7))
# print(bytes([8, 2, 3, 6]))

## fromhex() - Decodes a string object with two hexadecimal digits per byte to return a bytes object
# print(bytes.fromhex('2EF0 F1F2'))
# print(bytes.fromhex('1Ee0 24df'))

## hex() - Returns string object with two hexadecimal digits for each byte in instance
# print(b'\xf0\xf1\xf2'.hex())
# print(b'\x1e\xe0$\xdf'.hex())

## bytearray()
# msg = "Hello, world!"
# print(bytearray(msg, 'utf-8'))

# print(bytearray(7))
# print(bytearray([7, 2, 3, 5]))

## memoryview()
msg = bytearray("Hello, world!", 'utf-8')
mv = memoryview(msg)
print(mv)
print(mv[1]) # Output -> 101 -> ASCII value for "e"
print(list(mv[1:3])) # Output -> [101, 108] -> ASCII values for "e" and "l"
mv[1] = 65 # ASCII value for "A"
print(msg) # Output -> bytearray(b'HAllo, world!')


