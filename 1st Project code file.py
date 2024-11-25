
#this opens a file then allows it to be written in and allows it to be read
with open('1st Project read file.txt', 'r+') as f:
  #this tells it to write in the file
    f.write("Hello! Can you read  me?")
#this changes the position of the file pointer
    f.seek(0)  
    
  #this makes the read the same thinf=g as content
    f_content = f.read()
    
  #this prints it 
    print(f_content)




#this is some code i was practcing with

# with open('1st Project read file.txt', 'w') as f:
  
#     f.write('Hello! can you read me?')



# with open('1st Project read file.txt', 'r') as f:
#     f_contents = f.read()
    
#     if len(f_contents) > 100:
#         print('To Many Characters!')
#     else: 
#         print(f_contents)
  
