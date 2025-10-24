"""
LOGGING INFRASTRUCTURE
Replaces all print() statements with proper structured logging

Provides:
- Multiple log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Log rotation
- Structured logging with timestamps
- Module-specific loggers
- Configurable output (console, file, both)

Author: Semantic Substrate Database Project
License: MIT
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime


class LoggerConfig:
    """
    Centralized logging configuration for Semantic Substrate Database

    Replaces all print() statements with structured, leveled logging
    """

    def __init__(
        self,
        log_level: str = "INFO",
        log_to_file: bool = False,
        log_dir: Optional[str] = None,
        log_rotation: bool = True,
        max_bytes: int = 10485760,  # 10MB
        backup_count: int = 5
    ):
        """
        Initialize logging infrastructure

        Args:
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_to_file: Enable file logging
            log_dir: Directory for log files (default: ./logs)
            log_rotation: Enable log rotation
            max_bytes: Maximum bytes per log file before rotation
            backup_count: Number of backup files to keep
        """
        self.log_level = getattr(logging, log_level.upper(), logging.INFO)
        self.log_to_file = log_to_file
        self.log_dir = Path(log_dir) if log_dir else Path("logs")
        self.log_rotation = log_rotation
        self.max_bytes = max_bytes
        self.backup_count = backup_count

        # Create logs directory if needed
        if self.log_to_file:
            self.log_dir.mkdir(parents=True, exist_ok=True)

        # Configure root logger
        self._configure_root_logger()

    def _configure_root_logger(self):
        """Configure the root logger"""
        # Remove existing handlers
        root_logger = logging.getLogger()
        root_logger.handlers = []
        root_logger.setLevel(self.log_level)

        # Create formatters
        console_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)

        # File handler (if enabled)
        if self.log_to_file:
            log_file = self.log_dir / f"semantic_substrate_{datetime.now().strftime('%Y%m%d')}.log"

            if self.log_rotation:
                file_handler = logging.handlers.RotatingFileHandler(
                    log_file,
                    maxBytes=self.max_bytes,
                    backupCount=self.backup_count
                )
            else:
                file_handler = logging.FileHandler(log_file)

            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(file_formatter)
            root_logger.addHandler(file_handler)

    def get_logger(self, name: str) -> logging.Logger:
        """
        Get a logger for specific module

        Args:
            name: Module name (use __name__)

        Returns:
            Configured logger instance
        """
        return logging.getLogger(name)


# Global logger configuration instance
_logger_config: Optional[LoggerConfig] = None


def setup_logging(
    log_level: str = "INFO",
    log_to_file: bool = False,
    log_dir: Optional[str] = None
) -> LoggerConfig:
    """
    Setup global logging configuration

    Args:
        log_level: Logging level
        log_to_file: Enable file logging
        log_dir: Directory for log files

    Returns:
        LoggerConfig instance
    """
    global _logger_config
    _logger_config = LoggerConfig(
        log_level=log_level,
        log_to_file=log_to_file,
        log_dir=log_dir
    )
    return _logger_config


def get_logger(name: str) -> logging.Logger:
    """
    Get logger for module

    Args:
        name: Module name (use __name__)

    Returns:
        Logger instance
    """
    global _logger_config

    # Initialize default config if not set
    if _logger_config is None:
        _logger_config = LoggerConfig()

    return _logger_config.get_logger(name)


# Convenience functions for quick logging
def log_debug(message: str, logger_name: str = "semantic_substrate"):
    """Log debug message"""
    get_logger(logger_name).debug(message)


def log_info(message: str, logger_name: str = "semantic_substrate"):
    """Log info message"""
    get_logger(logger_name).info(message)


def log_warning(message: str, logger_name: str = "semantic_substrate"):
    """Log warning message"""
    get_logger(logger_name).warning(message)


def log_error(message: str, logger_name: str = "semantic_substrate", exc_info: bool = False):
    """Log error message"""
    get_logger(logger_name).error(message, exc_info=exc_info)


def log_critical(message: str, logger_name: str = "semantic_substrate", exc_info: bool = False):
    """Log critical message"""
    get_logger(logger_name).critical(message, exc_info=exc_info)
