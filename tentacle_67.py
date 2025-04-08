def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Categorize the HTML document based on known topics
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return 'data analysis html document detected'
        elif 'mathematics' in lower_input:
            return 'mathematics html document detected'
        elif 'text processing' in lower_input:
            return 'text processing html document detected'
        else:
            return 'unknown html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort and join the input data
        return ','.join(sorted(str(input_data).split(',')))