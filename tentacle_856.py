def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return "data analysis html document detected"
        elif 'mathematics' in input_lower:
            return "mathematics html document detected"
        elif 'text processing' in input_lower:
            return "text processing html document detected"
        elif 'wikipedia' in input_lower:
            return "wikipedia html document detected"
        elif 'html5' in input_lower:
            return "html5 document detected"
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
            # Remove any empty strings from the sorted list
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.strip().lower().startswith('http'):
                    return f"URL detected: {input_data}"
                elif '@' in input_data and '.' in input_data:
                    return f"Email address detected: {input_data}"
                elif len(input_data) > 1 and input_data.isupper():
                    return f"All uppercase text detected: {input_data.lower()}"
                elif input_data.strip().lower().startswith('error'):
                    return f"Error message detected: {input_data}"
                elif input_data.strip().lower().startswith('warning'):
                    return f"Warning message detected: {input_data}"
                elif input_data.strip().isdigit():
                    return f"Integer detected: {input_data}"
                else:
                    # If no specific pattern matches, return the input as a lowercase string
                    return str(input_data).lower()