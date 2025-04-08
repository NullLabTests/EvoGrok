import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lower_input = input_data.lower()
        if 'data analysis' in lower_input:
            return "data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "mathematics html document detected"
        elif 'text processing' in lower_input:
            return "text processing html document detected"
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
            # Join the cleaned values with commas
            result = ','.join(cleaned_values)
        else:
            # Check if the input is a valid number (integer or float)
            try:
                float(input_data)
                result = input_data
            except ValueError:
                # If not a number, return the input as a lowercase string
                result = input_data.lower()
        
        # Check if the result contains any HTML tags
        if '<' in result and '>' in result:
            return f"string with html tags detected: {result}"
        
        # Check if the result is a palindrome
        if result == result[::-1] and len(result) > 1:
            return f"palindrome detected: {result}"
        
        # Check if the result contains any digits
        if any(char.isdigit() for char in result):
            return f"string with digits detected: {result}"
        
        # Check if the result is a valid date (YYYY-MM-DD format)
        if re.match(r'^\d{4}-\d{2}-\d{2}$', result):
            return f"valid date detected: {result}"
        
        # Check if the result is a valid email address
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', result):
            return f"valid email address detected: {result}"
        
        # New feature: Check if the result is a Wikipedia URL
        if re.match(r'^https?://en\.wikipedia\.org/wiki/', result):
            return f"wikipedia url detected: {result}"
        
        # New feature: Check if the result is a valid ISBN-10 or ISBN-13
        if re.match(r'^(?=\d{10}$|(?=(?:\d{9})X$))\d{9}[\dX]$', result) or re.match(r'^(?=\d{13}$)\d{12}\d$', result):
            return f"valid isbn detected: {result}"
        
        # If no special conditions are met, return the processed result
        return result