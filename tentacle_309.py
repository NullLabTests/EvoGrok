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
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        result_words = str(result).lower().split()
        
        # If the result is a single number, return it as is
        if len(result_words) == 1 and result_words[0].replace('.', '').isdigit():
            return result_words[0]
        
        # Otherwise, return sorted words
        return ','.join(sorted(result_words))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        return ','.join(sorted(str(input_data).lower().split()))