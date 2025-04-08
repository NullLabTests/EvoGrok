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
        
        # Calculate the most common word length
        word_lengths = [len(word) for word in words]
        most_common_length = max(set(word_lengths), key=word_lengths.count) if word_lengths else 0
        
        # Calculate the percentage of words starting with a vowel
        vowels = 'aeiou'
        vowel_start_count = sum(1 for word in words if word and word[0] in vowels)
        vowel_start_percentage = (vowel_start_count / word_count) * 100 if word_count > 0 else 0
        
        # Return a formatted string with detailed HTML document information
        return (f"HTML document ({document_type}): {word_count} unique words, "
                f"avg length {avg_word_length:.2f}, most common length {most_common_length}, "
                f"{vowel_start_percentage:.2f}% words start with vowel - {','.join(sorted(words))}")
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and various calculations
        if result_str.replace('.', '').isdigit():
            calculation_double = result * 2
            calculation_square = result ** 2
            calculation_sqrt = result ** 0.5 if result >= 0 else "undefined"
            return (f"{result_str} (number): type={type(result).__name__}, "
                    f"doubled={calculation_double:.2f}, squared={calculation_square:.2f}, "
                    f"square root={calculation_sqrt:.2f}")
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
            return (f"String result: {total_words} words, {unique_words} unique, "
                    f"avg length {avg_word_length:.2f} - {','.join(sorted(words))}")
        
        # For other types of results, return the type, value, and a detailed representation
        return (f"{type(result).__name__} result: value={result_str}, "
                f"repr={repr(result)}, dir={','.join(dir(result))}")
    
    except:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Calculate the average word length
        avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
        
        # Calculate the most common word length
        word_lengths = [len(word) for word in words]
        most_common_length = max(set(word_lengths), key=word_lengths.count) if word_lengths else 0
        
        # Calculate the percentage of words starting with a vowel
        vowels = 'aeiou'
        vowel_start_count = sum(1 for word in words if word and word[0] in vowels)
        vowel_start_percentage = (vowel_start_count / total_words) * 100 if total_words > 0 else 0
        
        # Return a formatted string with detailed text input information
        return (f"Text input: {total_words} words, {unique_words} unique, "
                f"avg length {avg_word_length:.2f}, most common length {most_common_length}, "
                f"{vowel_start_percentage:.2f}% words start with vowel - {','.join(sorted(words))}")