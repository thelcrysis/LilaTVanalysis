### integration of scraper and plotter with save file in .txt formatted
import time
import matplotlib.pyplot as plt
import string
from selenium import webdriver            #all dependencies
import time
from time import gmtime, strftime
import main
import plotter

print "Number of checks, check is ~2sec long"
cycles = raw_input()

main.scraper(int(cycles))
plotter.Plotter()
