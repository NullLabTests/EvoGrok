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
        total_length = sum(len(word) for word in words)
        avg_word_length = total_length / word_count if word_count > 0 else 0
        
        # Count the number of digits in the HTML content
        digit_count = sum(c.isdigit() for c in input_data)
        
        # Return a formatted string with document type, word count, average word length, digit count, and sorted words
        return f"html document ({document_type}): {word_count} unique words, avg length {avg_word_length:.2f}, {digit_count} digits - {','.join(sorted(words))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and some basic statistics
        if result_str.replace('.', '').replace('-', '').isdigit():
            number = float(result_str)
            return f"{number} (number): min={min(number, 0)}, max={max(number, 0)}, abs={abs(number)}, square={number**2}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
            return f"string result from math eval: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f} - {','.join(sorted(words))}"
        
        # For other types of results, return the type, value, and a string representation
        return f"{type(result).__name__} result from math eval: {result} - {str(result)}"
    
    except:
        # If evaluation fails, process the input as text
        input_str = str(input_data).lower()
        words = input_str.split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Calculate the average word length
        total_length = sum(len(word) for word in words)
        avg_word_length = total_length / total_words if total_words > 0 else 0
        
        # Count the number of digits in the input
        digit_count = sum(c.isdigit() for c in input_str)
        
        # Return a formatted string with word counts, average word length, digit count, and sorted words
        return f"text input: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f}, {digit_count} digits - {','.join(sorted(words))}"