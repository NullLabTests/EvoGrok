import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia page on text processing detected"
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
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas and convert to lowercase
            return ','.join(cleaned_values).lower()
        else:
            # Check if the input is a valid number
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
                elif lowercase_input.startswith('{') and lowercase_input.endswith('}'):
                    # Check for JSON-like structure
                    try:
                        parsed_json = json.loads(input_data)
                        return json.dumps(parsed_json, sort_keys=True).lower()
                    except json.JSONDecodeError:
                        pass
                elif '://' in input_data:
                    # Check for URL-like pattern
                    return f"url detected: {input_data.lower()}"
                else:
                    # New feature: Check for specific keywords related to known topics
                    if 'data analysis' in lowercase_input:
                        return "data analysis topic detected"
                    elif 'mathematics' in lowercase_input:
                        return "mathematics topic detected"
                    elif 'text processing' in lowercase_input:
                        return "text processing topic detected"
                    else:
                        # If no specific pattern matches, return the input as a lowercase string
                        return lowercase_input