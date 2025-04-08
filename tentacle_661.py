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
        
        # Count the number of unique words in the document
        word_count = len(words)
        
        # Calculate the average length of words
        avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
        
        # Return a sorted, comma-separated list of detected elements
        # Include the document type, word count, average word length, and sorted unique words
        return ','.join(sorted(['html document', document_type, 
                                f'word count: {word_count}', 
                                f'average word length: {avg_word_length:.2f}'] + list(words)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words
        result_words = str(result).lower().split()
        
        # Calculate the sum of numeric values in the result
        numeric_sum = sum(float(word) for word in result_words if word.replace('.', '').isdigit())
        
        # Calculate the average length of words in the result
        avg_word_length = sum(len(word) for word in result_words) / len(result_words) if result_words else 0
        
        # Sort the words and join with commas
        sorted_words = ','.join(sorted(result_words))
        
        # Return the sorted words along with the sum of numeric values and average word length
        return f'{sorted_words}, numeric sum: {numeric_sum}, average word length: {avg_word_length:.2f}'
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words
        input_words = str(input_data).lower().split()
        
        # Calculate the average length of words
        avg_word_length = sum(len(word) for word in input_words) / len(input_words) if input_words else 0
        
        # Sort the words and join with commas
        sorted_words = ','.join(sorted(input_words))
        
        # Return the sorted words along with the average word length
        return f'{sorted_words}, average word length: {avg_word_length:.2f}'