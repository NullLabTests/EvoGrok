def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and content
        if 'data analysis' in lowercase_input:
            if 'class="mw-page-title-main"' in lowercase_input:
                return "wikipedia data analysis html document detected"
            else:
                return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            if 'class="vector-page-title"' in lowercase_input:
                return "wikipedia mathematics html document detected"
            else:
                return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            if 'class="firstHeading"' in lowercase_input:
                return "wikipedia text processing html document detected"
            else:
                return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"evaluated result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            return f"sorted list: {','.join(sorted_items)}"
        elif input_data.isdigit():
            # If it's a single number, return its square and cube
            number = int(input_data)
            return f"square: {number ** 2}, cube: {number ** 3}"
        else:
            # For other inputs, reverse the string, convert to lowercase, and add a prefix
            return f"reversed input: {input_data[::-1].lower()}"