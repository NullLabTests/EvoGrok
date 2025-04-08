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
            # Sort and join the comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings from the sorted list
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            # Join the cleaned and sorted values
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.strip().lower().startswith('http'):
                    return f"url detected: {input_data}"
                elif '@' in input_data and '.' in input_data:
                    return f"email address detected: {input_data}"
                elif len(input_data) > 1 and input_data.isupper():
                    return f"all uppercase text detected: {input_data.lower()}"
                else:
                    # If no specific pattern is detected, check for potential HTML content
                    if '<' in input_data and '>' in input_data:
                        return f"potential html fragment detected: {input_data.lower()}"
                    # If still no specific pattern, return the input as a lowercase string
                    return str(input_data).lower()