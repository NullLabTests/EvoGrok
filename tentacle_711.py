def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
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
            # Join the cleaned and sorted values
            result = ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                result = str(input_data).lower()
            except ValueError:
                # If not a number, reverse the string
                result = input_data[::-1].lower()
        
        # New feature: Check if the result contains any HTML tags
        if '<' in result and '>' in result:
            return f"string with html tags detected: {result}"
        
        # New feature: Check for specific keywords related to known HTML document types
        lowercase_result = result.lower()
        if 'data analysis' in lowercase_result:
            return f"data analysis related content detected: {result}"
        elif 'mathematics' in lowercase_result:
            return f"mathematics related content detected: {result}"
        elif 'text processing' in lowercase_result:
            return f"text processing related content detected: {result}"
        
        # If no special conditions are met, return the processed result
        return result