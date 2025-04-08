import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on knowledge
        document_type = 'unknown'
        for known_type, known_content in {
            'data analysis': 'data analysis',
            'mathematics': 'mathematics',
            'text processing': 'text processing'
        }.items():
            if known_content in input_data.lower():
                document_type = known_type
                break
        
        # Extract and process words from the HTML content
        words = set(re.findall(r'\b\w+\b', input_data.lower()))
        words.discard('<!doctype')
        words.discard('html')
        
        # Count the number of unique words
        word_count = len(words)
        
        # Calculate the average word length
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        
        # Calculate the percentage of words related to the document type and other topics
        topics = {
            'data analysis': {'data', 'analysis', 'statistics', 'information'},
            'mathematics': {'math', 'equation', 'formula', 'number'},
            'text processing': {'text', 'processing', 'nlp', 'language'}
        }
        topic_percentages = {}
        for topic, topic_words in topics.items():
            related_count = len(words.intersection(topic_words))
            topic_percentages[topic] = (related_count / word_count) * 100 if word_count > 0 else 0
        
        # Sort topic percentages in descending order
        sorted_topics = sorted(topic_percentages.items(), key=lambda x: x[1], reverse=True)
        
        # Create a string of top 3 relevant topics
        top_topics = ', '.join(f"{topic}: {percentage:.2f}%" for topic, percentage in sorted_topics[:3] if percentage > 0)
        
        # Return a formatted string with document type, word count, average word length, top topics, and sorted words
        return f"html document ({document_type}): {word_count} unique words, avg length {avg_word_length:.2f}, top topics - {top_topics} - {','.join(sorted(words))}"
    
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
            factorial = 1
            for i in range(1, int(result) + 1):
                factorial *= i
            return f"{result_str} (number): doubled={doubled:.2f}, squared={squared:.2f}, cubed={cubed:.2f}, factorial={factorial}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
            
            # Calculate the percentage of words related to common topics
            common_topics = {'data': {'data', 'analysis', 'statistics', 'information'},
                             'math': {'math', 'equation', 'formula', 'number'},
                             'text': {'text', 'processing', 'nlp', 'language'}}
            topic_percentages = {}
            for topic, topic_words in common_topics.items():
                topic_count = len(set(words).intersection(topic_words))
                topic_percentages[topic] = (topic_count / total_words) * 100 if total_words > 0 else 0
            
            # Sort topic percentages in descending order
            sorted_topics = sorted(topic_percentages.items(), key=lambda x: x[1], reverse=True)
            
            # Create a string of top 3 relevant topics
            top_topics = ', '.join(f"{topic}: {percentage:.2f}%" for topic, percentage in sorted_topics[:3] if percentage > 0)
            
            return f"string result: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f}, top topics - {top_topics} - {','.join(sorted(words))}"
        
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
        
        # Sort topic percentages in descending order
        sorted_topics = sorted(topic_percentages.items(), key=lambda x: x[1], reverse=True)
        
        # Create a string of top 3 relevant topics
        top_topics = ', '.join(f"{topic}: {percentage:.2f}%" for topic, percentage in sorted_topics[:3] if percentage > 0)
        
        # Return a formatted string with word counts, average word length, top topics, and sorted words
        return f"text input: {total_words} words, {unique_words} unique, avg length {avg_word_length:.2f}, top topics - {top_topics} - {','.join(sorted(words))}"