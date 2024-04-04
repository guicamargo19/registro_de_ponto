from pathlib import Path

import qdarktheme

# CAMINHOS

ROOT_DIR = Path(__file__).parent
ICON_DIR = ROOT_DIR / 'src'
ICON = ICON_DIR / 'gtatelie_ico.png'

ROOT_DIR_LOGO = Path(__file__).parent
LOGO_DIR = ROOT_DIR_LOGO / 'src'
LOGO = LOGO_DIR / 'gtatelie.png'

# COLORS

PRIMARY_COLOR = '#87baab'
BUTTON_INICIAL_COLOR = '#87baab'
DARKER_PRIMARY_COLOR = '#326273'
DARKEST_PRIMARY_COLOR = '#326273'

# SIZING

BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500

# QSS - application THEME


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {BUTTON_INICIAL_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='light',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {"primary": f"{PRIMARY_COLOR}", },
            "[light]": {"primary": f"{PRIMARY_COLOR}", },
        },
        additional_qss=qss,
    )
