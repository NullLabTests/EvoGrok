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
        
        # Count the number of unique words
        word_count = len(words)
        
        # Return a formatted string with document type, word count, and sorted words
        return f"html document ({document_type}): {word_count} unique words - {','.join(sorted(words))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type
        if result_str.replace('.', '').isdigit():
            return f"{result_str} (number)"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            return f"string result: {len(words)} words - {','.join(sorted(words))}"
        
        # For other types of results, return the type and value
        return f"{type(result).__name__} result: {result_str}"
    
    except:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Return a formatted string with word counts and sorted words
        return f"text input: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"