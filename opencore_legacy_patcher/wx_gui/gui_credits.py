"""
gui_Credits.py: Credits Menu
"""

import wx
import logging
import webbrowser

from .. import constants

from ..wx_gui import gui_support


class CreditsFrame(wx.Frame):
    """
    Append to main menu through a modal dialog
    """
    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants, screen_location: tuple = None) -> None:
        logging.info("Initializing Help Frame")
        self.dialog = wx.Dialog(parent, title=title, size=(1000, 400))

        self.constants: constants.Constants = global_constants
        self.title: str = title

        self._generate_elements(self.dialog)
        self.dialog.ShowWindowModal()


    def _generate_elements(self, frame: wx.Frame = None) -> None:
        """
        Format:
            - Title: Credits
            - Button: Return to Main Menu
        """

        frame = self if not frame else frame

        title_label = wx.StaticText(frame, label="Credits", pos=(-1,5))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        title_label.Centre(wx.HORIZONTAL)

        text_label = wx.StaticText(frame, label="OCLP has been made possible by these amazing people:", pos=(-1,30))
        text_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        text_label.Centre(wx.HORIZONTAL)

        buttons = {
            "❤️Mykola Grymalyuk": "https://github.com/Khronokernel",
            "❤️Dhinak G": "https://github.com/DhinakG",
            "❤️Vit9696": "https://github.com/vit9696",
            "❤️Dosdude1": "https://github.com/dosdude1",
            "❤️Asentientbot": "https://github.com/ASentientBot",
            "❤️EduCovas": "",
            "❤️ASentientHedgehog": "https://github.com/moosethegoose2213",
            "❤️Flagers": "https://github.com/flagersgit",
            "❤️Ausdauersportler": "https://github.com/Ausdauersportler",
            "❤️Jazzzny": "https://github.com/Jazzzny",
            "❤️Crystall1nedev": "https://github.com/crystall1nedev",
            "ThatStella7922": "https://github.com/ThatStella7922",
            "IronApple": "https://github.com/IronApple0915",
            "socamx": "https://github.com/socamx",
            "Paradox94": "https://github.com/ParaDoX1994",
            "Mario_bros_tech ": "https://github.com/mariobrostech",
            "Cdf": "https://github.com/cdf",
            "Syncretic": "https://forums.macrumors.com/members/syncretic.1173816/",
            "Parrotgeek1": "https://github.com/parrotgeek1",
            "BarryKN": "https://github.com/BarryKN",
            "Arter97": "https://github.com/arter97",
            "Joevt": "https://github.com/joevt",
            "SpiraMira": "https://github.com/SpiraMira",
            "Acidanthera": "https://github.com/Acidanthera",
            "Apple": "https://www.apple.com",

        }

        button_width = 175
        button_height = 30
        button_spacing = 5
        columns = 5

        grid_width = (button_width * columns) + (button_spacing * (columns - 1))
        frame_width = frame.GetClientSize()[0]
        start_x = (frame_width - grid_width) // 2

        start_y = text_label.GetPosition()[1] + text_label.GetSize()[1] + 10

        for index, button in enumerate(buttons):
            row = index // columns
            column = index % columns

            x = start_x + column * (button_width + button_spacing)
            y = start_y + row * (button_height + button_spacing)

            help_button = wx.Button(
                frame,
                label=button,
                pos=(x, y),
                size=(button_width, button_height)
            )
            help_button.Bind(
                wx.EVT_BUTTON,
                lambda event, temp=buttons[button]: webbrowser.open(temp)
            )

        # Button: Return to Main Menu
        return_button = wx.Button(frame, label="Return to Main Menu", pos=(-1, help_button.GetPosition()[1] + help_button.GetSize()[1]), size=(150, 30))
        return_button.Bind(wx.EVT_BUTTON, lambda event: frame.Close())
        return_button.Centre(wx.HORIZONTAL)

        # Set size of frame
        frame.SetSize((-1, return_button.GetPosition()[1] + return_button.GetSize()[1] + 40))





