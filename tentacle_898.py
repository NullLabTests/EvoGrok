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
        
        # Process specific document types
        if document_type == 'data analysis':
            # Check for class attributes related to data analysis
            if 'class="data-analysis"' in input_data.lower():
                return f"data analysis html document: {word_count} unique words - {','.join(sorted(words))}"
            
            # Check for Wikipedia-specific patterns
            if 'wikipedia' in input_data.lower():
                return f"data analysis wikipedia page: {word_count} unique words - {','.join(sorted(words))}"
        
        elif document_type == 'mathematics':
            # Check for HTML5 declaration
            if '<!doctype html>' in input_data.lower():
                return f"mathematics html5 document: {word_count} unique words - {','.join(sorted(words))}"
            
            # Check for Wikipedia-specific patterns
            if 'wikipedia' in input_data.lower():
                return f"mathematics wikipedia page: {word_count} unique words - {','.join(sorted(words))}"
        
        elif document_type == 'text processing':
            # Check for styling and functionality attributes
            if 'class="text-processing"' in input_data.lower():
                return f"text processing html document: {word_count} unique words - {','.join(sorted(words))}"
            
            # Check for Wikipedia-specific patterns
            if 'wikipedia' in input_data.lower():
                return f"text processing wikipedia page: {word_count} unique words - {','.join(sorted(words))}"
        
        # Return a generic HTML document result
        return f"html document ({document_type}): {word_count} unique words - {','.join(sorted(words))}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result)
        
        # If the result is a number, return it with its type and perform calculations
        if result_str.replace('.', '').isdigit():
            calculation = result * 2
            square_root = result ** 0.5
            return f"{result_str} (number): doubled value = {calculation}, square root = {square_root}"
        
        # If the result is a string, process it like text
        if isinstance(result, str):
            words = result_str.lower().split()
            total_words = len(words)
            unique_words = len(set(words))
            
            # Check for specific patterns in the text
            if 'data' in words and 'analysis' in words:
                return f"data analysis string: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
            elif 'mathematics' in words:
                return f"mathematics string: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
            elif 'text' in words and 'processing' in words:
                return f"text processing string: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
            
            # Return a generic string result
            return f"string result: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        
        # For other types of results, return the type and value, and attempt to convert to string
        try:
            string_value = str(result)
            return f"{type(result).__name__} result: {string_value}"
        except:
            return f"{type(result).__name__} result: unable to convert to string"
    
    except:
        # If evaluation fails, process the input as text
        words = str(input_data).lower().split()
        
        # Count the number of words and unique words
        total_words = len(words)
        unique_words = len(set(words))
        
        # Check for specific patterns in the text
        if 'data' in words and 'analysis' in words:
            return f"data analysis text: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        elif 'mathematics' in words:
            return f"mathematics text: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        elif 'text' in words and 'processing' in words:
            return f"text processing text: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        
        # Check for potential mathematical expressions
        if any(char in '+-*/^()' for char in input_data):
            return f"potential math expression: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"
        
        # Return a generic text input result
        return f"text input: {total_words} words, {unique_words} unique - {','.join(sorted(words))}"