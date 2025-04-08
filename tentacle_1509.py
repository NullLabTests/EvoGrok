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
        result = str(input_data)
        
        # Check for comma-separated values
        if ',' in result:
            # Sort and join comma-separated values
            sorted_values = sorted(result.split(','))
            # Remove any empty strings and strip whitespace
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            result = ','.join(cleaned_values)
        
        # Check if the result is a valid number (integer or float)
        try:
            float(result)
            return result
        except ValueError:
            # If not a number, process as a string
            result = result.lower()
            
            # Check for HTML tags
            if '<' in result and '>' in result:
                return f"string with html tags detected: {result}"
            
            # Check if the result is a palindrome
            if result == result[::-1] and len(result) > 1:
                return f"palindrome detected: {result}"
            
            # Check for digits
            if any(char.isdigit() for char in result):
                return f"string with digits detected: {result}"
            
            # Check for valid date (YYYY-MM-DD format)
            if re.match(r'^\d{4}-\d{2}-\d{2}$', result):
                return f"valid date detected: {result}"
            
            # Check for valid email address
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', result):
                return f"valid email address detected: {result}"
            
            # New feature: Check for Wikipedia page titles
            if result.startswith('wikipedia page on '):
                topic = result[len('wikipedia page on '):]
                return f"Wikipedia page on {topic.capitalize()} detected"
            
            # New feature: Check for common programming language keywords
            programming_keywords = ['if', 'else', 'for', 'while', 'def', 'class', 'import']
            if any(keyword in result.split() for keyword in programming_keywords):
                return f"programming code detected: {result}"
            
            # If no special conditions are met, return the processed result
            return result