import json

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or JSON-like structure
        if isinstance(input_data, str):
            if ',' in input_data:
                # Process comma-separated values
                values = [v.strip() for v in input_data.split(',') if v.strip()]
                processed_values = []
                for value in values:
                    try:
                        # Attempt to evaluate each value as a mathematical expression
                        eval_result = eval(value)
                        processed_values.append(str(eval_result).lower())
                    except:
                        # If evaluation fails, check if it's a JSON-like structure
                        try:
                            json_obj = json.loads(value)
                            processed_values.append(json.dumps(json_obj, sort_keys=True).lower())
                        except:
                            # If not JSON, keep the original value
                            processed_values.append(value.lower())
                # Sort and join the processed values with commas
                return ','.join(sorted(processed_values))
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        else:
            # For non-string inputs, attempt to convert to JSON
            try:
                return json.dumps(input_data, sort_keys=True).lower()
            except:
                # If JSON conversion fails, return the string representation
                return str(input_data).lower()