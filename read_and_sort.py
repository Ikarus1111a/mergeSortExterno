import uuid
import os
import sorting

    # Lê uuid's de um determinado caminho
def ler_uuids_arquivo(file_name, max_mem, output_directory):
    block = []
    total_size = 0
    block_number = 0

    
    file_path = f'ArquivoDeEntrada/{file_name}.txt'  
    output_directory = 'BlocosDeUUIDs'

    # Verifica se o diretório existe, se não, cria
    os.makedirs(output_directory, exist_ok=True)
    block_size = max_mem * 1024 * 1024

    with open(file_path, 'r') as file: # associa o arquivo e método de acesso a uma váriavel
        for line in file:
            uuid_str = line.strip()
            uuid_size = len(uuid_str.encode('utf-8'))
            
            if uuid_size + total_size > block_size:
                    block = sorting.merge_sort(block)
                    save_block_to_file(block, output_directory, block_number)
                    block = []
                    total_size = 0
                    block_number += 1
            else:
                uuid_size + total_size < block_size
                block.append(uuid_str)
                total_size += uuid_size

        if block:
            block = sorting.merge_sort(block)
            save_block_to_file(block, output_directory, block_number)


def save_block_to_file(block, output_directory, block_number):
    """Salva um bloco em um arquivo."""
    output_file_path = os.path.join(output_directory, f'block_{block_number}.txt')
    with open(output_file_path, 'w') as output_file:
        for uuid in block:
            output_file.write(uuid + '\n')



