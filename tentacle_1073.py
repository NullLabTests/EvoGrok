def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'.lower()
        else:
            return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it with a descriptive message
            return f"mathematical result: {result}"
        else:
            # Convert the result to a string, split it into words, sort them, and join with commas
            processed_result = ','.join(sorted(str(result).lower().split()))
            return f"processed result: {processed_result}"
    except:
        # If evaluation fails, process the input
        if isinstance(input_data, (int, float)):
            # If input is a number, return it with a descriptive message
            return f"numeric input: {input_data}"
        else:
            # Convert the input to a string, split it into words, sort them, and join with commas
            processed_input = ','.join(sorted(str(input_data).lower().split()))
            
            # Check if the processed input contains any HTML document types
            if any(doc_type in processed_input for doc_type in ['data analysis', 'mathematics', 'text processing']):
                return f"potential {processed_input.split(',')[0]} html document detected"
            else:
                return f"processed input: {processed_input}"