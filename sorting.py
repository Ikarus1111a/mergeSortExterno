import uuid

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir a lista ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursivamente ordenar as duas metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Mesclar as duas metades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Adicionar os elementos restantes, se houver, de ambas as metades
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result
