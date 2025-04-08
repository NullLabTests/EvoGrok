def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect specific types of HTML documents
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return 'data analysis html document detected'
        elif 'mathematics' in lowercase_input:
            return 'mathematics html document detected'
        elif 'text processing' in lowercase_input:
            return 'text processing html document detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort its characters, and join them
        return ','.join(sorted(str(result)))
    except:
        # If evaluation fails, sort and join the input characters
        return ','.join(sorted(str(input_data)))