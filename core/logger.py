import logging
import os
import sys
import rich

from datetime import datetime
from rich.logging import RichHandler
from rich.theme import Theme
from rich.style import Style

from core.settings import get_settings

settings = get_settings()

def init_logging():
    logger = logging.getLogger()

    if not os.path.isdir('./logs'):
        try:
            os.mkdir('./logs')
            logger.info('Creating log directory')
        except OSError as err:
            logger.error(f'Failed to create log directory: {err}')

    if settings.log_rich_formatter:
        rich_console = rich.get_console()
        rich.reconfigure(tab_size = 4)
        # Theme from https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/redbot/logging.py
        rich_console.push_theme(Theme(
            {
                    'log.time': Style(dim = True),
                    'logging.level.warning': Style(color = 'yellow'),
                    'logging.level.critical': Style(color = 'white', bgcolor = 'red'),
                    'logging.level.error': Style(color = 'red'),
                    'logging.level.verbose': Style(color = 'magenta', italic = True, dim = True),
                    'logging.level.trace': Style(color = 'white', italic = True, dim = True),
                    'repr.number': Style(color = 'cyan'),
                    'repr.url': Style(underline = True, italic = True, bold = False, color = 'cyan'),
            }
        ))
        rich_console.file = sys.stdout
        rich_formatter = logging.Formatter('{message}', datefmt = '[%X]', style = '{')
        stdout_handler = RichHandler(
            rich_tracebacks = True
        )
        stdout_handler.setFormatter(rich_formatter)
    else:
        stdout_handler = logging.StreamHandler(sys.stdout)

    log_handlers = [stdout_handler]
    if settings.log_save:
        log_name = f'./logs/main{datetime.now().strftime("%Y%m%d")}.log'
        filehandler = logging.FileHandler(log_name, encoding='utf-8')
        filehandler.setLevel(settings.log_level)
        log_handlers.append(filehandler) # type: ignore

    logging.basicConfig(
        level = settings.log_level,
        datefmt = '%Y-%m-%d %H:%M:%S',
        format = '[{asctime}] [{levelname}] {name}: {message}',
        style = '{',
        handlers = log_handlers
    )

    logging.captureWarnings(True)

    return True
