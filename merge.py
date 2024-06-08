import os
import heapq
import uuid

def is_valid_uuid(s):
    try:
        uuid_obj = uuid.UUID(s)
        return True
    except ValueError:
        return False

def read_uuid_chunk(file, chunk_size):
    chunk = []
    current_size = 0
    for line in file:
        line = line.strip()
        if is_valid_uuid(line):
            element_size = len(line.encode('utf-8'))  # Calculate the size of the UUID in bytes
            if current_size + element_size > chunk_size:
                break
            chunk.append(line)
            current_size += element_size
    return chunk

def merge_and_cleanup(folder, output_file, max_memory):
    max_memory_bytes = max_memory * 1024 * 1024  # Convert MB to bytes
    uuid_arrays = []

    # Lista os arquivos na pasta
    files_in_folder = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]

    # Le UUIDs
    for file_in_folder in files_in_folder:
        file_path = os.path.join(folder, file_in_folder)
        with open(file_path, 'r') as file:
            while True:
                chunk = read_uuid_chunk(file, max_memory_bytes)
                if not chunk:
                    break
                uuid_arrays.append(chunk)

    result = []
    heap = []

    # Inicializa com o primeiro UUID de cada arquivo
    for i, uuid_array in enumerate(uuid_arrays):
        if uuid_array:
            heapq.heappush(heap, (uuid_array[0], i, 0))  # (value, array_index, element_index)

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)

        element_index += 1

        if element_index < len(uuid_arrays[array_index]):
            heapq.heappush(heap, (uuid_arrays[array_index][element_index], array_index, element_index))

    # Escreve o resultado no arquivo
    with open(output_file, 'w') as output:
        for uuid_value in result:
            output.write(f"{uuid_value}\n")

    # Apaga arquivos da pasta
    for file_in_folder in files_in_folder:
        file_path = os.path.join(folder, file_in_folder)
        os.remove(file_path)

folder_with_files = 'BlocosDeUUIDs'
output_file_path = 'ArquivoDeSaida/Output.txt'
