def analyze_methodes(data):
    res_data={}
    for i in data:
        res_data[i["method"]]={}
        res_data[i["method"]]["max_error"]=0
        res_data[i["method"]]["iterations_count"]=0
        res_data[i["method"]]["total_time_ms"]=0
    for i in data:
        res_data[i["method"]]["max_error"]=max(res_data[i["method"]]["max_error"], i["error"])
        res_data[i["method"]]["iterations_count"] = max(res_data[i["method"]]["iterations_count"], i["iteration"])
        res_data[i["method"]]["total_time_ms"] = res_data[i["method"]]["total_time_ms"]+ i["time_ms"]
    return res_data

experiments_data = [
{"method": "Euler", "iteration": 1, "error": 0.15,
"time_ms": 1.2},
{"method": "Runge-Kutta", "iteration": 1, "error": 0.01,
"time_ms": 3.5},
{"method": "Euler", "iteration": 2, "error": 0.18,
"time_ms": 1.3},
{"method": "Runge-Kutta", "iteration": 2, "error": 0.008,
"time_ms": 3.6},
{"method": "Euler", "iteration": 3, "error": 0.22,
"time_ms": 1.2},
{"method": "Newton", "iteration": 1, "error": 0.05,
"time_ms": 2.1}
]

res = analyze_methodes(experiments_data)
print(res)