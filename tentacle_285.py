def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.lower().startswith('<!doctype'):
        # Check for specific Wikipedia page titles
        if 'data analysis' in input_str.lower():
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in input_str.lower():
            return "wikipedia page on mathematics detected"
        elif 'text processing' in input_str.lower():
            return "wikipedia page on text processing detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort and join the input
        return ','.join(sorted(input_str.split(',')))