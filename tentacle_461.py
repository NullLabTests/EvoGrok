def tentacle(input_data):
    """
    Process input data and return a transformed result based on its content and type.

    This function can handle HTML detection, mathematical expression evaluation,
    list processing, and string transformation.

    Args:
        input_data: The input to be processed. Can be any type.

    Returns:
        str: The processed result as a lowercase string.
    """
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()

    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str:
            return "data analysis html document detected"
        elif 'mathematics' in input_str:
            return "mathematics html document detected"
        elif 'text processing' in input_str:
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process as a list or return as is
        if ',' in input_str or ';' in input_str or '\n' in input_str:
            # Split the input using multiple delimiters
            items = input_str.replace(';', ',').replace('\n', ',').split(',')
            # Remove any empty strings and strip whitespace
            cleaned_items = [item.strip() for item in items if item.strip()]
            # Sort the list
            sorted_items = sorted(cleaned_items)
            # Join the sorted list
            return ','.join(sorted_items)
        else:
            # If no delimiters, return the input as a lowercase string
            return input_str