def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If it's an HTML document but doesn't match specific types, check for other keywords
            if 'wikipedia' in lowercase_input:
                return "wikipedia html document detected"
            elif 'tutorial' in lowercase_input:
                return "tutorial html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, and join them
            return ','.join(item[::-1].capitalize() for item in sorted_items)
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, and factorial
            number = int(input_data)
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, and first three letters capitalized
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3].upper()}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # and add the count of vowels
            reversed_clean = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_clean if char in 'aeiou')
            return f"processed: {reversed_clean}, vowel count: {vowels}"