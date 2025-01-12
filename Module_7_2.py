def custom_write(file_name: str,strings: list):
    file = open(file_name,'w', encoding= 'utf-8')
    index = 1
    strings_position = {}
    for string in strings:
        bytes_string = file.tell()
        file.write(string + '\n')
        strings_position[(index, bytes_string)] = string
        index +=1
    file.close()
    return strings_position

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]


result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)
