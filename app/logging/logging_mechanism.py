import logging


class LoggingTracker:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LoggingTracker, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.logger = logging.getLogger("LoggingTracker")
            self.__initialize_logger()
            self._initialized = True  # Ensure logger is initialized only once
    
    def __initialize_logger(self):
        # Default log level
        self.logger.setLevel(logging.INFO)

        # Single handler and remove all existing handlers
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        handler = logging.StreamHandler()  # send logs to controller
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Set the logger to not propagate messages to the root logger
        self.logger.propagate = False

        self.logger.info("Logger Initialized")

    def set_log_level(self, level):
        level = level.upper()
        if hasattr(logging, level):
            self.logger.setLevel(getattr(logging, level))
            self.logger.info(f"Log level set to {level}")
        else:
            self.logger.error(f"Invalid log level: {level}. Log level not changed.")
            raise ValueError(f"Invalid log level: {level}. Valid levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
        
    def debug(self, *args):
        log_text = " ".join(map(str, args))
        self.logger.debug(log_text, stacklevel=2)
    
    def info(self, *args):
        log_text = " ".join(map(str, args))
        self.logger.info(log_text, stacklevel=2)

    def warning(self, *args):
        log_text = " ".join(map(str, args))
        self.logger.warning(log_text, stacklevel=2)
    
    def error(self, *args):
        log_text = " ".join(map(str, args))
        self.logger.error(log_text, stacklevel=2)

    def print_current_log_level(self):
        log_level = self.logger.getEffectiveLevel()
        log_level_name = logging.getLevelName(log_level)
        self.logger.info(f"Current log level: {log_level_name}")