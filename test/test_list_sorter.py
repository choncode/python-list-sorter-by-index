from src.list_sorter import list_sorter

def test_function_takes_two_arguments_and_returns_a_list():
    fruits = ['apple', 'orange', 'banana']
    result = list_sorter(fruits, 0)
    assert isinstance(result, list)

def test_sorts_list_alphabetically():
    fruits = ['apple', 'orange', 'banana']
    result = list_sorter(fruits, 0)
    assert result == ['apple', 'banana', 'orange']
    
    colours = ['green', 'yellow', 'blue']
    result = list_sorter(colours, 0)
    assert result == ['blue', 'green', 'yellow']

def test_sorts_list_by_index():
    fruits = ['apple', 'orange', 'banana']
    result = list_sorter(fruits, 1)
    assert result == ['banana', 'apple', 'orange']

    colours = ['green', 'yellow', 'blue']
    result = list_sorter(colours, 2)
    assert result == ['green', 'yellow', 'blue']

def test_sorts_nested_list_by_index():
    fruits = [['apple', 'orange', 'banana'], 
              ['grapes', 'pear', 'melon']]
    result = list_sorter(fruits, 1)
    assert result == [['banana', 'apple', 'orange'], 
                      ['pear', 'melon', 'grapes']]