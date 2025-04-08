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
        return f"evaluated result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings that might result from leading/trailing commas
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return f"sorted and cleaned: {','.join(cleaned_values)}"
            else:
                # Convert the input to lowercase and remove any leading/trailing whitespace
                return f"processed string: {input_data.strip().lower()}"
        else:
            # For non-string inputs, convert to string and lowercase
            return f"non-string input: {str(input_data).lower()}"