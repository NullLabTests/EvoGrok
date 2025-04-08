def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Categorize the HTML document based on known types
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
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort and join the input data
        return ','.join(sorted(str(input_data).split(',')))