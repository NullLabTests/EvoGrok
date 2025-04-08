import re
from collections import Counter

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        document_type = 'unknown'
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        
        # Extract and process words from the HTML content
        words = set(re.findall(r'\b\w+\b', input_data.lower()))
        words.discard('doctype')
        words.discard('html')
        
        # Count the number of unique words
        word_count = len(words)
        
        # Check for specific keywords related to the document type
        related_keywords = {
            'data analysis': ['statistics', 'visualization', 'modeling', 'data'],
            'mathematics': ['algebra', 'geometry', 'calculus', 'equation'],
            'text processing': ['nlp', 'tokenization', 'stemming', 'text'],
            'unknown': ['generic', 'html', 'web']
        }
        relevant_keywords = set()
        for keyword in related_keywords.get(document_type, []):
            if keyword in words:
                relevant_keywords.add(keyword)
        
        # Calculate the percentage of relevant keywords
        relevant_keyword_percentage = (len(relevant_keywords) / len(related_keywords.get(document_type, []))) * 100 if related_keywords.get(document_type, []) else 0
        
        # Extract class attributes from the HTML
        classes = set(re.findall(r'class="([^"]*)"', input_data.lower()))
        
        # Return a formatted string with document type, word count, sorted words, relevant keywords, their percentage, and class attributes
        return f"HTML document ({document_type}): {word_count} unique words - {','.join(sorted(words))}. Relevant keywords ({relevant_keyword_percentage:.2f}%): {','.join(sorted(relevant_keywords))}. Classes: {','.join(sorted(classes))}"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and multiple calculations
        if result_str.replace('.', '').replace('-', '').isdigit():
            calculations = {
                'Double': result * 2,
                'Square': result ** 2,
                'Square Root': result ** 0.5 if result >= 0 else 'undefined',
                'Cube': result ** 3,
                'Absolute Value': abs(result)
            }
            return f"{result_str} (number) - Calculations: {', '.join(f'{key}: {value}' for key, value in calculations.items())}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            word_frequency = Counter(words)
            most_common_word = word_frequency.most_common(1)[0][0] if words else ''
            return f"String result: {total_words} words, {unique_words} unique - Most common word: '{most_common_word}' ({word_frequency[most_common_word]} occurrences) - {','.join(sorted(words))}"

        # For other types of results, return the type, value, and a detailed representation
        return f"{type(result).__name__} result: {result_str} - Detailed repr: {repr(result)} - Length: {len(repr(result))}"

    except Exception as e:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Check for mathematical operators
        operators = set(['+', '-', '*', '/', '**', '%', '=', '<', '>', '<=', '>='])
        detected_operators = operators.intersection(set(input_data))
        
        # Calculate word frequency
        word_frequency = Counter(words)
        most_common_word = word_frequency.most_common(1)[0][0] if words else ''
        
        # Check for potential HTML tags
        html_tags = set(re.findall(r'<[^>]+>', input_data.lower()))
        
        # Return a formatted string with word counts, sorted words, detected operators, word frequency information, and potential HTML tags
        return f"Text input: {total_words} words, {unique_words} unique - Most common word: '{most_common_word}' ({word_frequency[most_common_word]} occurrences) - {','.join(sorted(words))}. Detected operators: {','.join(sorted(detected_operators))}. Potential HTML tags: {','.join(sorted(html_tags))}"