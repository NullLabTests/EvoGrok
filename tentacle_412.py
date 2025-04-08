def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known titles
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'.lower()
        else:
            # Check for other common HTML document types
            if 'wikipedia' in input_data.lower():
                return 'wikipedia html document detected'.lower()
            elif '<html lang="en">' in input_data.lower():
                return 'english language html document detected'.lower()
            else:
                return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        return ','.join(sorted(str(result).split()))
    except:
        # If evaluation fails, process the input as text
        if isinstance(input_data, (list, tuple, set)):
            # If input is a collection, convert each item to string, lowercase, split, sort, and join
            processed_items = []
            for item in input_data:
                processed_items.extend(sorted(str(item).lower().split()))
            return ','.join(sorted(processed_items))
        elif isinstance(input_data, dict):
            # If input is a dictionary, process keys and values separately
            keys = ','.join(sorted([str(k).lower() for k in input_data.keys()]))
            values = ','.join(sorted([str(v).lower() for v in input_data.values()]))
            return f"keys:{keys},values:{values}"
        else:
            # For other types of input, convert to lowercase, split, sort, and join
            return ','.join(sorted(str(input_data).lower().split()))