def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            result = ','.join(cleaned_values)
        else:
            # If no commas, return the input as a lowercase string
            result = str(input_data).lower()
        
        # Check if the result looks like a URL
        if result.startswith('http://') or result.startswith('https://'):
            return f"url detected: {result}"
        
        # Check if the result looks like an email address
        if '@' in result and '.' in result.split('@')[-1]:
            return f"email detected: {result}"
        
        # If no special patterns detected, return the processed result
        return result