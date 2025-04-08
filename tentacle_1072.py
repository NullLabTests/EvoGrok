import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known titles and content
        if 'data analysis' in input_data.lower():
            return 'data analysis wikipedia html document detected'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics wikipedia html document detected'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing wikipedia html document detected'.lower()
        else:
            # Check for other common HTML document types
            if 'wikipedia' in input_data.lower():
                return 'generic wikipedia html document detected'.lower()
            elif '<html lang="en">' in input_data.lower():
                return 'english language html document detected'.lower()
            else:
                return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        return ','.join(sorted(str(result).split()))
    except:
        # If evaluation fails, process the input based on its type
        if isinstance(input_data, (list, tuple, set)):
            # If input is a collection, convert each item to string, lowercase, split, sort, and join
            processed_items = []
            for item in input_data:
                processed_items.extend(sorted(str(item).lower().split()))
            return ','.join(sorted(processed_items))
        elif isinstance(input_data, dict):
            # If input is a dictionary, process keys and values separately
            keys = ','.join(sorted([str(k).lower() for k in input_data.keys()]))
            values = ','.join(sorted([str(v).lower() for v in input_data.values()]))
            return f"keys:{keys},values:{values}"
        elif isinstance(input_data, str):
            # Attempt to parse as JSON if it's a string
            try:
                json_data = json.loads(input_data)
                if isinstance(json_data, dict):
                    keys = ','.join(sorted([str(k).lower() for k in json_data.keys()]))
                    values = ','.join(sorted([str(v).lower() for v in json_data.values()]))
                    return f"json keys:{keys},json values:{values}"
                else:
                    return ','.join(sorted(str(json_data).lower().split()))
            except json.JSONDecodeError:
                # If not JSON, process as regular string
                return ','.join(sorted(input_data.lower().split()))
        else:
            # For other types of input, convert to lowercase, split, sort, and join
            return ','.join(sorted(str(input_data).lower().split()))