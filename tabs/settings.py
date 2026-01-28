from tkinter import *
from tkinter import ttk
import dataMgr as d

def create(notebook: ttk.Notebook):
	settingsFrame = ttk.Frame(notebook, padding=(10,10,10,10))
	notebook.add(settingsFrame, text="Settings")
	ttk.Label(settingsFrame, "TODO")
	