def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of Wikipedia page based on known titles
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis page detected".lower()
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics page detected".lower()
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing page detected".lower()
        else:
            return "wikipedia page detected".lower()
    
    try:
        # Split the input by commas, sort the resulting list, and join it back
        sorted_items = sorted(input_data.split(','))
        result = ','.join(sorted_items)
        
        # Attempt to evaluate the sorted and joined result as a mathematical expression
        eval_result = eval(result)
        
        # If evaluation succeeds, return the result as a lowercase string
        return str(eval_result).lower()
    except:
        # If evaluation fails, return the sorted and joined result as a lowercase string
        return result.lower()