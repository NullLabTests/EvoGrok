def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Identify the topic of the HTML document
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            return "unknown topic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process as a comma-separated list
        if isinstance(input_data, str):
            # Split the input by commas, sort the resulting list, and join it back
            sorted_items = sorted(input_data.split(','))
            return ','.join(item.strip().lower() for item in sorted_items if item.strip())
        else:
            # If not a string, return a string representation of the input
            return str(input_data).lower()