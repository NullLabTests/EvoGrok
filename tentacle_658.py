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
        
        # Calculate the average word length
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        
        # Return a formatted string with document type, word count, average word length, and sorted words
        return f"html document ({document_type}): {word_count} unique words, avg length {avg_word_length:.2f} - {','.join(sorted(words))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and a simple calculation
        if result_str.replace('.', '').isdigit():
            calculation = result * 2 if isinstance(result, int) else result ** 2
            return f"{result_str} (number): doubled={calculation:.2f}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            return f"string result: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        
        # For other types of results, return the type, value, and a simple representation
        return f"{type(result).__name__} result: {result_str}, repr={repr(result)}"
    
    except:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Calculate the average word length
        avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
        
        # Return a formatted string with word counts, average word length, and sorted words
        return f"text input: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f} - {','.join(sorted(words))}"