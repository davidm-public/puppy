from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QToolBar, QAction
)
from PyQt5.QtCore import Qt, QSize
from .editorpane import EditorPane
from ..resources import load_icon


class ButtonBar(QToolBar):
    """
    Represents the bar of buttons across the top of the editor and defines
    their behaviour.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.configure()

    def configure(self):
        """Set up the buttons"""
        self.setMovable(False)
        self.setIconSize(QSize(64, 64))
        self.setToolButtonStyle(3)
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setObjectName("StandardToolBar")
        # Create actions to be added to the button bar.
        self.new_python_file_act = QAction(
            load_icon("new"),
            "New", self,
            statusTip="Create a new Python file",
            triggered=self._new_python_file)
        self.open_python_file_act = QAction(
            load_icon("open"),
            "Open", self,
            statusTip="Open a Python file",
            triggered=self._open_python_file)
        self.save_python_file_act = QAction(
            load_icon("save"),
            "Save", self,
            statusTip="Save a Python file",
            triggered=self._save_python_file)
        self.run_python_file_act = QAction(
            load_icon("run"),
            "Run", self,
            statusTip="Run your Python file",
            triggered=self._run_python_file)
        self.build_python_file_act = QAction(
            load_icon("build"),
            "Build", self,
            statusTip="Build Python into Hex file",
            triggered=self._build_python_file)
        self.zoom_in_act = QAction(
            load_icon("zoom-in"),
            "Zoom in", self,
            statusTip="Make the text bigger",
            triggered=self._zoom_in)
        self.zoom_out_act = QAction(
            load_icon("zoom-out"),
            "Zoom out", self,
            statusTip="Make the text smaller",
            triggered=self._zoom_out)

        # Add the actions to the button bar.
        self.addAction(self.new_python_file_act)
        self.addAction(self.open_python_file_act)
        self.addAction(self.save_python_file_act)
        self.addSeparator()
        self.addAction(self.run_python_file_act)
        self.addAction(self.build_python_file_act)
        self.addSeparator()
        self.addAction(self.zoom_in_act)
        self.addAction(self.zoom_out_act)

    def _new_python_file():
        """
        Handle the creation of a new Python file.
        """
        pass

    def _open_python_file():
        """
        Handle opening an existing Python file.
        """
        pass

    def _save_python_file():
        """
        Save the current Python file.
        """
        pass

    def _run_python_file():
        """
        Attempt to run the current file.
        """
        pass

    def _build_python_file():
        """
        Generate a .hex file to flash onto a micro:bit.
        """
        pass

    def _zoom_in():
        """
        Make the text BIGGER.
        """
        pass

    def _zoom_out():
        """
        Make the text smaller.
        """
        pass


class Editor(QWidget):
    """
    Represents the application.
    """
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.project = project

        # Gotta have a nice icon.
        # Vertical box layout.
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # The application has two aspects to it: buttons and the editor.
        self.buttons = ButtonBar(parent=self)
        self.tabs = QTabWidget(parent=self)

        # Add the buttons and editor to the user inteface.
        self.layout.addWidget(self.buttons)
        self.layout.addWidget(self.tabs)
        # Ensure we have a minimal sensible size for the application.
        self.setMinimumSize(800, 600)

    def add_tab(self, path):
        text = self.project.read_file(path)
        editor = EditorPane()
        editor.path = path
        editor.setText(text)
        self.tabs.addTab(editor, path)