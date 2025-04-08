def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known titles
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected".lower()
        elif 'text processing' in input_data.lower():
            return "text processing html document detected".lower()
        else:
            return "generic html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort its characters
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # If the input contains commas, sort and join the split parts
            return ','.join(sorted(input_data.split(',')))
        else:
            # Otherwise, return the input as a lowercase string
            return str(input_data).lower()