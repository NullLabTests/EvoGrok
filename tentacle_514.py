def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
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
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values (enhanced from Parent2)
            sorted_values = sorted(input_data.split(','))
            cleaned_values = [value.strip() for value in sorted_values]
            # Remove duplicates while preserving order
            unique_values = []
            for value in cleaned_values:
                if value not in unique_values:
                    unique_values.append(value)
            return ','.join(unique_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for common text patterns
                if input_data.strip().lower() in ['true', 'false']:
                    return input_data.strip().lower()
                elif input_data.strip().startswith('http'):
                    return 'url detected'
                else:
                    # If no special patterns detected, return the input as a lowercase string
                    return str(input_data).lower()