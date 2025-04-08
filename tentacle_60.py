def tentacle(input_data):
    # Check if the input is a string and looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Check for specific HTML document types
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, check if the input contains commas
        if ',' in input_data:
            # Sort and join the input
            return ','.join(sorted(input_data.split(',')))
        else:
            # Return the input as a lowercase string
            return str(input_data).lower()