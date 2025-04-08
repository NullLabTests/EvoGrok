def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known titles
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
            'data analysis': ['statistics', 'visualization', 'modeling', 'data', 'analysis'],
            'mathematics': ['algebra', 'geometry', 'calculus', 'equation', 'theorem'],
            'text processing': ['nlp', 'tokenization', 'stemming', 'text', 'processing']
        }
        relevant_keywords = set()
        for keyword in related_keywords.get(document_type, []):
            if keyword in words:
                relevant_keywords.add(keyword)
        
        # Calculate the relevance score based on the number of relevant keywords
        relevance_score = len(relevant_keywords) / len(related_keywords.get(document_type, [])) * 100 if related_keywords.get(document_type, []) else 0
        
        # Return a formatted string with document type, word count, sorted words, relevant keywords, and relevance score
        return f"HTML document ({document_type}): {word_count} unique words - {','.join(sorted(words))}. Relevant keywords: {','.join(sorted(relevant_keywords))}. Relevance score: {relevance_score:.2f}%"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and various calculations
        if result_str.replace('.', '').replace('-', '').isdigit():
            calculations = {
                'Double': result * 2,
                'Square': result ** 2,
                'Square Root': result ** 0.5 if result >= 0 else 'undefined',
                'Cube': result ** 3,
                'Logarithm': math.log(result) if result > 0 else 'undefined'
            }
            return f"{result_str} (number) - Calculations: {', '.join(f'{k}: {v:.2f}' for k, v in calculations.items() if v != 'undefined')}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            word_frequency = {word: words.count(word) for word in set(words)}
            most_common_word = max(word_frequency, key=word_frequency.get) if words else ''
            return f"String result: {total_words} words, {unique_words} unique - {','.join(sorted(words))}. Most common word: '{most_common_word}' (appears {word_frequency.get(most_common_word, 0)} times)"
        
        # For other types of results, return the type, value, and a detailed representation
        return f"{type(result).__name__} result: {result_str} - Detailed repr: {repr(result)}. Attributes: {', '.join(dir(result))}"
    
    except Exception as e:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Check for mathematical operators
        operators = set(['+', '-', '*', '/', '**', '%', '=', '<', '>', '!', '&', '|'])
        detected_operators = operators.intersection(set(input_data))
        
        # Calculate word frequency
        word_frequency = {word: words.count(word) for word in set(words)}
        most_common_word = max(word_frequency, key=word_frequency.get) if words else ''
        
        # Check for potential HTML structure
        html_structure = 'html' in words or 'doctype' in words
        
        # Return a formatted string with word counts, sorted words, detected operators, and word frequency information
        return f"Text input: {total_words} words, {unique_words} unique - {','.join(sorted(words))}. Most common word: '{most_common_word}' (appears {word_frequency.get(most_common_word, 0)} times). Detected operators: {','.join(sorted(detected_operators))}. Potential HTML structure detected: {html_structure}. Error during evaluation: {str(e)}"