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
        total_length = sum(len(word) for word in words)
        avg_word_length = total_length / word_count if word_count > 0 else 0
        
        # Count the number of digits in the HTML content
        digit_count = sum(c.isdigit() for c in input_data)
        
        # Count the number of tags in the HTML content
        tag_count = len([c for c in input_data if c == '<'])
        
        # Calculate the ratio of digits to total characters
        digit_ratio = digit_count / len(input_data) if len(input_data) > 0 else 0
        
        # Count the number of classes in the HTML content
        class_count = len([word for word in words if word.startswith('class=')])
        
        # Count the number of links in the HTML content
        link_count = input_data.lower().count('href=')
        
        # Return a formatted string with detailed HTML document analysis
        return (f"HTML document ({document_type}): {word_count} unique words, "
                f"avg length {avg_word_length:.2f}, {digit_count} digits, "
                f"{tag_count} tags, {class_count} classes, {link_count} links, "
                f"digit ratio {digit_ratio:.4f} - "
                f"{','.join(sorted(words))}").lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and some basic statistics
        if result_str.replace('.', '').replace('-', '').isdigit():
            number = float(result_str)
            return (f"{number} (number): min={min(number, 0)}, max={max(number, 0)}, "
                    f"abs={abs(number)}, square={number**2}, "
                    f"cube={number**3}, factorial={1 if number==0 else number*eval(input_data.replace('*', '*1').replace('/', '/1'))}, "
                    f"is_integer={number.is_integer()}").lower()
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
            digit_count = sum(c.isdigit() for c in result_str)
            digit_ratio = digit_count / len(result_str) if len(result_str) > 0 else 0
            return (f"string result from math eval: {total_words} words, "
                    f"{unique_words} unique, avg length {avg_word_length:.2f}, "
                    f"{digit_count} digits, digit ratio {digit_ratio:.4f} - "
                    f"{','.join(sorted(words))}").lower()
        
        # For other types of results, return the type, value, and a string representation
        return f"{type(result).__name__} result from math eval: {result} - {str(result)}".lower()
    
    except:
        # If evaluation fails, process the input as text
        input_str = str(input_data).lower()
        words = input_str.split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Calculate the average word length
        total_length = sum(len(word) for word in words)
        avg_word_length = total_length / total_words if total_words > 0 else 0
        
        # Count the number of digits in the input
        digit_count = sum(c.isdigit() for c in input_str)
        
        # Calculate the ratio of digits to total characters
        digit_ratio = digit_count / len(input_str) if len(input_str) > 0 else 0
        
        # Count the number of punctuation marks
        punctuation_count = sum(c in '.,!?;:' for c in input_str)
        
        # Count the number of uppercase letters (if any)
        uppercase_count = sum(1 for c in input_str if c.isupper())
        
        # Return a formatted string with detailed text analysis
        return (f"text input: {total_words} words, {unique_words} unique, "
                f"avg length {avg_word_length:.2f}, {digit_count} digits, "
                f"digit ratio {digit_ratio:.4f}, {punctuation_count} punctuation marks, "
                f"{uppercase_count} uppercase letters - "
                f"{','.join(sorted(words))}").lower()