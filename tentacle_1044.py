def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            doc_type = "data analysis html document"
        elif 'mathematics' in lowercase_input:
            doc_type = "mathematics html document"
        elif 'text processing' in lowercase_input:
            doc_type = "text processing html document"
        else:
            doc_type = "generic html document"
        
        # Extract and process the content
        content = lowercase_input.split('>', 1)[-1].split('<', 1)[0]
        if content:
            # Split the content into words, remove empty strings, sort, and join
            words = [word for word in content.split() if word]
            # Count the occurrences of each word
            word_counts = {word: words.count(word) for word in set(words)}
            # Sort the words by count (descending) and then alphabetically
            sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            # Return the document type and top 5 words with their counts
            word_freq = ','.join(f"{word}:{count}" for word, count in sorted_words[:5])
            return f"{doc_type} detected: {word_freq}"
        else:
            return f"{doc_type} detected: no content found"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, remove empty strings, sort, and join
        words = [word for word in str(result).split() if word]
        # Count the occurrences of each word
        word_counts = {word: words.count(word) for word in set(words)}
        # Sort the words by count (descending) and then alphabetically
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        # Return the top 5 words with their counts
        return f"math expression evaluated: {','.join(f'{word}:{count}' for word, count in sorted_words[:5])}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove empty strings, sort, and join
        words = [word for word in str(input_data).lower().split() if word]
        # Count the occurrences of each word
        word_counts = {word: words.count(word) for word in set(words)}
        # Sort the words by count (descending) and then alphabetically
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        # Return the top 5 words with their counts
        return f"text processed: {','.join(f'{word}:{count}' for word, count in sorted_words[:5])}"