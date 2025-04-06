#File reading and error handlig
try:
    
    file1 = open('sample.txt','r')
    read = file1.read()
    for line in read.splitlines():
       print(line)
   
except FileNotFoundError:
  
   print('Error: The file \"sample.txt\" not found')


# write and append data to a file

finally:
  
  print('Oopening next file....')
  file2 = open('output.txt','w')
  
  writing_file = file2.write(input('Enter text to the file:'))
  print('Content added to file.\n')
  file2.close()
  
  file2 = open('output.txt','a')
  
  apending_file = file2.write(input('\n' +'Add additional text to append: '))
  file2.close()
  
  file2 = open('output.txt','r')
  
  reading_file = file2.read()
  for line in reading_file.splitlines():
    print(line)
  file2.close()
  
  
      