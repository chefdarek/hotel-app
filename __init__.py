#creates relative import paths
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import firebase_admin
default_app = firebase_admin.initialize_app()
