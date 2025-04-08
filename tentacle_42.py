def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        if 'data analysis' in input_str:
            return "wikipedia data analysis page detected"
        elif 'mathematics' in input_str:
            return "wikipedia mathematics page detected"
        elif 'text processing' in input_str:
            return "wikipedia text processing page detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails and input contains commas, sort and join
        if ',' in input_str:
            return ','.join(sorted(input_str.split(',')))
        # If evaluation fails and no commas, return the input as a lowercase string
        else:
            return input_str