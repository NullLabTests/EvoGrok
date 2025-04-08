def tentacle(input_data):
    """
    Process input data based on its type and content.

    This function first checks if the input is an HTML document related to
    specific topics (data analysis, mathematics, or text processing). If so,
    it returns a corresponding message. Otherwise, it attempts to evaluate
    the input as a mathematical expression. If evaluation fails, it sorts
    and joins the input elements (if comma-separated) or returns the input
    as a lowercase string.

    Args:
        input_data (str): The input data to process.

    Returns:
        str: Processed output based on the input's content and type.
    """
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()

    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific HTML document types
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
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, check if the input is comma-separated
        if ',' in input_str:
            # Sort and join the elements
            return ','.join(sorted(input_str.split(',')))
        else:
            # Return the input as a lowercase string
            return input_str