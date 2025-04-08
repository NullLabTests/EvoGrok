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
        # Convert the result to a string, lowercase it, and add a prefix
        return f"evaluated result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                return f"sorted and cleaned string: {','.join(cleaned_values).lower()}"
            elif input_data.strip():
                # If the input is a non-empty string without commas, return it as a lowercase string
                return f"processed string: {input_data.lower()}"
            else:
                # If the input is an empty string or only whitespace, return "empty input"
                return "empty input detected"
        elif isinstance(input_data, (int, float, bool)):
            # For numeric or boolean inputs, convert to string and lowercase
            return f"numeric or boolean input: {str(input_data).lower()}"
        elif isinstance(input_data, list):
            # For list inputs, sort and join the elements
            sorted_list = sorted([str(item).strip() for item in input_data])
            return f"sorted list: {','.join(sorted_list).lower()}"
        else:
            # For other types of inputs, convert to string and lowercase
            return f"other input type: {str(input_data).lower()}"