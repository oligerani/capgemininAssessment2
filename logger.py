# 11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self, message, level="info"):  
        levels = {"error": "[ERROR]", "warning": "[WARNING]", "info": "[INFO]"}
        log_prefix = levels.get(level.lower(), "[INFO]") 
        print(f"{log_prefix} {message}")


logger = Logger()
logger.log("System started")  
logger.log("Low disk space", "warning")
logger.log("File not found", "error")
