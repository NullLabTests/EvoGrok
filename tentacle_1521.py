def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove leading/trailing whitespace
        return str(result).strip().lower()
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            # Remove leading/trailing whitespace
            cleaned_input = input_data.strip()
            
            if ',' in cleaned_input:
                # Sort and join comma-separated values
                sorted_values = sorted(cleaned_input.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            else:
                # Check if the input is a non-empty string of words
                if cleaned_input:
                    # Split the input into words, sort them, remove duplicates, and join them back
                    words = sorted(set(cleaned_input.lower().split()))
                    # Join words with commas for a different output format
                    return ','.join(words)
                else:
                    # Return an empty string for empty input
                    return ''
        else:
            # For non-string inputs, convert to lowercase string and remove leading/trailing whitespace
            return str(input_data).strip().lower()