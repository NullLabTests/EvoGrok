def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_str:
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_str:
            return "text processing wikipedia page detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process as a comma-separated list or return as is
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_list = [item for item in sorted_list if item]
            return ','.join(cleaned_list)
        else:
            # If no commas, check for specific keywords
            if 'data' in input_str and 'analysis' in input_str:
                return "data analysis related content detected"
            elif 'mathematics' in input_str or 'math' in input_str:
                return "mathematics related content detected"
            elif 'text' in input_str and 'processing' in input_str:
                return "text processing related content detected"
            else:
                # If no specific keywords, return the input as a lowercase string
                return input_str