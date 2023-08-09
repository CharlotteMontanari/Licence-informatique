#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

import sys

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
from tomlkit import key

###############################################################
# variables globales
year, day, hour = 0, 0, 0
quadric = None
abscisse = 0
ordonnee = 0

###############################################################


def init():
    global quadric
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)


def display():
    # permet de faire bouger la camera
    glTranslatef(abscisse, ordonnee, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 0.0, 1.0))
    glPushMatrix()
    gluSphere(quadric, 1.0, 40, 100)  # point du soleil
    glRotatef(year, 0.0, 1.0, 0.0)

    glTranslatef(2.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.0, 0.0, 1.0, 1.0))
    glRotatef(day, 0.0, 1.0, 0.0)
    gluSphere(quadric, 0.2, 20, 60)  # point de la terre
    glPushMatrix()

    glMaterialfv(
        GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.0, 1.0, 0.0, 1.0)
    )  # vert

    glTranslatef(0.4, 0.0, 0.0)

    glRotatef(hour, 0.0, 1.0, 0.0)
    gluSphere(quadric, 0.1, 20, 20)  # point de la lune
    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        glOrtho(-2.5, 2.5, -2.5 * height / width, 2.5 * height / width, -10.0, 10.0)
    else:
        glOrtho(-2.5 * width / height, 2.5 * width / height, -2.5, 2.5, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global day, year, hour
    key = key.decode("utf-8")

    # ic, la terre tourn autour du soleil
    if key == "d":
        day = (day + 20) % 360
    elif key == "D":
        day = (day - 20) % 360

    # ici, la terre tourne sur elle meme
    elif key == "y":
        year = (year + 10) % 360
    elif key == "Y":
        year = (year - 10) % 360

    # ici, la terre tourne sur elle meme et autour du soleil
    elif key == "t":
        day = (day + 20) % 360
        year = (year + 10) % 360
    elif key == "T":
        day = (day - 20) % 360
        year = (year - 10) % 360

    # ici, la lune tourne autour d'elle meme
    elif key == "l":
        hour = (hour + 5) % 360
    elif key == "L":
        hour = (hour - 5) % 360

    elif key == "\033":
        # sys.exit( )  # Exception ignored
        glutLeaveMainLoop()
    glutPostRedisplay()  # indispensable en Python

def keyboard2(key, x, y):
    global abscisse, ordonnee

    if key == GLUT_KEY_RIGHT:
        abscisse -= 0.1

    elif key == GLUT_KEY_LEFT:
        abscisse += 0.1
    
    elif key == GLUT_KEY_UP:
        ordonnee -= 0.1
    
    elif key == GLUT_KEY_DOWN:
        ordonnee += 0.1
    
    glutPostRedisplay() #permet d'actualiser


###############################################################
# MAIN

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

glutCreateWindow("planet")
glutReshapeWindow(700, 700)

glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutSpecialFunc(keyboard2)

init()

glutMainLoop()
