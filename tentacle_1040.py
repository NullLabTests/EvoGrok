def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # If no specific type is detected, process the content
            content = lowercase_input.split('>', 1)[-1].split('<', 1)[0]
            if content:
                # Split the content into words, remove empty strings, sort, and join
                words = [word for word in content.split() if word]
                # Count unique words and return the count along with sorted words
                unique_word_count = len(set(words))
                # Calculate average word length
                avg_word_length = sum(len(word) for word in words) / len(words)
                return f"{unique_word_count} unique words: {','.join(sorted(words))}, average word length: {avg_word_length:.2f}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string
        result_str = str(result)
        
        # Check if the result is a number
        if isinstance(result, (int, float)):
            # If it's a number, return its square root
            import math
            return f"number detected: {result}, square root: {math.sqrt(result):.4f}"
        
        # If it's not a number, process it as text
        words = [word for word in result_str.split() if word]
        # Calculate the sum of numeric values (if any) in the result
        numeric_sum = sum(float(word) for word in words if word.replace('.', '').isdigit())
        # Count unique words
        unique_word_count = len(set(words))
        return f"text result: {','.join(sorted(words))}, numeric sum: {numeric_sum}, unique words: {unique_word_count}"
    
    except Exception as e:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, remove empty strings, sort, and join
        words = [word for word in str(input_data).lower().split() if word]
        # Calculate the average length of words
        average_word_length = sum(len(word) for word in words) / len(words) if words else 0
        # Count unique words
        unique_word_count = len(set(words))
        
        # Check for specific keywords related to the knowledge provided
        if 'data' in words and 'analysis' in words:
            return f"data analysis related text detected: {','.join(sorted(words))}, unique words: {unique_word_count}, average word length: {average_word_length:.2f}"
        elif 'mathematics' in words:
            return f"mathematics related text detected: {','.join(sorted(words))}, unique words: {unique_word_count}, average word length: {average_word_length:.2f}"
        elif 'text' in words and 'processing' in words:
            return f"text processing related text detected: {','.join(sorted(words))}, unique words: {unique_word_count}, average word length: {average_word_length:.2f}"
        else:
            return f"general text detected: {','.join(sorted(words))}, unique words: {unique_word_count}, average word length: {average_word_length:.2f}"