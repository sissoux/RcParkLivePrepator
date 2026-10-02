import unittest

from overlay_preparator import OverlayPreparator


class DummyVar:
    def __init__(self, value=""):
        self.value = value

    def get(self):
        return self.value


class OverlayPreparatorTests(unittest.TestCase):
    def test_get_selected_file_paths_skips_blank_entries(self):
        app = OverlayPreparator.__new__(OverlayPreparator)
        app.file_paths = {
            "ScreenPodiumVide": DummyVar("C:/images/podium.png"),
            "ScreenRanking": DummyVar(""),
            "ScreenStartLineVide": DummyVar("C:/images/start.png"),
            "BandeauSeul": DummyVar("   "),
        }

        selected = app.get_selected_file_paths()

        self.assertEqual(
            selected,
            [
                ("ScreenPodiumVide", "C:/images/podium.png"),
                ("ScreenStartLineVide", "C:/images/start.png"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
