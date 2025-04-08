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
            # If it's not a recognized type, process as a generic HTML document
            # Extract and sort unique words from the document
            words = sorted(set(word.strip() for word in lowercase_input.split() if word.strip()))
            
            # Return the first 5 keywords and attempt to evaluate them as a mathematical expression
            keyword_string = ', '.join(words[:5])
            try:
                result = eval(keyword_string)
                return f"generic html document detected with keywords: {keyword_string}. Evaluated result: {str(result).lower()}"
            except Exception as e:
                return f"generic html document detected with keywords: {keyword_string}. Evaluation failed: {str(e)}"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Check if it's a comma-separated list
            if ',' in input_data:
                # Split the input, sort it, and join it back together
                sorted_items = sorted(input_data.split(','))
                processed_items = [item.strip().lower() for item in sorted_items if item.strip()]
                
                # Attempt to evaluate the processed items as a mathematical expression
                try:
                    result = eval(','.join(processed_items))
                    return f"processed list: {','.join(processed_items)}. Evaluated result: {str(result).lower()}"
                except Exception as e:
                    return f"processed list: {','.join(processed_items)}. Evaluation failed: {str(e)}"
            else:
                # If it's not a list, return the input as a lowercase string
                return input_data.strip().lower()
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort and join its elements
            sorted_items = sorted(str(item).strip().lower() for item in input_data if str(item).strip())
            
            # Attempt to evaluate the sorted items as a mathematical expression
            try:
                result = eval(','.join(sorted_items))
                return f"processed collection: {','.join(sorted_items)}. Evaluated result: {str(result).lower()}"
            except Exception as e:
                return f"processed collection: {','.join(sorted_items)}. Evaluation failed: {str(e)}"
        else:
            # For other types, return a lowercase string representation
            return str(input_data).lower()