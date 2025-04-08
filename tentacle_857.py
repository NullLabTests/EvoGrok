def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "Wikipedia page on Data Analysis detected"
        elif 'mathematics' in input_data.lower():
            return "Wikipedia page on Mathematics detected"
        elif 'text processing' in input_data.lower():
            return "Wikipedia page on Text Processing detected"
        else:
            return "Generic HTML document detected"
    
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
                elif input_data.strip().isdigit():
                    return f"Integer detected: {input_data}"
                elif any(char.isdigit() for char in input_data) and any(char.isalpha() for char in input_data):
                    return f"Alphanumeric string detected: {input_data.lower()}"
                else:
                    # If no specific pattern matches, return the input as a lowercase string
                    return str(input_data).lower()