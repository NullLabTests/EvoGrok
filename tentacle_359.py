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
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            return ','.join(sorted(input_data.split(',')))
        elif ' ' in input_data:
            # Sort and join space-separated values
            return ' '.join(sorted(input_data.split()))
        elif input_data.isdigit():
            # If the input is a single number, return its square
            return str(int(input_data) ** 2)
        else:
            # Return the input as a lowercase string
            return str(input_data).lower()