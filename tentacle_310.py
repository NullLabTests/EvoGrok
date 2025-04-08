def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on content
        document_type = 'unknown'
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        elif 'wikipedia' in input_data.lower():
            document_type = 'wikipedia'
        
        # Extract and process words from the HTML content
        words = set(input_data.lower().split())
        words.discard('<!doctype')
        words.discard('html')
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type] + list(words)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, sort them, and join with commas
        return ','.join(sorted(str(result).lower().split()))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        return ','.join(sorted(str(input_data).lower().split()))