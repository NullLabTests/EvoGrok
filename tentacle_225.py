def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        return "html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # If successful, return the result as a lowercase string
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            return ','.join(sorted(input_data.split(',')))
        else:
            # Return the input as a lowercase string
            return str(input_data).lower()