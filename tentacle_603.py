def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'.lower()
        else:
            return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it as is
            return str(result)
        else:
            # Convert the result to a string, split it into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            return processed_result
    except:
        # If evaluation fails, process the input
        if isinstance(input_data, (list, tuple, set)):
            # If input is a collection, sort its elements and join with commas
            return ','.join(map(str, sorted(input_data)))
        elif isinstance(input_data, dict):
            # If input is a dictionary, sort keys and join key-value pairs with commas
            return ','.join(f"{k}:{v}" for k, v in sorted(input_data.items()))
        else:
            # For other types, convert to string, split into words, sort, and join with commas
            return ','.join(sorted(str(input_data).lower().split()))