def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected: wikipedia page"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected: wikipedia page"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected: wikipedia page"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings, strip whitespace, and remove duplicates
            cleaned_values = list(dict.fromkeys([value.strip().lower() for value in sorted_values if value.strip()]))
            return f"sorted and cleaned values: {','.join(cleaned_values)}"
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
                # Check for other keywords that might be relevant
                if 'statistics' in lowercase_input:
                    return f"statistics related: {lowercase_input}"
                elif 'machine learning' in lowercase_input:
                    return f"machine learning related: {lowercase_input}"
                elif 'natural language processing' in lowercase_input:
                    return f"natural language processing related: {lowercase_input}"
                else:
                    return lowercase_input