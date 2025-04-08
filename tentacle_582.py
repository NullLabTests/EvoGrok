def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title and content
        lowercase_input = input_data.lower()
        
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected".lower()
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected".lower()
        elif 'text processing' in lowercase_input:
            return "text processing html document detected".lower()
        elif 'wikipedia' in lowercase_input:
            return "wikipedia html document detected".lower()
        else:
            return "html document detected".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        
        # Check if the result contains any numbers
        if any(char.isdigit() for char in sorted_result):
            return f"mathematical result: {sorted_result}".lower()
        else:
            return f"non-numeric result: {sorted_result}".lower()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        
        # Check if the processed input contains any numbers
        if any(char.isdigit() for char in processed_input):
            return f"text with numbers: {processed_input}".lower()
        else:
            return f"text without numbers: {processed_input}".lower()