def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia page detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia page detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # If the result is a number, return its square root and factorial
        if isinstance(result, (int, float)):
            import math
            return f"square root: {math.sqrt(result):.2f}, factorial: {math.factorial(int(result)) if result.is_integer() and result >= 0 else 'N/A'}"
        # For other types of results, convert to string and lowercase
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, and join them
            return ','.join(item[::-1].capitalize() for item in sorted_items)
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, and binary representation
            number = int(input_data)
            return f"square: {number ** 2}, cube: {number ** 3}, binary: {bin(number)}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, and vowel count
            vowels = sum(1 for char in input_data.lower() if char in 'aeiou')
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, vowels: {vowels}"
        else:
            # For other inputs, reverse the string, convert to uppercase, and keep only alphanumeric characters
            return ''.join(char.upper() for char in input_data[::-1] if char.isalnum())