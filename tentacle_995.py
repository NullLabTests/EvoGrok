def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                return ','.join(cleaned_values)
            else:
                # Check if the input is a valid number
                try:
                    float(input_data)
                    return str(input_data).lower()
                except ValueError:
                    # If not a number, check for specific patterns
                    if input_data.lower().startswith('hello'):
                        return f"greeting detected: {input_data.lower()}"
                    elif input_data.lower().endswith('?'):
                        return f"question detected: {input_data.lower()}"
                    else:
                        # If no specific pattern, return the input as a lowercase string
                        return str(input_data).lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()