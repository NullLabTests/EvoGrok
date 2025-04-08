import re

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
            # Extract the title from the HTML if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().lower()
                # Check if the title contains keywords from known document types
                if 'data' in title and 'analysis' in title:
                    return "data analysis html document detected"
                elif 'math' in title or 'mathematics' in title:
                    return "mathematics html document detected"
                elif 'text' in title and 'processing' in title:
                    return "text processing html document detected"
                else:
                    return f"html document detected: {title}"
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
            # If all values are numbers, sum them up
            if all(value.replace('.', '', 1).isdigit() for value in cleaned_values):
                return str(sum(float(value) for value in cleaned_values)).lower()
            else:
                return ','.join(cleaned_values).lower()
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, check for common text patterns
                if input_data.strip().isupper():
                    return input_data.lower() + " (was all uppercase)"
                elif len(input_data) > 50:
                    return input_data[:50].lower() + "... (truncated)"
                else:
                    return input_data.lower()