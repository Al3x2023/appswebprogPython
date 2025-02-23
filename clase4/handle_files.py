try:
    #new_file = open('C:\\Users\\aleja\\Documents\\archivo.txt','w')
    #new_file.write("Hello world\n")
    #new_file.write("Hola mundo\n")
    #new_file.write("Hola UTVT\n")
    #new_file.close()

    path='C:\\Users\\aleja\\Documents\\archivo.txt'
    new_file =open(path,'r')
#    data = new_file.readlines()
#    print(data)
    one_line = new_file.readline()
    print(one_line)
    print(one_line)
    
   # for line in  data:
    #        print(line)

except Exception as e:
    print(e)
