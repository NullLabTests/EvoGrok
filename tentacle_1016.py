import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected: advanced statistical techniques"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected: covering algebra, geometry, and calculus"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected: includes tokenization and stemming"
        else:
            return "generic html document detected: standard web page"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        result_str = str(result).lower()
        if result_str.replace('.', '').isdigit():
            number = float(result_str)
            # Calculate square, cube, and square root
            square = number ** 2
            cube = number ** 3
            square_root = math.sqrt(number)
            # Calculate factorial for integers
            if number.is_integer():
                factorial = math.factorial(int(number))
                return f"result: {result_str}, square: {square}, cube: {cube}, square root: {square_root}, factorial: {factorial}"
            else:
                return f"result: {result_str}, square: {square}, cube: {cube}, square root: {square_root}"
        else:
            return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort, reverse, lowercase, and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            reversed_items = [item[::-1].lower() for item in sorted_items]
            # Calculate the length of each item
            lengths = [len(item) for item in reversed_items]
            return f"processed: {','.join(reversed_items)}, lengths: {','.join(map(str, lengths))}"
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, square root, and factorial
            number = int(input_data)
            square = number ** 2
            cube = number ** 3
            square_root = math.sqrt(number)
            factorial = math.factorial(number)
            return f"number: {number}, square: {square}, cube: {cube}, square root: {square_root}, factorial: {factorial}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, uppercase, and vowel count
            word = input_data.replace(' ', '')
            vowels = sum(1 for char in word.lower() if char in 'aeiou')
            return f"word: {word}, length: {len(word)}, reverse: {word[::-1]}, uppercase: {word.upper()}, vowels: {vowels}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # and return the result along with its length and the count of unique characters
            processed_input = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            unique_chars = len(set(processed_input))
            return f"processed: {processed_input}, length: {len(processed_input)}, unique characters: {unique_chars}"