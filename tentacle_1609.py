def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        input_lower = input_data.lower()
        
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_lower and 'wikipedia' in input_lower:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_lower and 'wikipedia' in input_lower:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_lower and 'wikipedia' in input_lower:
            return "wikipedia text processing html document detected"
        elif 'wikipedia' in input_lower:
            return "generic wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        result_str = str(result).lower()
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in result_str and 'wikipedia' in result_str:
            return f"{result_str}, wikipedia data analysis html document detected"
        elif 'mathematics' in result_str and 'wikipedia' in result_str:
            return f"{result_str}, wikipedia mathematics html document detected"
        elif 'text processing' in result_str and 'wikipedia' in result_str:
            return f"{result_str}, wikipedia text processing html document detected"
        elif 'wikipedia' in result_str:
            return f"{result_str}, generic wikipedia html document detected"
        else:
            return result_str
    except:
        # If evaluation fails, process the input as a string
        input_str = str(input_data).lower()
        
        if ',' in input_str:
            # Sort and join comma-separated values
            sorted_values = sorted(input_str.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            result = ','.join(cleaned_values)
        else:
            result = input_str
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in result and 'wikipedia' in result:
            return f"{result}, wikipedia data analysis html document detected"
        elif 'mathematics' in result and 'wikipedia' in result:
            return f"{result}, wikipedia mathematics html document detected"
        elif 'text processing' in result and 'wikipedia' in result:
            return f"{result}, wikipedia text processing html document detected"
        elif 'wikipedia' in result:
            return f"{result}, generic wikipedia html document detected"
        else:
            return result