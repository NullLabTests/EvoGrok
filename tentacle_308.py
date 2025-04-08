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
        words = set(input_data.lower().split())
        words.discard('<!doctype')
        words.discard('html')
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type] + list(words)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result: convert to string, split into words, remove non-alphanumeric characters
        processed_result = ''.join(c.lower() if c.isalnum() else ' ' for c in str(result))
        words = processed_result.split()
        
        # Calculate the sum of numeric values in the result
        numeric_sum = sum(int(word) for word in words if word.isdigit())
        
        # Return a sorted, comma-separated list of processed words and the numeric sum
        return ','.join(sorted(words + [str(numeric_sum)]))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, remove non-alphanumeric characters, split into words, sort them, and join with commas
        processed_input = ''.join(c.lower() if c.isalnum() else ' ' for c in str(input_data))
        words = processed_input.split()
        
        # Calculate the length of the processed input
        input_length = len(processed_input)
        
        # Return a sorted, comma-separated list of processed words and the input length
        return ','.join(sorted(words + [str(input_length)]))