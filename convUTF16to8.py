with open('u16.txt', 'rb') as source_file:
  with open('u8.txt', 'w+b') as dest_file:
    contents = source_file.read()
    dest_file.write(contents.decode('utf-16').encode('utf-8'))

