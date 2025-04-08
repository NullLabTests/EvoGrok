def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of Wikipedia page based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia page detected".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia page detected".lower()
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia page detected".lower()
        else:
            return "generic wikipedia page detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort its characters
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, split the input by commas, sort the parts, and join them
        return ','.join(sorted(str(input_data).lower().split(',')))