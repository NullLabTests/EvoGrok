import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lower_input = input_data.lower()
        
        # Determine the type of HTML document based on the title and content
        if 'data analysis' in lower_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lower_input:
            return "wikipedia text processing html document detected"
        else:
            # Check for specific classes or attributes
            if 'class="mw-page-title-main"' in lower_input:
                # Extract the title if possible
                title_match = re.search(r'class="mw-page-title-main">(.*?)</', lower_input)
                if title_match:
                    return f"wikipedia {title_match.group(1)} html document detected"
                else:
                    return "wikipedia generic html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, lowercase it, and sort its characters
        sorted_result = ''.join(sorted(str(result).lower()))
        
        # Count the number of unique characters
        unique_chars = len(set(sorted_result))
        
        # Calculate the sum of digits if any are present
        digit_sum = sum(int(char) for char in sorted_result if char.isdigit())
        
        # Calculate the product of digits if any are present
        digit_product = 1
        for char in sorted_result:
            if char.isdigit():
                digit_product *= int(char)
        
        # Check if the result is related to data analysis, mathematics, or text processing
        if 'data' in sorted_result or 'analysis' in sorted_result:
            context = "data analysis"
        elif 'math' in sorted_result or any(char in '+-*/^' for char in sorted_result):
            context = "mathematics"
        elif any(word in sorted_result for word in ['text', 'process', 'string', 'regex']):
            context = "text processing"
        else:
            context = "general"
        
        return f"{sorted_result} (unique characters: {unique_chars}, digit sum: {digit_sum}, digit product: {digit_product}, context: {context})"
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, str):
            # Split the input, sort it, remove duplicates, and join it back together
            sorted_items = sorted(set(item.strip().lower() for item in input_data.split(',')))
            result = ','.join(sorted_items)
            
            # Count the number of items
            item_count = len(sorted_items)
            
            # Calculate the average length of items
            avg_length = sum(len(item) for item in sorted_items) / item_count if item_count > 0 else 0
            
            # Calculate the total length of all items
            total_length = sum(len(item) for item in sorted_items)
            
            # Check for context
            if any(word in result for word in ['data', 'analysis']):
                context = "data analysis"
            elif any(word in result for word in ['math', 'equation', 'formula']):
                context = "mathematics"
            elif any(word in result for word in ['text', 'process', 'string', 'regex']):
                context = "text processing"
            else:
                context = "general"
            
            return f"{result} (item count: {item_count}, average length: {avg_length:.2f}, total length: {total_length}, context: {context})"
        elif isinstance(input_data, (list, tuple, set)):
            # If it's a collection, sort its elements and join them
            sorted_items = sorted(str(item).lower() for item in input_data)
            result = ','.join(sorted_items)
            
            # Count the number of items
            item_count = len(sorted_items)
            
            # Calculate the average length of items
            avg_length = sum(len(str(item)) for item in input_data) / item_count if item_count > 0 else 0
            
            # Calculate the total length of all items
            total_length = sum(len(str(item)) for item in input_data)
            
            # Check for context
            if any(word in result for word in ['data', 'analysis']):
                context = "data analysis"
            elif any(word in result for word in ['math', 'equation', 'formula']):
                context = "mathematics"
            elif any(word in result for word in ['text', 'process', 'string', 'regex']):
                context = "text processing"
            else:
                context = "general"
            
            return f"{result} (item count: {item_count}, average length: {avg_length:.2f}, total length: {total_length}, context: {context})"
        else:
            # For other types, return a lowercase string representation
            # and include the type of the input, its length, and its hash value
            str_repr = str(input_data).lower()
            input_hash = hash(input_data)
            
            # Check for context
            if 'data' in str_repr or 'analysis' in str_repr:
                context = "data analysis"
            elif 'math' in str_repr or any(char in '+-*/^' for char in str_repr):
                context = "mathematics"
            elif any(word in str_repr for word in ['text', 'process', 'string', 'regex']):
                context = "text processing"
            else:
                context = "general"
            
            return f"{str_repr} (type: {type(input_data).__name__}, length: {len(str_repr)}, hash: {input_hash}, context: {context})"