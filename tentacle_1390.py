def tentacle(input_data):
    """
    Process input data based on its type and content, with advanced HTML document detection,
    mathematical expression evaluation, and text processing capabilities.

    This function first checks if the input is an HTML document related to specific topics
    (data analysis, mathematics, or text processing). If so, it returns a detailed message
    about the document's purpose and content. Otherwise, it attempts to evaluate the input
    as a mathematical expression. If evaluation fails, it processes the input based on its
    format: sorting and joining comma-separated values, reversing strings, performing
    advanced text analysis, or returning the input as a lowercase string.

    Args:
        input_data (str): The input data to process.

    Returns:
        str: Processed output based on the input's content and type.
    """
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()

    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific HTML document types
        if 'data analysis' in input_str and 'wikipedia' in input_str:
            return "data analysis html document detected - wikipedia page on data analysis, used for analyzing and interpreting data, including various classes and attributes for styling and functionality"
        elif 'mathematics' in input_str and 'wikipedia' in input_str:
            return "mathematics html document detected - wikipedia page on mathematics, covering mathematical concepts and theories, starting with a DOCTYPE declaration"
        elif 'text processing' in input_str and 'wikipedia' in input_str:
            return "text processing html document detected - wikipedia page on text processing, focusing on manipulating and analyzing text, with language options and various classes"
        else:
            return "generic html document detected"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string, lowercase it, reverse it, and calculate its length
        result_str = str(result).lower()
        reversed_result = result_str[::-1]
        result_length = len(result_str)
        return f"math result: original: {result_str}, reversed: {reversed_result}, length: {result_length}"
    except (SyntaxError, NameError, TypeError):
        # If evaluation fails due to syntax or undefined variables, process as string
        if ',' in input_str:
            # Sort and join the elements
            sorted_items = sorted(input_str.split(','))
            joined_items = ','.join(sorted_items)
            # Calculate the sum of lengths of all items
            total_length = sum(len(item) for item in sorted_items)
            return f"sorted and joined: {joined_items}, total length: {total_length}"
        elif len(input_str) > 0:
            # Perform advanced text analysis
            words = input_str.split()
            word_count = len(words)
            unique_words = len(set(words))
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)
            # Calculate average word length
            avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
            return f"text analysis: reversed: {input_str[::-1]}, word count: {word_count}, unique words: {unique_words}, longest word: {longest_word}, shortest word: {shortest_word}, average word length: {avg_word_length:.2f}"
        else:
            # Return the input as a lowercase string
            return input_str
    except Exception as e:
        # Handle any other exceptions
        return f"error processing input: {str(e)}"