import os
from werkzeug.utils import secure_filename
from urllib.request import Request
from flask import Flask, render_template, Response, request, redirect, flash
from Myfunctions import *
import urllib
import secrets
import cv2
