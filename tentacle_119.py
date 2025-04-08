def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect specific types of HTML documents based on known titles
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return 'data analysis html document detected'
        elif 'mathematics' in lowercase_input:
            return 'mathematics html document detected'
        elif 'text processing' in lowercase_input:
            return 'text processing html document detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values if present
            return ','.join(sorted(input_data.split(',')))
        else:
            # Return the input as a lowercase string
            return str(input_data).lower()