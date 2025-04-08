def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Categorize the HTML document based on its content
        if 'data analysis' in input_data.lower():
            return 'data analysis html document'
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document'
        elif 'text processing' in input_data.lower():
            return 'text processing html document'
        else:
            return 'unknown html document'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a comma-separated list
        return ','.join(sorted(str(input_data).split(',')))