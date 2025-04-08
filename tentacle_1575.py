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
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                # Join the cleaned values with commas and lowercase the result
                return ','.join(cleaned_values).lower()
            elif input_data.strip():
                # If the input is a non-empty string without commas, return it as a lowercase string
                return input_data.lower()
            else:
                # If the input is an empty string or only whitespace, return "empty input"
                return "empty input"
        elif isinstance(input_data, (list, tuple)):
            # If the input is a list or tuple, sort it, convert to strings, and join with commas
            sorted_items = sorted(map(str, input_data))
            return ','.join(sorted_items).lower()
        else:
            # For other non-string inputs, convert to string and lowercase
            return str(input_data).lower()