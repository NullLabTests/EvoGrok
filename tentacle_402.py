def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
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
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values (from Parent2)
            return ','.join(sorted(input_data.split(',')))
        elif isinstance(input_data, str):
            # Process the string further
            words = input_data.split()
            if len(words) > 1:
                # If multiple words, reverse them and join with underscores
                return '_'.join(reversed(words)).lower()
            else:
                # If single word, return it in uppercase
                return input_data.upper()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()