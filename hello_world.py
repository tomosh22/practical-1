from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
import keyboard


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.

        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.angleDegrees = 0
        self.angleRadians = 0
        self.cameraZOffset = 0
        self.cameraXOffset = 0
        # Load and transform the panda actor.
        if drawPanda:
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005)
            self.pandaActor.reparentTo(self.render)
            # Loop its animation.
            self.pandaActor.loop("walk")
        if helpMenu:
            OnscreenText(text = "Help Menu", pos = (0.9,0.8),scale = 0.1,fg = (255,255,255,255))
            OnscreenText(text="Move Camera Up: W", pos=(0.9, 0.7), scale=0.1,fg = (255,255,255,255))
            OnscreenText(text="Move Camera Left: A", pos=(0.9, 0.6), scale=0.1,fg = (255,255,255,255))
            OnscreenText(text="Move Camera Down: S", pos=(0.9, 0.5), scale=0.1,fg = (255,255,255,255))
            OnscreenText(text="Move Camera Right: D", pos=(0.9, 4), scale=0.1,fg = (255,255,255,255))
            OnscreenText(text="Only works with spin camera off", pos=(0.9, 0.45), scale=0.05, fg=(255, 255, 255, 255))


    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        if spinCamera:
            self.angleDegrees = task.time * 6.0
            self.angleRadians = self.angleDegrees * (pi / 180.0)
        else:
            if keyboard.is_pressed("w"):
                self.cameraZOffset += 0.05
            if keyboard.is_pressed("s"):
                self.cameraZOffset -= 0.05
            if keyboard.is_pressed("a"):
                self.cameraXOffset -= 0.05
            if keyboard.is_pressed("d"):
                self.cameraXOffset += 0.05


        self.camera.setPos(20 * sin(self.angleRadians) + self.cameraXOffset, -20.0 * cos(self.angleRadians), 3 + self.cameraZOffset)
        self.camera.setHpr(self.angleDegrees, 0, 0)
        return Task.cont
spinCamera = True
drawPanda = True
helpMenu = True
print("Spin Camera?")
if input() != "yes":
    spinCamera = False
print("Draw Panda?")
if input() != "yes":
    drawPanda = False
print("Help Menu?")
if input() != "yes":
    helpMenu = False

app = MyApp()
app.run()
