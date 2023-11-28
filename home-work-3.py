list_path_file = ['1.txt', '2.txt', '3.txt']


def result_file(list_path_file, path_result):
    dict_file_data = {}
    for path_file in list_path_file:
        with open(path_file, encoding='UTF-8') as f:
            data_file = f.readlines()
            dict_file_data[str(len(data_file))+' | '+path_file] = data_file
    dict_file_data = sorted(dict_file_data.items())
    with open(path_result, 'w', encoding='UTF-8') as f:
        for tuple_file_data in dict_file_data:
            length, path_file = tuple_file_data[0].split(' | ')
            f.writelines(path_file + '\n')
            f.writelines(length + '\n')
            for list_str_file in tuple_file_data[1]:
                f.writelines(list_str_file.rstrip() + '\n')


result_file(list_path_file, 'result.txt')

