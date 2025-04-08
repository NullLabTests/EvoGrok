def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return "data analysis html document detected"
        elif 'mathematics' in input_lower:
            return "mathematics html document detected"
        elif 'text processing' in input_lower:
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
            sorted_items = sorted(input_data.split(','))
            # Convert each item to lowercase (new feature)
            lowercase_items = [item.strip().lower() for item in sorted_items]
            return ','.join(lowercase_items)
        else:
            # Return the input as a lowercase string (from Parent1)
            return str(input_data).lower()