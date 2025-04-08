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
            return "generic wikipedia html document detected"
    
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
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            return ','.join(cleaned_values).lower()
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                lowercase_input = input_data.strip().lower()
                if lowercase_input.startswith('wiki:'):
                    # Extract the topic from the wiki pattern
                    topic = lowercase_input.split('wiki:')[1].strip()
                    return f"wikipedia page on {topic} detected"
                elif lowercase_input.startswith('html:'):
                    # Extract the HTML content and process it
                    html_content = lowercase_input.split('html:')[1].strip()
                    if 'data analysis' in html_content:
                        return "data analysis html document detected"
                    elif 'mathematics' in html_content:
                        return "mathematics html document detected"
                    elif 'text processing' in html_content:
                        return "text processing html document detected"
                    else:
                        return "generic html document detected"
                else:
                    # If no specific pattern is detected, return the input as a lowercase string
                    return lowercase_input