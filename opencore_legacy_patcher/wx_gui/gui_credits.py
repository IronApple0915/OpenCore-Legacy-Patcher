"""
gui_Credits.py: Credits Menu
"""

import wx
import logging
import webbrowser
import os

from .. import constants
from ..wx_gui import gui_support


class CreditsFrame(wx.Frame):
    """
    Credits menu with carousel.
    Each person contains:
        - Profile picture
        - Name Button that links to website
        - Description
    """

    def __init__(
        self,
        parent: wx.Frame,
        title: str,
        global_constants: constants.Constants,
        screen_location: tuple = None
    ) -> None:
        logging.info("Initializing Credits Frame")

        self.dialog = wx.Dialog(
            parent,
            title=title,
            size=(1000, 430)
        )

        self.constants: constants.Constants = global_constants
        self.title: str = title

        self.card_width = 280
        self.card_height = 285
        self.card_spacing = 20
        #set carousel speed
        self.carousel_delay = 2000
        self.animation_step = 20
        self.animation_distance = self.card_width + self.card_spacing
        self.carousel_timer = None
        self.animation_timer = None
        self.animation_position = 0
        self.is_animating = False
        self._generate_elements(self.dialog)
        self.dialog.ShowWindowModal()

    def _get_people(self):

        return [
            {
                "name": "Mykola Grymalyuk",
                "link": "https://github.com/Khronokernel",
                "profile_picture": str(self.constants.icns_profiles_path / "mykola_grymalyuk.png"),
                "contribution": "Main co-author"
            },
            {
                "name": "Dhinak G",
                "link": "https://github.com/DhinakG",
                "profile_picture": str(self.constants.icns_profiles_path / "dhinakg.png"),
                "contribution": "Main co-author"
            },
            {
                "name": "Vit9696",
                "link": "https://github.com/vit9696",
                "profile_picture": str(self.constants.icns_profiles_path / "vit9696.png"),
                "contribution": "Endless amount of help troubleshooting, determining fixes and writing patches"
            },
            {
                "name": "Dosdude1",
                "link": "https://github.com/dosdude1",
                "profile_picture": str(self.constants.icns_profiles_path / "dosdude1.png"),
                "contribution": "Main author of the original GUI, Development of previous patchers, laying out much of what needs to be patched"
            },
            {
                "name": "Acidanthera",
                "link": "https://github.com/Acidanthera",
                "profile_picture": str(self.constants.icns_profiles_path / "acidanthera.png"),
                "contribution": "OpenCorePkg, as well as many of the core kexts and tools"
            },
            {
                "name": "Asentientbot",
                "link": "https://github.com/ASentientBot",
                "profile_picture": str(self.constants.icns_profiles_path / "asentientbot.png"),
                "contribution": "non-Metal patch set, Metal bundle interposer, dsce"
            },
            {
                "name": "EduCovas",
                "link": "",
                "profile_picture": str(self.constants.icns_profiles_path / "educovas.png"),
                "contribution": "non-Metal patch set, 3802 Metal patch set, MetallibSupportPkg, IOSurface offset patches, legacy Wi-Fi patch set, T1 patch set, AppleGVA downgrade, USB 1 patches"
            },
            {
                "name": "ASentientHedgehog",
                "link": "https://github.com/moosethegoose2213",
                "profile_picture": str(self.constants.icns_profiles_path / "asentienthedgehog.png"),
                "contribution": "non-Metal patch set"
            },
            {
                "name": "Flagers",
                "link": "https://github.com/flagersgit",
                "profile_picture": str(self.constants.icns_profiles_path / "flagers.png"),
                "contribution": "non-Metal patch set, Metal bundle interposer, Nvidia's WebDriver Development"
            },
            {
                "name": "Ausdauersportler",
                "link": "https://github.com/Ausdauersportler",
                "profile_picture": str(self.constants.icns_profiles_path / "ausdauersportler.png"),
                "contribution": "iMacs Metal GPUs Upgrade Patch set and documentation"
            },
            {
                "name": "Jazzzny",
                "link": "https://github.com/Jazzzny",
                "profile_picture": str(self.constants.icns_profiles_path / "jazzzny.png"),
                "contribution": "UEFI Legacy XHCI, NVIDIA OpenCL, LegacyKeyboardInjector, Pre-Ivy Bridge Aquantia Ethernet Patch, Non-Metal Photo Booth, GUI and Backend Development, Vaulting implementation"
            },
            {
                "name": "Crystall1nedev",
                "link": "https://enclave.fruitycord.org/crystll1ne",
                "profile_picture": str(self.constants.icns_profiles_path / "crystall1nedev.png"),
                "contribution": "Dirty Root Volume checks & Many, Many, Many hours of testing. "
            },
            {
                "name": "ThatStella7922",
                "link": "https://github.com/ThatStella7922",
                "profile_picture": str(self.constants.icns_profiles_path / "thatstella7922.png"),
                "contribution": "Donated Hardware: 2017 13 inch MacBook Pro (A1708)"
            },
            {
                "name": "IronApple",
                "link": "https://github.com/IronApple0915",
                "profile_picture": str(self.constants.icns_profiles_path / "ironapple.png"),
                "contribution": "Many, Many, Many hours of testing."
            },
            {
                "name": "socamx",
                "link": "https://github.com/socamx",
                "profile_picture": str(self.constants.icns_profiles_path / "socamx.png"),
                "contribution": "Hello, dumbass."
            },
            {
                "name": "Paradox94",
                "link": "https://github.com/ParaDoX1994",
                "profile_picture": str(self.constants.icns_profiles_path / "paradox94.png"),
                "contribution": "Guide rewrite, Many, Many, Many hours of testing."
            },
            {
                "name": "Mr.Macintosh",
                "link": "https://mrmacintosh.com/",
                "profile_picture": str(self.constants.icns_profiles_path / "mrmacintosh.png"),
                "contribution": "Endless hours helping architect and troubleshoot many portions of the project"
            },
            {
                "name": "Mario_bros_tech",
                "link": "https://github.com/mariobrostech",
                "profile_picture": str(self.constants.icns_profiles_path / "mario_bros_tech.png"),
                "contribution": "Unsupported Macs Discord: The Catalyst that started OpenCore Legacy Patcher"
            },
            {
                "name": "Cdf",
                "link": "https://github.com/cdf",
                "profile_picture": str(self.constants.icns_profiles_path / "cdf.png"),
                "contribution": "Mac Pro on OpenCore Patch set and documentation, Innie and NightShiftEnabler"
            },
            {
                "name": "Syncretic",
                "link": "https://forums.macrumors.com/members/syncretic.1173816/",
                "profile_picture": str(self.constants.icns_profiles_path / "syncretic.png"),
                "contribution": "AAAMouSSE, telemetrap and SurPlus"
            },
            {
                "name": "Parrotgeek1",
                "link": "https://github.com/parrotgeek1",
                "profile_picture": str(self.constants.icns_profiles_path / "parrotgeek1.png"),
                "contribution": "VMM Patch Set"
            },
            {
                "name": "BarryKN",
                "link": "https://github.com/BarryKN",
                "profile_picture": str(self.constants.icns_profiles_path / "barrykn.png"),
                "contribution": "Development of previous patchers, laying out much of what needs to be patched"
            },
            {
                "name": "Arter97",
                "link": "https://github.com/arter97",
                "profile_picture": str(self.constants.icns_profiles_path / "arter97.png"),
                "contribution": "SimpleMSR to disable firmware throttling in Nehalem+ MacBooks without batteries"
            },
            {
                "name": "Joevt",
                "link": "https://github.com/joevt",
                "profile_picture": str(self.constants.icns_profiles_path / "joevt.png"),
                "contribution": "FixPCIeLinkrate"
            },
            {
                "name": "JohnD",
                "link": "https://forums.macrumors.com/members/johnd.53633/",
                "profile_picture": str(self.constants.icns_profiles_path / "JohnD.png"),
                "contribution": "Donated Hardware: 2013 Mac Pro"
            },
            {
                "name": "SpiGAndromeda",
                "link": "https://github.com/SpiGAndromeda",
                "profile_picture": str(self.constants.icns_profiles_path / "SpiGAndromeda.png"),
                "contribution": "Donated Hardware: AMD Vega 64"
            },
            {
                "name": "turbomacs",
                "link": "https://github.com/turbomacs",
                "profile_picture": str(self.constants.icns_profiles_path / "turbomacs.png"),
                "contribution": "Donated Hardware: 2014 5k iMac"
            },{
                "name": "vinaypundith",
                "link": "https://forums.macrumors.com/members/vinaypundith.1212357/",
                "profile_picture": str(self.constants.icns_profiles_path / "vinaypundith.png"),
                "contribution": "Donated Hardware: Macbook 7,1"
            },
            {
                "name": "Apple",
                "link": "https://www.apple.com",
                "profile_picture": str(self.constants.icns_profiles_path / "apple.png"),
                "contribution": "MacOS and The Mac Hardware"
            }
        ]

    def _generate_elements(self, frame=None):
        frame = self.dialog if frame is None else frame
        title_label = wx.StaticText(frame, label="Credits", pos=(-1, 5))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        title_label.Centre(wx.HORIZONTAL)

        text_label = wx.StaticText(
            frame,
            label="OCLP has been made possible by these amazing people:",
            pos=(-1, 35)
        )
        text_label.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        text_label.Centre(wx.HORIZONTAL)

        visible_width = (
            self.card_width * 3
            + self.card_spacing * 2
        )

        self.carousel_panel = wx.Panel(
            frame,
            pos=((1000 - visible_width) // 2, 75),
            size=(visible_width, self.card_height)
        )
        self.carousel_panel.SetBackgroundColour(frame.GetBackgroundColour())
        self.people = self._get_people()
        self.cards = []

        for person in self.people:
            self.cards.append(
                self._create_person_card(self.carousel_panel, person)
            )

        self._position_cards()
        self.carousel_timer = wx.Timer(self.carousel_panel)
        self.carousel_panel.Bind(
            wx.EVT_TIMER,
            self._start_carousel_animation,
            self.carousel_timer
        )
        self.carousel_timer.Start(self.carousel_delay)

        return_button = wx.Button(
            frame,
            label="Return to Main Menu",
            size=(170, 30)
        )
        return_button.Bind(wx.EVT_BUTTON, lambda event: frame.Close())
        return_button.SetPosition(
            ((1000 - return_button.GetSize()[0]) // 2, 350)
        )

    def _create_person_card(self, parent, person):
        card = wx.Panel(
            parent,
            size=(self.card_width, self.card_height)
        )
        card.SetBackgroundColour(parent.GetBackgroundColour())

        picture = self._load_profile_picture(person["profile_picture"])
        profile_image = wx.StaticBitmap(card, bitmap=picture)
        profile_image.SetPosition(
            ((self.card_width - 150) // 2, 10)
        )

        name_button = wx.Button(
            card,
            label=person["name"],
            size=(230, 35)
        )
        name_button.SetPosition(
            ((self.card_width - 230) // 2, 145)
        )
        name_button.SetFont(
            gui_support.font_factory(12, wx.FONTWEIGHT_BOLD)
        )

        if person["link"]:
            name_button.Bind(
                wx.EVT_BUTTON,
                lambda event, link=person["link"]: webbrowser.open(link)
            )
        else:
            name_button.Enable(False)

        contribution = wx.StaticText(
            card,
            label=person["contribution"],
            size=(250, 75),
            style=wx.ALIGN_CENTER_HORIZONTAL
        )
        contribution.SetFont(
            gui_support.font_factory(11, wx.FONTWEIGHT_NORMAL)
        )
        contribution.Wrap(250)
        contribution.SetPosition(
            ((self.card_width - 250) // 2, 190)
        )
        contribution.SetWindowStyleFlag(wx.ALIGN_CENTER_HORIZONTAL)
        return card

    def _load_profile_picture(self, picture_path):
        if os.path.isfile(picture_path):
            image = wx.Image(picture_path, wx.BITMAP_TYPE_ANY)

            if image.IsOk():
                return self._scale_image(image, 150, 120)

        # Placeholder profile picture
        bitmap = wx.Bitmap(150, 120)
        dc = wx.MemoryDC(bitmap)
        dc.Clear()
        dc.SetFont(gui_support.font_factory(12, wx.FONTWEIGHT_NORMAL))
        text = "NO IMAGE"
        text_width, text_height = dc.GetMultiLineTextExtent(text)
        dc.DrawLabel(
            text,
            wx.Rect(
                (150 - text_width) // 2,
                (120 - text_height) // 2,
                text_width,
                text_height
            )
        )
        dc.SelectObject(wx.NullBitmap)
        return bitmap

    def _scale_image(self, image, width, height):
        image_width = image.GetWidth()
        image_height = image.GetHeight()

        if image_width <= 0 or image_height <= 0:
            return wx.Bitmap(width, height)

        # Scaling the image
        scale = min(
            float(width) / image_width,
            float(height) / image_height
        )

        new_width = max(1, int(image_width * scale))
        new_height = max(1, int(image_height * scale))

        image = image.Scale(
            new_width,
            new_height,
            wx.IMAGE_QUALITY_HIGH
        )

        # Make image square first.
        diameter = min(new_width, new_height)

        crop_x = (new_width - diameter) // 2
        crop_y = (new_height - diameter) // 2

        image = image.GetSubImage(
            wx.Rect(
                crop_x,
                crop_y,
                diameter,
                diameter
            )
        )

        # Create a transparent image and copy only the pixels inside a circle into it.
        circle = wx.Image(diameter, diameter, True)
        circle.InitAlpha()

        radius = diameter / 2.0
        center = radius

        for y in range(diameter):
            for x in range(diameter):
                dx = x + 0.5 - center
                dy = y + 0.5 - center

                if (dx * dx + dy * dy) <= (radius * radius):
                    circle.SetRGB(
                        x,
                        y,
                        image.GetRed(x, y),
                        image.GetGreen(x, y),
                        image.GetBlue(x, y)
                    )
                    circle.SetAlpha(x, y, 255)
                else:
                    circle.SetAlpha(x, y, 0)

        # Put the circular image into bitmap
        bitmap = wx.Bitmap(width, height)
        dc = wx.MemoryDC(bitmap)
        dc.Clear()

        circle_bitmap = wx.Bitmap(circle)

        x = (width - diameter) // 2
        y = (height - diameter) // 2

        dc.DrawBitmap(
            circle_bitmap,
            x,
            y,
            True
        )

        dc.SelectObject(wx.NullBitmap)

        return bitmap

    def _position_cards(self):
        visible_width = (
            self.card_width * 3
            + self.card_spacing * 2
        )

        start_x = 0

        for index, card in enumerate(self.cards):
            x = start_x + index * (self.card_width + self.card_spacing)
            card.SetPosition((x, 0))
            if index < 3:
                card.Show()
            else:
                card.Hide()

        self.carousel_panel.Refresh()

    def _start_carousel_animation(self, event):
        if self.is_animating:
            return

        self.is_animating = True
        self.animation_position = 0

        self.animation_timer = wx.Timer(self.carousel_panel)

        self.carousel_panel.Bind(
            wx.EVT_TIMER,
            self._animate_carousel,
            self.animation_timer
        )

        self.animation_timer.Start(self.animation_step)

    def _animate_carousel(self, event):
        move_amount = 8
        self.animation_position += move_amount

        for card in self.cards:
            x, y = card.GetPosition()
            card.SetPosition((x - move_amount, y))

        if self.animation_position >= self.animation_distance:
            self.animation_timer.Stop()
            self.animation_timer.Destroy()
            self.animation_timer = None

            first_card = self.cards.pop(0)
            self.cards.append(first_card)
            for index, card in enumerate(self.cards):
                x = index * (self.card_width + self.card_spacing)
                card.SetPosition((x, 0))

                if index < 3:
                    card.Show()
                else:
                    card.Hide()

            self.is_animating = False

        self.carousel_panel.Refresh()

    def __del__(self):
        try:
            if self.carousel_timer:
                self.carousel_timer.Stop()
            if self.animation_timer:
                self.animation_timer.Stop()
        except Exception:
            pass