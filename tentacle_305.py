def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        document_type = 'unknown'
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        
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
        
        # Calculate the sum of numeric values in the result
        numeric_sum = sum(float(word) for word in words if word.replace('.', '').isdigit())
        
        # Return a sorted, comma-separated list of processed words and the numeric sum
        return ','.join(sorted(words + [str(numeric_sum)]))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove non-alphanumeric
        words = [word for word in str(input_data).lower().split() if word.isalnum()]
        
        # Calculate the length of the input string
        input_length = len(str(input_data))
        
        # Return a sorted, comma-separated list of processed words and the input length
        return ','.join(sorted(words + [str(input_length)]))