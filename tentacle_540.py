def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and return it with a prefix
        return f"evaluated result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            return f"sorted comma-separated: {','.join(sorted_values)}"
        elif ' ' in input_data:
            # Sort and join space-separated values
            sorted_values = sorted(input_data.split())
            return f"sorted space-separated: {' '.join(sorted_values)}"
        elif input_data.isdigit():
            # If the input is a single number, return its square and cube
            number = int(input_data)
            return f"square: {number ** 2}, cube: {number ** 3}"
        else:
            # Return the input as a lowercase string with a prefix
            return f"processed string: {str(input_data).lower()}"