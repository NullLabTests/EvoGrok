def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        # Detect specific Wikipedia pages
        if 'data analysis' in lowercase_input:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia page on text processing detected"
        else:
            # Check for other HTML content
            if 'class=' in lowercase_input or 'id=' in lowercase_input:
                # Extract and sort classes and ids
                classes = sorted(set(re.findall(r'class="([^"]*)"', lowercase_input)))
                ids = sorted(set(re.findall(r'id="([^"]*)"', lowercase_input)))
                result = "generic html document with styling detected"
                if classes:
                    result += f", classes: {', '.join(classes)}"
                if ids:
                    result += f", ids: {', '.join(ids)}"
                return result.lower()
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
                elif lowercase_input.startswith('html:'):
                    # Extract the content from the html pattern
                    content = lowercase_input.split('html:')[1].strip()
                    if 'class=' in content or 'id=' in content:
                        return f"html document with styling: {content}"
                    else:
                        return f"html document: {content}"
                else:
                    # Check for mathematical expressions in string format
                    if any(op in lowercase_input for op in ['+', '-', '*', '/', '**', '%']):
                        try:
                            result = eval(lowercase_input)
                            return str(result).lower()
                        except:
                            pass
                    # If no specific pattern matches, return the input as a lowercase string
                    return lowercase_input