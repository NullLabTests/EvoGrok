def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known titles
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            return ','.join(sorted_values)
        else:
            # Return the input as a lowercase string
            return str(input_data).lower()