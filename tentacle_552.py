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
        return f"mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            return f"sorted list: {','.join(sorted_items)}"
        elif input_data.strip().isdigit():
            # If it's a single number, return it as a string with a descriptive message
            return f"single number detected: {input_data}"
        elif input_data.strip().isalpha():
            # If it's a single word, return it capitalized
            return f"single word detected: {input_data.strip().capitalize()}"
        else:
            # For other inputs, return the input as a lowercase string
            return f"other input detected: {str(input_data).lower()}"