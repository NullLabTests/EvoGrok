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
            # Check for potential HTML document types based on keywords
            keywords = ['data', 'analysis', 'mathematics', 'text', 'processing', 'wiki', 'wikipedia']
            detected_keywords = [kw for kw in keywords if kw in input_data.lower()]
            if detected_keywords:
                return f"potential {' '.join(detected_keywords)} html document detected"
            else:
                # Check for specific Wikipedia page patterns
                if 'class="wiki"' in input_data.lower() or 'id="wiki"' in input_data.lower():
                    return "wikipedia html document detected"
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
            # Check if all values are numbers
            if all(value.replace('.', '', 1).isdigit() for value in cleaned_values):
                # If all values are numbers, return them as a sorted list
                return str(sorted([float(value) for value in cleaned_values]))
            else:
                # If not all values are numbers, join the sorted strings
                return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.strip().lower().startswith('wiki:'):
                    # Process Wikipedia-style links
                    return f"wikipedia link: {input_data[5:].strip().lower()}"
                elif any(keyword in input_data.lower() for keyword in ['data', 'analysis', 'mathematics', 'text', 'processing']):
                    # Detect keywords related to HTML document types
                    detected_keywords = [kw for kw in ['data', 'analysis', 'mathematics', 'text', 'processing'] if kw in input_data.lower()]
                    return f"potential {' '.join(detected_keywords)} html document"
                else:
                    # Check for URL patterns
                    if input_data.startswith(('http://', 'https://')):
                        return f"url detected: {input_data.lower()}"
                    # If no specific pattern is detected, return the input as a lowercase string
                    return str(input_data).lower()