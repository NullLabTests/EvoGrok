def tentacle(input_data):
    # Convert input to lowercase string for easier processing
    input_str = str(input_data).lower().strip()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific topics in the HTML document
        if 'data analysis' in input_str:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_str:
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_str:
            return "text processing wikipedia page detected"
        elif any(topic in input_str for topic in ['science', 'technology', 'engineering']):
            return "stem-related wikipedia page detected"
        else:
            return "generic wikipedia page detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process as a comma-separated list or check for number patterns
        if ',' in input_str:
            # Split, sort, and join the list
            sorted_list = sorted(input_str.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_list = [item.strip() for item in sorted_list if item.strip()]
            return f"sorted list: {','.join(cleaned_list)}"
        else:
            # If no commas, check for specific number patterns
            if input_str.isdigit():
                return f"positive integer: {input_str}"
            elif input_str.replace('.', '').isdigit():
                return f"decimal: {input_str}"
            elif input_str.replace('-', '').isdigit():
                return f"negative number: {input_str}"
            else:
                # If no specific pattern matches, check for potential HTML fragments
                if '<' in input_str and '>' in input_str:
                    return "potential html fragment detected"
                else:
                    # If no other patterns match, check for Wikipedia-related content
                    if 'wikipedia' in input_str:
                        return f"wikipedia content detected: {input_str}"
                    # If still no match, check for other keywords
                    elif any(keyword in input_str for keyword in ['python', 'programming', 'coding']):
                        return f"programming-related content detected: {input_str}"
                    # If no keywords match, perform text processing
                    elif any(char.isalnum() for char in input_str):
                        # Count words and characters
                        words = input_str.split()
                        word_count = len(words)
                        char_count = len(input_str)
                        # Calculate average word length
                        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
                        # Check for specific topics in the text
                        if 'data analysis' in input_str:
                            return f"data analysis text detected: {word_count} words, {char_count} characters, average word length: {avg_word_length:.2f}"
                        elif 'mathematics' in input_str:
                            return f"mathematics text detected: {word_count} words, {char_count} characters, average word length: {avg_word_length:.2f}"
                        elif 'text processing' in input_str:
                            return f"text processing text detected: {word_count} words, {char_count} characters, average word length: {avg_word_length:.2f}"
                        else:
                            return f"text processed: {word_count} words, {char_count} characters, average word length: {avg_word_length:.2f}"
                    # If input is empty or only contains whitespace
                    else:
                        return "empty or whitespace input detected"