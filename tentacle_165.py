def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'
        else:
            return 'html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort the characters
        return ','.join(sorted(str(result).lower()))
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # If the input contains commas, sort the split values
            return ','.join(sorted(input_data.split(',')))
        else:
            # Otherwise, return the lowercase input
            return input_data.lower()