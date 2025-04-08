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
            # Remove any empty strings and strip whitespace
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            # If all values are numeric, sum them up
            if all(value.replace('.', '').isdigit() for value in cleaned_values):
                return str(sum(float(value) for value in cleaned_values)).lower()
            else:
                return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.lower().startswith('hello'):
                    return f"greeting detected: {input_data.lower()}"
                elif 'python' in input_data.lower():
                    return f"python reference detected: {input_data.lower()}"
                elif input_data.lower().startswith('error'):
                    return f"error message detected: {input_data.lower()}"
                else:
                    # If no specific pattern is detected, return the input as a lowercase string
                    return str(input_data).lower()