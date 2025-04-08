def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Check for specific types of HTML documents
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
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
        if isinstance(input_data, str):
            input_str = input_data.strip().lower()
            
            # Check for special patterns
            if input_str.startswith('http://') or input_str.startswith('https://'):
                return f"url detected: {input_str}"
            
            if '@' in input_str and '.' in input_str.split('@')[-1]:
                return f"email detected: {input_str}"
            
            # Check for potential HTML fragments
            if '<' in input_str and '>' in input_str:
                return f"html fragment detected: {input_str}"
            
            # Check for JSON-like structures
            if input_str.startswith('{') and input_str.endswith('}'):
                return f"json object detected: {input_str}"
            elif input_str.startswith('[') and input_str.endswith(']'):
                return f"json array detected: {input_str}"
            
            # Process comma-separated values
            if ',' in input_str:
                sorted_values = sorted(input_str.split(','))
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                result = ','.join(cleaned_values)
            else:
                result = input_str
            
            # Return the processed result
            return result
        else:
            # If input is not a string, convert it to a string and return
            return str(input_data).lower()