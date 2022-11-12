import os
import logging
import logging.handlers


class Logger:
    def __init__(
        self,
        name,
        ch_level=logging.INFO,
        fh_level=logging.DEBUG,
        log_dir="logs",
        log_file="log",
        when="midnight",
        interval=1,
        backup_count=7,
    ):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, log_file)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - [%(name)s:%(lineno)s] - %(levelname)s - %(message)s"
        )

        # create file handler which logs even debug messages
        file_handler = logging.handlers.TimedRotatingFileHandler(
            log_file, when=when, interval=interval, backupCount=backup_count
        )
        file_handler.suffix = "%Y-%m-%d.log"
        file_handler.setLevel(fh_level)
        file_handler.setFormatter(formatter)

        # create console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(ch_level)
        console_handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)
