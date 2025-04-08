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
            # Sort and join comma-separated values (inspired by Parent2)
            sorted_values = sorted(input_data.split(','))
            # Remove duplicates and join (new feature)
            unique_values = list(dict.fromkeys(sorted_values))
            return ','.join(unique_values)
        else:
            # Check if the input is a number (new feature)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # Reverse the string if it's not a number (new feature)
                return str(input_data)[::-1].lower()