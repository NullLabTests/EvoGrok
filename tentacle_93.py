def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of Wikipedia page based on the title
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis page detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics page detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing page detected"
        else:
            return "wikipedia page detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, sort its characters, and join them
        return ','.join(sorted(str(result)))
    except:
        # If evaluation fails, split the input by commas, sort the parts, and join them
        return ','.join(sorted(input_data.split(',')))