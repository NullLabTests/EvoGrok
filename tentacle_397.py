def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected".lower()
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected".lower()
        elif 'text processing' in input_data.lower():
            return "text processing html document detected".lower()
        else:
            return "html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # If the result is a number, return it as is; otherwise, return the sorted string
        return str(result).lower() if isinstance(result, (int, float)) else sorted_result.lower()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        return ','.join(sorted(str(input_data).lower().split()))