from typing import List

def search(array: List[int], thing_to_find: int) -> int:
    """ Binary search Algorithm

    Args:

        array (List[int]): represents the list in which you are searching
        thing_to_find (int): represents thing that you're searching

    Returns:

        int: result of the search. 
        Binary serach algorithm return the thing's postion if thing is present in the list or -1 if thing isn't in the list.
    """
    
    start: int = 0
    end: int = len(array) - 1
    array.sort()
    # tour = 0
    
    while start <= end:
        # tour += 1
        array_middle = (start + end) // 2
        
        if array[array_middle] == thing_to_find:
            # print(f'nombre de tours : {tour}')
            return array_middle
        
        if array[start] == thing_to_find:
            # print(f'nombre de tours : {tour}')
            return start
        
        if array[end] == thing_to_find:
            # print(f'nombre de tours : {tour}')
            return end

        if array[array_middle] > thing_to_find:
            end = array_middle - 1

        if array[array_middle] < thing_to_find:
            start = array_middle + 1
    else:
        # print(f'nombre de tours : {tour}')
        return -1


if __name__ == '__main__':
    # for exemple i've used a integer list
    # nevertheless search can be done on string list

    numbers_array = [i for i in range(100000)]
    number_to_search = int(input('Entrez le nombre que vous recherchez : '))

    result = search(numbers_array, number_to_search)
    
    if result != -1:
        print(f'✅  Element trouvé à l\'index {result} du tableau trié')
    else:
        print('❌  L\'element n\'a pas été trouvé 😥')