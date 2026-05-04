def log_filter(logs:str, level:str):
    parts = logs.split(" 20") #splits the logs by the commom prefix in each new sentence, feel free to use 20 (as for the date) or a dot (.) as ever sentence finishes with one as well
    
    for part in parts:
        log_entry = part.strip() # removes extra blank spaces 
        if not log_entry.startswith("20"): # if using the dot sep method, change the line to endswith(".") then log_entry = log_entry+"." or just ignore it, after all its a final dot
            log_entry = "20" + log_entry
            
        if f" {level} " in log_entry:
            yield log_entry # using yield as the function works as a generator, thus we cant use return because we want the values kept in memory and only unveiled when needed


logs = """2023-08-15 14:15:24 INFO Starting the system. 2023-08-15 14:15:26 WARN System load is above 80%. 2023-08-15 14:15:27 ERROR Failed to connect to database. 2023-08-15 14:15:28 INFO Connection retry in 5 seconds. """

for log in log_filter(logs, 'ERROR'): print(log)





def parse_query_string(qs):
    result = {}
    parts = qs.split('&') # splits the string using & as the separation, btw, the & wont be included in any element of the list
    
    for part in parts:
        if '=' in part:
            key, val = part.split('=', 1) # same thought 
        else:
            key, val = part, ''
            
        # replace characters 
        val = val.replace('+', ' ')
        
        # Decoding the HEX code, I think theres a lobrary for it %xx 
        def decode(s):
            segments = s.split('%')
            res = segments[0]
            for seg in segments[1:]:
                if len(seg) >= 2:
                    # Convert hex to int, then to character
                    res += chr(int(seg[:2], 16)) + seg[2:]
                else:
                    res += '%' + seg
            return res

        final_key = decode(key)
        final_val = decode(val)
        
        # Logic for collecting repeated keys into a list
        if final_key in result:
            if type(result[final_key]) == list:
                result[final_key].append(final_val)
            else:
                result[final_key] = [result[final_key], final_val]
        else:
            result[final_key] = final_val
            
    return result
    
    
    
qs ="name=John+Doe&age=25&hobby=books&hobby=music" 
print(parse_query_string(qs))