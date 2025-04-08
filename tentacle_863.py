import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            # If no specific type is detected, check for other keywords
            if 'wikipedia' in input_data.lower():
                return "wikipedia html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove extra whitespace
        return re.sub(r'\s+', ' ', str(result).lower()).strip()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove extra whitespace from each value
            cleaned_values = [re.sub(r'\s+', ' ', value.strip()) for value in sorted_values]
            return ','.join(cleaned_values)
        else:
            # Convert to lowercase, remove extra whitespace, and replace multiple spaces with a single space
            processed_input = re.sub(r'\s+', ' ', input_data.lower()).strip()
            
            # Check for specific patterns in the processed input
            if re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', processed_input):
                return f"email address detected: {processed_input}"
            elif re.match(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', processed_input):
                return f"url detected: {processed_input}"
            elif re.match(r'^\d{4}-\d{2}-\d{2}$', processed_input):
                return f"date detected (YYYY-MM-DD): {processed_input}"
            elif re.match(r'^\d+(\.\d+)?$', processed_input):
                return f"number detected: {processed_input}"
            elif re.match(r'^[a-f0-9]{32}$', processed_input):
                return f"md5 hash detected: {processed_input}"
            elif re.match(r'^[a-f0-9]{40}$', processed_input):
                return f"sha1 hash detected: {processed_input}"
            else:
                return processed_input