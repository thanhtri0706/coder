
import struct

bin_data = struct.pack('bbbb', 123, 12, 45, 34)

fh = open('mybinary.dat', 'wb')

fh.write(bin_data)

fh.close()

file_read_handle = open('mybinary.dat', 'rb')

bin_data2 = file_read_handle.read()

data = struct.unpack('bbbb', bin_data2)
print(data)