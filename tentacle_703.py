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
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values (from Parent2)
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.strip().lower().startswith('hello'):
                    return f"greeting detected: {input_data.lower()}"
                elif input_data.strip().lower().startswith('goodbye'):
                    return f"farewell detected: {input_data.lower()}"
                # New feature: Check for email patterns
                elif '@' in input_data and '.' in input_data.split('@')[-1]:
                    return f"email address detected: {input_data.lower()}"
                # New feature: Check for URL patterns
                elif input_data.strip().lower().startswith(('http://', 'https://')):
                    return f"url detected: {input_data.lower()}"
                # If no specific pattern matches, return the input as a lowercase string (from Parent1)
                return str(input_data).lower()