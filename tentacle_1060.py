import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia page detected"
        else:
            # If no specific type is detected, check for related keywords
            keywords = ['data', 'analysis', 'mathematics', 'text', 'processing', 'wikipedia']
            detected_keywords = [kw for kw in keywords if kw in input_data.lower()]
            if detected_keywords:
                return f"potential {' '.join(detected_keywords)} wikipedia page detected"
            else:
                return "generic wikipedia page detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings, convert to lowercase, and remove duplicates
            cleaned_values = list(dict.fromkeys([value.strip().lower() for value in sorted_values if value.strip()]))
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                return f"numeric value: {str(input_data).lower()}"
            except ValueError:
                # If not a number, check for specific patterns
                if input_data.strip().lower().startswith('wiki:'):
                    # Process Wikipedia-style links
                    wiki_content = input_data[5:].strip().lower()
                    # Check for known Wikipedia page titles
                    if 'data analysis' in wiki_content:
                        return f"wikipedia link to data analysis: {wiki_content}"
                    elif 'mathematics' in wiki_content:
                        return f"wikipedia link to mathematics: {wiki_content}"
                    elif 'text processing' in wiki_content:
                        return f"wikipedia link to text processing: {wiki_content}"
                    else:
                        return f"wikipedia link: {wiki_content}"
                elif any(keyword in input_data.lower() for keyword in ['data', 'analysis', 'mathematics', 'text', 'processing']):
                    # Detect keywords related to HTML document types
                    detected_keywords = [kw for kw in ['data', 'analysis', 'mathematics', 'text', 'processing'] if kw in input_data.lower()]
                    return f"potential {' '.join(detected_keywords)} wikipedia page content"
                else:
                    # Check for email addresses
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    email_matches = re.findall(email_pattern, input_data)
                    if email_matches:
                        return f"email address detected: {', '.join(email_matches)}"
                    
                    # If no specific pattern is detected, return the input as a lowercase string
                    return str(input_data).lower()