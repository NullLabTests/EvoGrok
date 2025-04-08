def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Check for specific HTML document types
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia page detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia page detected"
        
        # Check for other common HTML document types
        elif 'wikipedia' in lowercase_input:
            return "generic wikipedia page detected"
        elif 'blog' in lowercase_input:
            return "blog page detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                # Reverse each item and join them
                reversed_items = [item[::-1].strip() for item in sorted_items]
                return f"reversed and sorted: {','.join(reversed_items)}"
            elif input_data.isdigit():
                # If it's a single number, return its square, cube, and factorial
                number = int(input_data)
                factorial = 1
                for i in range(1, number + 1):
                    factorial *= i
                return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}"
            elif input_data.replace(' ', '').isalpha():
                # If it's a string of letters (with or without spaces), return its length, reverse, and vowel count
                vowels = sum(1 for char in input_data.lower() if char in 'aeiou')
                return f"length: {len(input_data)}, reverse: {input_data[::-1].lower()}, vowels: {vowels}"
            else:
                # For other inputs, reverse the string, convert to lowercase, and remove non-alphanumeric characters
                cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
                return f"cleaned and reversed: {cleaned_input[::-1]}"
        else:
            # Handle non-string inputs
            return f"non-string input: {str(input_data).lower()}"