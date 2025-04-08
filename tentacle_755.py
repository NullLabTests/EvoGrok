def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
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
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings, strip whitespace, and remove duplicates
            cleaned_values = list(dict.fromkeys([value.strip().lower() for value in sorted_values if value.strip()]))
            return ','.join(cleaned_values)
        else:
            # Convert the input to lowercase and remove any leading/trailing whitespace
            lowercase_input = input_data.strip().lower()
            
            # Check for specific keywords related to the known HTML document types
            if 'data analysis' in lowercase_input:
                return f"data analysis related: {lowercase_input}"
            elif 'mathematics' in lowercase_input:
                return f"mathematics related: {lowercase_input}"
            elif 'text processing' in lowercase_input:
                return f"text processing related: {lowercase_input}"
            else:
                return lowercase_input