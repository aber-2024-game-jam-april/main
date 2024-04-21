import arcade
import arcade.gui

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "MainMenu"
SCREEN_RESIZABLE = False


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_RESIZABLE)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        #self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        # use a decorator to handle on_click events
        @settings_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        @start_button.event("on_click")
        def on_click_start(event):
            print("Start:",event)

        @quit_button.event("on_click")
        def on_click_start(event):
            print("Event:",event)
        
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        def on_click_start(self, event):
            print("Start:", event)

        def on_draw(self):
            arcade.start_render()
            self.manager.draw()

window = MyWindow()
arcade.run()