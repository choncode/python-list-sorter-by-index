from src.list_sorter import list_sorter

def test_function_takes_two_arguments_and_returns_a_list():
    fruits = ['apple', 'orange', 'banana']
    result = list_sorter(fruits, 0)
    assert isinstance(result, list)