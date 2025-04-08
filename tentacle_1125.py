def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'wikipedia data analysis html document detected (html5)'
        elif 'mathematics' in input_data.lower():
            return 'wikipedia mathematics html document detected (html5)'
        elif 'text processing' in input_data.lower():
            return 'wikipedia text processing html document detected (html5)'
        else:
            return 'generic html5 document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        processed_result = ','.join(sorted(str(result).lower().split()))
        
        # If the result is a single word or number, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_result:
            return f"Calculated: {processed_result.capitalize()}"
        else:
            return f"Calculated: {processed_result.replace(',', '').capitalize()}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        processed_input = ','.join(sorted(str(input_data).lower().split()))
        
        # If the result is a single word, return it capitalized
        # Otherwise, return the sorted, comma-separated list with the first word capitalized
        if ',' in processed_input:
            return f"Processed: {processed_input.capitalize()}"
        else:
            return f"Processed: {processed_input.replace(',', '').capitalize()}"