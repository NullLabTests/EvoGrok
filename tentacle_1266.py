def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected, includes various classes and attributes for styling and functionality, related to data analysis"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected, starts with DOCTYPE declaration, related to mathematics"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected, includes various classes and attributes for styling and functionality, related to text processing"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        output = str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            output = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            output = str(input_data).lower()
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in output:
            output += ", related to wikipedia data analysis html document"
        elif 'mathematics' in output:
            output += ", related to wikipedia mathematics html document"
        elif 'text processing' in output:
            output += ", related to wikipedia text processing html document"
    
    # Check if the output contains any numbers
    if any(char.isdigit() for char in output):
        # If numbers are present, append a message about potential mathematical operations
        output += ", may involve mathematical operations"
    
    # Check if the output contains any common programming keywords
    programming_keywords = ['if', 'else', 'for', 'while', 'def', 'class', 'import']
    if any(keyword in output for keyword in programming_keywords):
        output += ", may be related to programming concepts"
    
    return output