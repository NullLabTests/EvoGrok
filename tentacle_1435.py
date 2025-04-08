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
        
        # Extract class attributes
        class_attributes = re.findall(r'class="([^"]*)"', input_data, re.IGNORECASE)
        all_classes = set()
        for classes in class_attributes:
            all_classes.update(classes.split())
        
        # Return a formatted string with document analysis
        return f"HTML document ({document_type}): {word_count} unique words - {','.join(sorted(words))}. Relevant keywords: {','.join(sorted(relevant_keywords))}. Relevance score: {relevance_score:.2f}%. Class attributes: {','.join(sorted(all_classes))}"
    
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
                'Inverse': 1 / result if result != 0 else 'undefined'
            }
            return f"{result_str} (number) - Calculations: {', '.join(f'{k}: {v}' for k, v in calculations.items())}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            word_frequency = Counter(words)
            most_common_word = word_frequency.most_common(1)[0][0] if words else ''
            most_common_count = word_frequency[most_common_word] if words else 0
            return f"String result: {total_words} words, {unique_words} unique - {','.join(sorted(words))}. Most common word: '{most_common_word}' (appears {most_common_count} times)"
        
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
        word_frequency = Counter(words)
        most_common_word = word_frequency.most_common(1)[0][0] if words else ''
        most_common_count = word_frequency[most_common_word] if words else 0
        
        # Check for potential HTML-like content
        html_like = input_data.strip().lower().startswith('<') and input_data.strip().lower().endswith('>')
        
        # Check for potential URL
        url_pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
        is_url = bool(url_pattern.match(input_data))
        
        # Return a formatted string with text analysis
        return f"Text input: {total_words} words, {unique_words} unique - {','.join(sorted(words))}. Most common word: '{most_common_word}' (appears {most_common_count} times). Detected operators: {','.join(sorted(detected_operators))}. HTML-like content: {html_like}. Potential URL: {is_url}. Error during evaluation: {str(e)}"