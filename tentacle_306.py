def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        else:
            document_type = 'unknown'
        
        # Extract and process words from the HTML content
        words = set()
        for word in input_data.lower().split():
            if word.isalnum():
                words.add(word)
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type] + list(words)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result: convert to string, split into words, remove non-alphanumeric
        words = [word for word in str(result).lower().split() if word.isalnum()]
        
        # If the result is a number, add its square root to the output
        if isinstance(result, (int, float)):
            import math
            words.append(str(round(math.sqrt(abs(result)), 2)))
        
        # Return a sorted, comma-separated list of processed words
        return ','.join(sorted(words))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove non-alphanumeric, sort, and join with commas
        words = [word for word in str(input_data).lower().split() if word.isalnum()]
        return ','.join(sorted(words))