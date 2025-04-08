def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on content
        document_type = 'unknown'
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        elif 'wikipedia' in input_data.lower():
            document_type = 'wikipedia'
        
        # Extract and process words from the HTML content
        words = set(input_data.lower().split())
        words.discard('<!doctype')
        words.discard('html')
        
        # Count the number of unique words in the document
        word_count = len(words)
        
        # Calculate the average length of words
        avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
        
        # Calculate the sum of numeric values in the text
        numeric_value_sum = sum(float(word) for word in words if word.replace('.', '').isdigit())
        
        # Attempt to evaluate any numeric expressions found in the text
        numeric_sum = 0
        for word in words:
            try:
                numeric_sum += eval(word)
            except:
                pass
        
        # Check for specific content based on document type
        if document_type == 'data analysis':
            data_analysis_score = sum(1 for word in words if word in ['statistics', 'visualization', 'modeling', 'regression'])
        elif document_type == 'mathematics':
            math_score = sum(1 for word in words if word in ['equation', 'theorem', 'proof', 'variable'])
        elif document_type == 'text processing':
            text_processing_score = sum(1 for word in words if word in ['tokenization', 'stemming', 'lemmatization', 'parsing'])
        else:
            general_score = sum(1 for word in words if word in ['information', 'knowledge', 'content', 'article'])
        
        # Return a sorted, comma-separated list of detected elements
        result = ['html document', document_type, f'word count: {word_count}', f'average word length: {avg_word_length:.2f}']
        
        if document_type == 'data analysis':
            result.append(f'data analysis score: {data_analysis_score}')
        elif document_type == 'mathematics':
            result.append(f'mathematics score: {math_score}')
        elif document_type == 'text processing':
            result.append(f'text processing score: {text_processing_score}')
        else:
            result.append(f'general score: {general_score}')
        
        result.extend([f'numeric sum: {numeric_sum}', f'numeric value sum: {numeric_value_sum:.2f}'])
        result.extend(sorted(words))
        
        return ','.join(result)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words
        result_words = str(result).lower().split()
        
        # Calculate the sum of numeric values in the result
        numeric_sum = sum(float(word) for word in result_words if word.replace('.', '').isdigit())
        
        # Calculate the average length of words in the result
        avg_word_length = sum(len(word) for word in result_words) / len(result_words) if result_words else 0
        
        # Attempt to evaluate any numeric expressions found in the result
        expression_sum = 0
        for word in result_words:
            try:
                expression_sum += eval(word)
            except:
                pass
        
        # Sort the words and join with commas
        sorted_words = ','.join(sorted(result_words))
        
        # Return the sorted words along with the numeric sum, average word length, and expression sum
        return f'{sorted_words}, numeric sum: {numeric_sum:.2f}, average word length: {avg_word_length:.2f}, expression sum: {expression_sum}'
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words
        input_words = str(input_data).lower().split()
        
        # Calculate the average length of words
        avg_word_length = sum(len(word) for word in input_words) / len(input_words) if input_words else 0
        
        # Attempt to evaluate any numeric expressions found in the text
        expression_sum = 0
        for word in input_words:
            try:
                expression_sum += eval(word)
            except:
                pass
        
        # Calculate the sum of numeric values in the text
        numeric_sum = sum(float(word) for word in input_words if word.replace('.', '').isdigit())
        
        # Sort the words and join with commas
        sorted_words = ','.join(sorted(input_words))
        
        # Return the sorted words along with the average word length, numeric sum, and expression sum
        return f'{sorted_words}, average word length: {avg_word_length:.2f}, numeric sum: {numeric_sum:.2f}, expression sum: {expression_sum}'