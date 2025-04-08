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
            # Calculate the total word count
            total_words = sum(word_counts.values())
            # Calculate the percentage of each word
            word_percentages = {word: (count / total_words) * 100 for word, count in word_counts.items()}
            # Sort the words by percentage (descending) and then alphabetically
            sorted_percentages = sorted(word_percentages.items(), key=lambda x: (-x[1], x[0]))
            # Return the document type, top 5 words with their counts, and top 5 words with their percentages
            word_freq = ','.join(f"{word}:{count}" for word, count in sorted_words[:5])
            word_percent = ','.join(f"{word}:{percentage:.2f}%" for word, percentage in sorted_percentages[:5])
            return f"{doc_type} detected: {word_freq} | word percentages: {word_percent}"
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
        # Calculate the total word count
        total_words = sum(word_counts.values())
        # Calculate the percentage of each word
        word_percentages = {word: (count / total_words) * 100 for word, count in word_counts.items()}
        # Sort the words by percentage (descending) and then alphabetically
        sorted_percentages = sorted(word_percentages.items(), key=lambda x: (-x[1], x[0]))
        # Return the result, top 5 words with their counts, and top 5 words with their percentages
        word_freq = ','.join(f"{word}:{count}" for word, count in sorted_words[:5])
        word_percent = ','.join(f"{word}:{percentage:.2f}%" for word, percentage in sorted_percentages[:5])
        return f"math expression evaluated: {result} | word frequencies: {word_freq} | word percentages: {word_percent}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove empty strings, sort, and join
        words = [word for word in str(input_data).lower().split() if word]
        # Count the occurrences of each word
        word_counts = {word: words.count(word) for word in set(words)}
        # Sort the words by count (descending) and then alphabetically
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        # Calculate the total word count
        total_words = sum(word_counts.values())
        # Calculate the percentage of each word
        word_percentages = {word: (count / total_words) * 100 for word, count in word_counts.items()}
        # Sort the words by percentage (descending) and then alphabetically
        sorted_percentages = sorted(word_percentages.items(), key=lambda x: (-x[1], x[0]))
        # Return the top 5 words with their counts and percentages
        word_freq = ','.join(f"{word}:{count}" for word, count in sorted_words[:5])
        word_percent = ','.join(f"{word}:{percentage:.2f}%" for word, percentage in sorted_percentages[:5])
        return f"text processed: {word_freq} | word percentages: {word_percent}"