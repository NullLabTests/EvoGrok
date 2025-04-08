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
            # Join the cleaned and sorted values
            result = ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                result = str(input_data).lower()
            except ValueError:
                # If not a number, reverse the string
                result = input_data[::-1].lower()
        
        # Check if the result contains any HTML tags
        if '<' in result and '>' in result:
            return f"string with html tags detected: {result}"
        
        # New feature: Check for common programming language keywords
        programming_keywords = ['if', 'else', 'for', 'while', 'def', 'class', 'import']
        if any(keyword in result.lower() for keyword in programming_keywords):
            return f"potential code snippet detected: {result}"
        
        # New feature: Check for common data formats
        if result.startswith('{'):
            return f"potential JSON object detected: {result}"
        elif result.startswith('['):
            return f"potential JSON array detected: {result}"
        
        # If no special conditions are met, return the processed result
        return result