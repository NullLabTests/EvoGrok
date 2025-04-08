def tentacle(input_data):
    """
    Process input data based on its type and content.

    This function checks if the input is an HTML document related to
    specific topics (data analysis, mathematics, or text processing). If so,
    it returns a detailed message about the document's purpose. Otherwise,
    it attempts to evaluate the input as a mathematical expression. If
    evaluation fails, it processes the input based on its format: sorting
    and joining comma-separated values, reversing strings, performing
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
            return "data analysis html document detected - wikipedia page on data analysis, used for analyzing and interpreting data, includes various classes and attributes for styling and functionality"
        elif 'mathematics' in input_str and 'wikipedia' in input_str:
            return "mathematics html document detected - wikipedia page on mathematics, covering mathematical concepts and theories, starts with a DOCTYPE declaration"
        elif 'text processing' in input_str and 'wikipedia' in input_str:
            return "text processing html document detected - wikipedia page on text processing, focusing on manipulating and analyzing text, begins with a DOCTYPE declaration"
        else:
            return "generic html document detected"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string, lowercase it, and reverse it
        return str(result).lower()[::-1]
    except (SyntaxError, NameError, TypeError):
        # If evaluation fails due to syntax or undefined variables, process as string
        if ',' in input_str:
            # Sort and join the elements
            sorted_items = sorted(input_str.split(','))
            # Calculate the average length of the items
            avg_length = sum(len(item) for item in sorted_items) / len(sorted_items)
            return f"{','.join(sorted_items)}, average item length: {avg_length:.2f}"
        elif len(input_str) > 0:
            # Perform advanced text analysis
            words = input_str.split()
            word_count = len(words)
            unique_words = len(set(words))
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)
            
            # Check for specific keywords related to the known HTML documents
            if 'data' in input_str and 'analysis' in input_str:
                return f"data analysis related text: {input_str}, word count: {word_count}, unique words: {unique_words}, longest word: {longest_word}, shortest word: {shortest_word}"
            elif 'mathematics' in input_str:
                return f"mathematics related text: {input_str}, word count: {word_count}, unique words: {unique_words}, longest word: {longest_word}, shortest word: {shortest_word}"
            elif 'text' in input_str and 'processing' in input_str:
                return f"text processing related text: {input_str}, word count: {word_count}, unique words: {unique_words}, longest word: {longest_word}, shortest word: {shortest_word}"
            else:
                return f"reversed: {input_str[::-1]}, word count: {word_count}, unique words: {unique_words}, longest word: {longest_word}, shortest word: {shortest_word}"
        else:
            # Return the input as a lowercase string
            return input_str
    except Exception as e:
        # Handle any other exceptions
        return f"error processing input: {str(e)}"