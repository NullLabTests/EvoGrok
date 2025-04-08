def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()
    
    # Check if the input is the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific HTML document types
        if 'data analysis' in input_str:
            return "data analysis html document detected"
        elif 'mathematics' in input_str:
            return "mathematics html document detected"
        elif 'text processing' in input_str:
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to sort and join the input data
        return ','.join(sorted(input_str.split(',')))
    except:
        try:
            # If sorting fails, attempt to evaluate as a mathematical expression
            result = eval(input_str)
            return str(result).lower()
        except:
            # If all else fails, return the input as a lowercase string
            return input_str