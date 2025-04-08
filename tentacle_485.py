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
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_values = [v.strip() for v in sorted_values if v.strip()]
            # Convert each value to lowercase
            lowercased_values = [v.lower() for v in cleaned_values]
            return ','.join(lowercased_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(float(input_data)).lower()
            except ValueError:
                # If it's not a number, check if it's a short string
                if len(input_data) <= 5:
                    # For short strings, return in uppercase
                    return input_data.upper()
                else:
                    # For longer strings, return in lowercase
                    return input_data.lower()