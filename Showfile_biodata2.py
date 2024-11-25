with open ("biodata.txt", "r") as file:
  data = file.read()
  print(lines[0].strip())
  print(lines[2].strip())
  print(lines[1].strip())
  print(lines[3].strip())

with open ("biodata2.txt", "w") as file_copy:
  file_copy.write(data)