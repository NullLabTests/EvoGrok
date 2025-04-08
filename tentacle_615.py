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
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).strip().lower()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check for comma-separated values
            if ',' in input_data:
                # Sort and join comma-separated values, then convert to lowercase
                sorted_values = sorted(input_data.split(','))
                return f"sorted values: {','.join(sorted_values).lower()}"
            # Check for potential list or dictionary
            elif input_data.strip().startswith('[') and input_data.strip().endswith(']'):
                try:
                    # Attempt to parse as a list
                    parsed_list = eval(input_data)
                    return f"list detected: {','.join(map(str, parsed_list)).lower()}"
                except:
                    pass
            elif input_data.strip().startswith('{') and input_data.strip().endswith('}'):
                try:
                    # Attempt to parse as a dictionary
                    parsed_dict = eval(input_data)
                    return f"dictionary detected: {','.join(f'{k}:{v}' for k,v in parsed_dict.items()).lower()}"
                except:
                    pass
        
        # If no special processing applies, return the input as a lowercase string
        return str(input_data).lower()