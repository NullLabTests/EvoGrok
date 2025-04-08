import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Classify HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        
        # Attempt to extract the title from the HTML
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip().lower()
            return f"html document detected: {title}"
        
        # If no specific classification, check for Wikipedia pages
        if 'wikipedia' in lowercase_input:
            return "wikipedia html document detected"
        
        # Generic HTML document detection
        return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return it with 5 decimal places
        if isinstance(result, (int, float)):
            return f"{result:.5f}".lower()
        
        # For other types of results, convert to string and lowercase
        return str(result).lower()
    
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
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
                lowercase_input = input_data.strip().lower()
                if lowercase_input in ['true', 'false']:
                    return lowercase_input
                elif lowercase_input.startswith('http'):
                    return 'url detected'
                elif lowercase_input.startswith('www.'):
                    return 'website detected'
                elif '@' in lowercase_input and '.' in lowercase_input:
                    return 'email address detected'
                elif re.match(r'^[a-f0-9]{32}$', lowercase_input):
                    return 'md5 hash detected'
                elif re.match(r'^[a-f0-9]{40}$', lowercase_input):
                    return 'sha1 hash detected'
                else:
                    # If no special patterns detected, return the input as a lowercase string
                    return lowercase_input