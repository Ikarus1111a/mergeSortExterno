import read_and_sort
import merge

    
file_name = input("Nome do arquivo na pasta:\n")
max_mem = input("Por favor, quanta memoria deseja usar em MB:\n")

output_path = 'BlocosDeUUIDs'

read_and_sort.ler_uuids_arquivo(file_name, max_mem, output_path)
merge.merge_and_cleanup