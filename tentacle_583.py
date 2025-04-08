def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title and content
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        elif 'wikipedia' in lowercase_input:
            return "wikipedia html document detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # For numbers, return the result as is
            return str(result).lower()
        elif isinstance(result, str):
            # For strings, split, sort, and join
            sorted_result = ','.join(sorted(result.split()))
            return sorted_result.lower()
        else:
            # For other types, convert to string, split, sort, and join
            sorted_result = ','.join(sorted(str(result).split()))
            return sorted_result.lower()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        return ','.join(sorted(str(input_data).lower().split()))