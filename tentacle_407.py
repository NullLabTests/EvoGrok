def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
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
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if the input is a comma-separated list
            if ',' in input_data:
                # Sort and join the split input
                sorted_items = sorted(input_data.split(','))
                return ','.join(item.strip().lower() for item in sorted_items if item.strip())
            else:
                # If not a list, return the input as a lowercase string
                return input_data.strip().lower()
        elif isinstance(input_data, (list, tuple, set)):
            # If input is a collection, sort and join its elements
            sorted_items = sorted(str(item) for item in input_data)
            return ','.join(item.strip().lower() for item in sorted_items if item.strip())
        else:
            # For other types, convert to string and lowercase
            return str(input_data).lower()