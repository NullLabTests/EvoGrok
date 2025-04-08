def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia page topics in the HTML document
        if 'data analysis' in input_str:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in input_str:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in input_str:
            return "wikipedia page on text processing detected"
        else:
            # If it's an HTML document but not a known Wikipedia page
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process as a comma-separated list or check for keywords
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings from the list
            cleaned_list = [item.strip() for item in sorted_list if item.strip()]
            return ','.join(cleaned_list)
        else:
            # If no commas, check for specific keywords
            if 'data' in input_str and 'analysis' in input_str:
                return "data analysis mentioned"
            elif 'mathematics' in input_str:
                return "mathematics mentioned"
            elif 'text' in input_str and 'processing' in input_str:
                return "text processing mentioned"
            else:
                # If no keywords match, return the input as a lowercase string
                return input_str