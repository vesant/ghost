# File: /ghost-system/ghost-system/src/main.py

import tkinter as tk
from tkinter import messagebox
import threading
import cv2

class GhostApp:
    def __init__(self, root):
        self.root = root

        ### GUI Inicialization

        self.root.title("G.H.O.S.T. Interface")
        self.root.configure(bg="#00aaff")
        self.root.geometry("400x400")

        # Terminal-like prompt
        self.prompt = tk.Label(root, text=">", font=("Consolas", 48), bg="#00aaff", fg="black")
        self.prompt.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Message area
        self.message = tk.Label(root, text="", font=("Consolas", 14), bg="#00aaff", fg="black")
        self.message.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Start webcam thread
        self.webcam_thread = threading.Thread(target=self.webcam_loop, daemon=True)
        self.webcam_thread.start()

        ### End GUI Initialization

    def webcam_loop(self):
        cap = cv2.VideoCapture(1)  # Use 0 for default camera, 1 for external
        print(f"Webcam opened: {cap.isOpened()}, Frame size: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        while True:
            ret, frame = cap.read()
            if ret:
                # add here movement detection and reactions
                # for debug, it will display a message if movement is detected (simple diff)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if hasattr(self, 'prev_gray'):
                    diff = cv2.absdiff(self.prev_gray, gray)
                    if diff.mean() > 5:  # Simple threshold
                        self.message.config(text="Movement detected!")
                self.prev_gray = gray
            else:
                self.message.config(text="Webcam not found.")
                break
        cap.release()

def main():

    print("Initializing G.H.O.S.T. application...")
    print("G.H.O.S.T. application is running.")

    # Initialize components
    # from ai.heuristic import HeuristicAI
    # from geospatial.processor import GeospatialProcessor
    # from utils.helpers import HelperFunctions

    # heuristic_ai = HeuristicAI()
    # geospatial_processor = GeospatialProcessor()
    # helper = HelperFunctions()

    # Main application logic goes here
    # Example: heuristic_ai.learnFromData(some_data)
    # Example: geospatial_processor.processData(some_geospatial_data)

    root = tk.Tk()
    app = GhostApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()