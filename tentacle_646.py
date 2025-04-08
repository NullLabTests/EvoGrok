def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Detect specific HTML document types based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If no specific type is detected, try to evaluate as a mathematical expression
            try:
                result = eval(input_data)
                return f"html document evaluated: {str(result).lower()}"
            except:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            non_empty_values = [value.strip() for value in sorted_values if value.strip()]
            return ','.join(non_empty_values).lower()
        else:
            # If no commas, check if the input is a valid number
            try:
                float(input_data)
                return f"numeric value: {input_data.lower()}"
            except ValueError:
                # If not a number, return the input as a lowercase string
                return str(input_data).lower()