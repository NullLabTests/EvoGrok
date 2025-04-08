import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia text processing html document detected"
        elif 'blog' in lowercase_input:
            return "blog html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and provide more detailed information
        return f"math result: {str(result).lower()}, type: {type(result).__name__}"
    except:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                # Reverse each item, capitalize it, and join them
                return ','.join(item[::-1].strip().capitalize() for item in sorted_items)
            elif input_data.isdigit():
                # If it's a single number, return its square, cube, factorial, and logarithm
                number = int(input_data)
                factorial = math.factorial(number)
                logarithm = math.log(number) if number > 0 else "undefined"
                return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, logarithm: {logarithm:.2f}"
            elif input_data.replace(' ', '').isalpha():
                # If it's a string of letters (with or without spaces), return its length, reverse, vowel count, and consonant count
                lowercase_input = input_data.lower()
                vowels = sum(1 for char in lowercase_input if char in 'aeiou')
                consonants = sum(1 for char in lowercase_input if char.isalpha() and char not in 'aeiou')
                return f"length: {len(input_data)}, reverse: {input_data[::-1].lower()}, vowels: {vowels}, consonants: {consonants}"
            else:
                # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters, and count digits
                cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
                digit_count = sum(1 for char in cleaned_input if char.isdigit())
                return f"cleaned and reversed: {cleaned_input[::-1]}, digit count: {digit_count}"
        else:
            # Handle non-string inputs
            return f"non-string input: {str(input_data).lower()}, type: {type(input_data).__name__}"