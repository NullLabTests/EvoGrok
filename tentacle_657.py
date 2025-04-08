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
        
        # Check for specific keywords related to the document type
        related_keywords = {
            'data analysis': ['statistics', 'visualization', 'modeling'],
            'mathematics': ['algebra', 'geometry', 'calculus'],
            'text processing': ['nlp', 'tokenization', 'stemming']
        }
        relevant_keywords = set()
        for keyword in related_keywords.get(document_type, []):
            if keyword in words:
                relevant_keywords.add(keyword)
        
        # Return a formatted string with document type, word count, sorted words, and relevant keywords
        return f"HTML document ({document_type}): {word_count} unique words - {','.join(sorted(words))}. Relevant keywords: {','.join(sorted(relevant_keywords))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and a simple calculation
        if result_str.replace('.', '').isdigit():
            calculation = result * 2
            return f"{result_str} (number) - Double: {calculation}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            return f"String result: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        
        # For other types of results, return the type, value, and a simple representation
        return f"{type(result).__name__} result: {result_str} - Simple repr: {repr(result)}"
    
    except:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Check for mathematical operators
        operators = set(['+', '-', '*', '/', '**', '%'])
        detected_operators = operators.intersection(set(input_data))
        
        # Return a formatted string with word counts, sorted words, and detected operators
        return f"Text input: {total_words} words, {unique_words} unique - {','.join(sorted(words))}. Detected operators: {','.join(sorted(detected_operators))}"