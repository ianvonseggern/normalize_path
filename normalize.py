import sys

def normalizePath(path):
    """
    This function normalizes a path by removing all
    single dots '/./', and by removing all '/../' and the
    parent directory (if it exists, note this does not throw
    an error if there is no parent directory). It does
    nothing else to normalize the path.
    
    Examples:
    'hello/to/.././the/../././world/.' returns 'hello/world'
    'foo//bar' returns 'foo//bar'
    '../foo' returns 'foo'
    'hello/../../world' returns 'world'
    """
    path_array = path.split("/")
    normalized_array = []
    for element in path_array:
        if element == '..':
            if len(normalized_array) != 0:
                normalized_array.pop()
        elif element != '.':
            normalized_array.append(element)
    return '/'.join(normalized_array)

if __name__ == "__main__":
    """
    A brief main function which prompts the user to
    input a path, normalizes it, and prints the result.
    """
    while True:
        input = raw_input("Please enter a path('q' to quit):")
        if input == 'q':
            break
        print normalizePath(input)
