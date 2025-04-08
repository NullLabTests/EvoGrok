def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia topics in the HTML document
        if 'data analysis' in input_str and 'wikipedia' in input_str:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_str and 'wikipedia' in input_str:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_str and 'wikipedia' in input_str:
            return "wikipedia text processing html document detected"
        else:
            # Check for additional keywords to provide more specific detection
            if 'wikipedia' in input_str:
                return "wikipedia html document detected"
            elif 'class=' in input_str or 'id=' in input_str:
                return "styled html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process as a comma-separated list or return as is
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings from the list
            cleaned_list = [item for item in sorted_list if item]
            return ','.join(cleaned_list)
        else:
            # If no commas, return the input as a lowercase string
            return input_str