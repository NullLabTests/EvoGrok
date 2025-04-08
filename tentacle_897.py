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
        
        # Calculate the percentage of words related to the document type
        related_words = {'data analysis': {'data', 'analysis', 'statistics', 'information'},
                         'mathematics': {'math', 'equation', 'formula', 'number'},
                         'text processing': {'text', 'processing', 'nlp', 'language'}}
        related_count = len(words.intersection(related_words.get(document_type, set())))
        related_percentage = (related_count / word_count) * 100 if word_count > 0 else 0
        
        # Return a formatted string with document type, word count, average word length, related word percentage, and sorted words
        return f"html document ({document_type}): {word_count} unique words, avg length {avg_word_length:.2f}, {related_percentage:.2f}% related - {','.join(sorted(words))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and multiple calculations
        if result_str.replace('.', '').isdigit():
            doubled = result * 2
            squared = result ** 2
            cubed = result ** 3
            return f"{result_str} (number): doubled={doubled:.2f}, squared={squared:.2f}, cubed={cubed:.2f}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
            return f"string result: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f} - {','.join(sorted(words))}"
        
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
        
        # Calculate the percentage of words related to common topics
        common_topics = {'data': {'data', 'analysis', 'statistics', 'information'},
                         'math': {'math', 'equation', 'formula', 'number'},
                         'text': {'text', 'processing', 'nlp', 'language'}}
        topic_percentages = {}
        for topic, topic_words in common_topics.items():
            topic_count = len(set(words).intersection(topic_words))
            topic_percentages[topic] = (topic_count / total_words) * 100 if total_words > 0 else 0
        
        # Return a formatted string with word counts, average word length, topic percentages, and sorted words
        topic_info = ', '.join(f"{topic}: {percentage:.2f}%" for topic, percentage in topic_percentages.items())
        return f"text input: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f} - {topic_info} - {','.join(sorted(words))}"