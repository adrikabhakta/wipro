import logging
import os
from pathlib import Path


class CustomLogger:
    """
    Custom Logger utility for generating execution logs in console and log files.
    """
    @staticmethod
    def get_logger(name: str = "AutomationLogger") -> logging.Logger:
        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            # Locate log directory relative to project root
            base_dir = Path(__file__).resolve().parent.parent
            log_dir = base_dir / "reports" / "logs"
            log_dir.mkdir(parents=True, exist_ok=True)
            log_file = log_dir / "automation.log"

            # Formatter
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)-8s | [%(filename)s:%(lineno)d] | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            # File Handler
            file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger
