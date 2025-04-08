def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title and content
        lowercase_input = input_data.lower()
        
        # Check for specific Wikipedia page types
        if 'wikipedia' in lowercase_input:
            if 'data analysis' in lowercase_input:
                return "wikipedia data analysis html document detected"
            elif 'mathematics' in lowercase_input:
                return "wikipedia mathematics html document detected"
            elif 'text processing' in lowercase_input:
                return "wikipedia text processing html document detected"
            else:
                return "generic wikipedia html document detected"
        else:
            # Check for other types of HTML documents
            if 'data analysis' in lowercase_input:
                return "data analysis html document detected"
            elif 'mathematics' in lowercase_input:
                return "mathematics html document detected"
            elif 'text processing' in lowercase_input:
                return "text processing html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, and join it back together
            sorted_items = sorted(input_data.split(','))
            processed_items = [item.strip().lower() for item in sorted_items if item.strip()]
            
            # Try to evaluate the processed items as a mathematical expression
            try:
                result = eval(','.join(processed_items))
                return str(result).lower()
            except:
                # If evaluation fails, try to evaluate individual items
                results = []
                for item in processed_items:
                    try:
                        result = eval(item)
                        results.append(str(result).lower())
                    except:
                        results.append(item)
                
                # Return the sorted and processed items, joining with commas
                return ','.join(results)
        else:
            # If it's not a string, return a lowercase string representation
            return str(input_data).lower()