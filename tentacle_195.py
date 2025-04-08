def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of Wikipedia page based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia page detected".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia page detected".lower()
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia page detected".lower()
        else:
            return "unknown wikipedia page detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort its characters
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # If the input contains commas, sort the split parts
            return ','.join(sorted(input_data.split(',')))
        else:
            # Otherwise, sort the characters of the input
            return ','.join(sorted(str(input_data).lower()))