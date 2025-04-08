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
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item and join them
            return ','.join(item[::-1] for item in sorted_items)
        elif input_data.isdigit():
            # If it's a single number, return its square and cube
            number = int(input_data)
            return f"square: {number ** 2}, cube: {number ** 3}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a string of letters (with or without spaces), return its length and reverse
            return f"length: {len(input_data)}, reverse: {input_data[::-1].lower()}"
        else:
            # For other inputs, reverse the string, convert to lowercase, and remove non-alphanumeric characters
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            return cleaned_input[::-1]