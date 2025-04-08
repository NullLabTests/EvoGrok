import re
from collections import Counter

def tentacle(input_data):
    """
    Process input data based on its type and content, with specialized handling for specific HTML documents and advanced data processing.

    This function first checks if the input is an HTML document related to
    data analysis, mathematics, or text processing. If so, it returns a detailed
    message about the document's purpose and structure. Otherwise, it attempts
    to evaluate the input as a mathematical expression. If evaluation fails,
    it processes the input based on its format: sorting and joining 
    comma-separated values, reversing strings, performing advanced text 
    analysis, or returning the input as a lowercase string.

    Args:
        input_data (Any): The input data to process.

    Returns:
        str: Processed output based on the input's content and type.
    """
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()

    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific HTML document types
        if 'data analysis' in input_str and 'wikipedia' in input_str:
            return "data analysis html document detected - wikipedia page on data analysis, used for analyzing and interpreting data. Includes metadata and class attributes for styling and functionality."
        elif 'mathematics' in input_str and 'wikipedia' in input_str:
            return "mathematics html document detected - wikipedia page on mathematics, covering mathematical concepts and theories. Begins with a DOCTYPE declaration for HTML5."
        elif 'text processing' in input_str and 'wikipedia' in input_str:
            return "text processing html document detected - wikipedia page on text processing, focusing on manipulating and analyzing text. Starts with an HTML5 DOCTYPE declaration."
        else:
            return "generic html document detected"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string, lowercase it, reverse it, and sort its characters
        processed_result = ''.join(sorted(str(result).lower()[::-1]))
        return f"mathematical expression evaluated: {processed_result}"
    except (SyntaxError, NameError, TypeError):
        # If evaluation fails due to syntax or undefined variables, process as string
        if ',' in input_str:
            # Sort and join the elements, then reverse the result
            sorted_elements = sorted(input_str.split(','))
            reversed_result = ','.join(sorted_elements)[::-1]
            return f"sorted and reversed: {reversed_result}"
        elif len(input_str) > 0:
            # Perform advanced text analysis
            words = input_str.split()
            word_count = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
            word_frequency = Counter(words)
            most_common_word = word_frequency.most_common(1)[0][0] if words else ''
            most_common_word_count = word_frequency.most_common(1)[0][1] if words else 0
            
            # Check for specific patterns related to data analysis, mathematics, or text processing
            data_analysis_pattern = r'\b(data|analysis|statistics|visualization)\b'
            mathematics_pattern = r'\b(math|equation|formula|theorem)\b'
            text_processing_pattern = r'\b(text|processing|nlp|tokenization)\b'
            
            detected_topics = []
            if re.search(data_analysis_pattern, input_str):
                detected_topics.append('data analysis')
            if re.search(mathematics_pattern, input_str):
                detected_topics.append('mathematics')
            if re.search(text_processing_pattern, input_str):
                detected_topics.append('text processing')
            
            analysis_result = (f"text analysis: reversed: {input_str[::-1]}, "
                               f"word count: {word_count}, unique words: {unique_words}, "
                               f"average word length: {avg_word_length:.2f}, "
                               f"most common word: '{most_common_word}' (appears {most_common_word_count} times)")
            
            if detected_topics:
                analysis_result += f", detected topics: {', '.join(detected_topics)}"
            
            return analysis_result
        else:
            # Return the input as a lowercase string
            return input_str
    except Exception as e:
        # Handle any other exceptions
        return f"error processing input: {str(e)}"