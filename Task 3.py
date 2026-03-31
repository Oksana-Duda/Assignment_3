def analyze_methodes(data):
    res_data={}
    for i in data:
        res_data[data["method"]]={}
        res_data[data["method"]]["max_error"]=0
        res_data[data["method"]]["iterations_count"]=0
        res_data[data["method"]]["total_time_ms"]=0
    for i in data:
        res_data[data["method"]["max_error"]]=max(res_data[data["method"]["max_error"]], data["error"])
        res_data[data["method"]["iterations_count"]] = max(res_data[data["method"]["iterations_count"]], data["iteration"])
        res_data[data["method"]["total_time_ms"]] = max(res_data[data["method"]["total_time_ms"]], data["time_ms"])
    return res_data