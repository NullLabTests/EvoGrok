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
            # For unknown HTML types, attempt to extract the title
            title_start = input_data.lower().find('<title>')
            title_end = input_data.lower().find('</title>')
            if title_start != -1 and title_end != -1:
                title = input_data[title_start+7:title_end].strip()
                return f"unknown html document detected: {title}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and sort any comma-separated values
        result_str = str(result).lower()
        if ',' in result_str:
            sorted_values = sorted(result_str.split(','))
            cleaned_values = [value.strip() for value in sorted_values]
            return ','.join(cleaned_values)
        return result_str
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any leading/trailing whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values]
                return ','.join(cleaned_values).lower()
            elif input_data.strip():
                # If the input is a non-empty string without commas, return it as a lowercase string
                return input_data.lower()
            else:
                # If the input is an empty string or only whitespace, return "empty input"
                return "empty input"
        else:
            # For non-string inputs, convert to string, lowercase, and sort any comma-separated values
            input_str = str(input_data).lower()
            if ',' in input_str:
                sorted_values = sorted(input_str.split(','))
                cleaned_values = [value.strip() for value in sorted_values]
                return ','.join(cleaned_values)
            return input_str