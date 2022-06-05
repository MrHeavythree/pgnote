# manim: Animation engine for explanatory math videos

>keyword:manim python

## Introduction

In programming, making animation is important.Let's take a look at the following animation:

[ExampleScene](aseets%5CExampleScene.mp4)

Is that cool?

In fact, this is made using [Manim](https://www.github.com/3b1b/manim), a Python based animation library.Now I will make a brief introduction about it.

## Manim--install

As mentioned above, manim is a python library, so it also needs to be installed.For any system, the installation methods are:

```powershell
pip install manimgl
```

Note: you need to install the following dependencies:

1. FFmpeg
2. LaTeX(optional)
3. dvisvgm(optional)

If you have completed the above operations, you can try the following operations:

```powershell
    manimgl example_scenes.py OpeningManimExampl>
```

This should pop up a window playing a simple scene.

## Manim--bulid first animation

Let's see how the above animation is made:

```py
from manimlib import *

class ExampleScene(Scene):
    def construct(self):
        text_1 = Tex("a^{2} + b^{2} = c^{2}")
        text_2 = Text("This is the Pythagorean theorem.").next_to(text_1,DOWN)
        vg_1 = VGroup(text_1,text_2)
        text_1 = Tex(r"\int_{a}^{b} f(x)\mathrm{d}x = F(b)-F(a)")
        text_2 = Text("And this is Newton-Leibniz formula.").next_to(text_1,DOWN)
        vg_2 = VGroup(text_1,text_2)
        
        self.add(vg_1)
        self.play(Transform(vg_1,vg_2))
        self.wait()
```

Let's analyze it step by step:

1. ` from manimlib import * ` This means importing manimGL (the version of manim we are using now. There are three versions of manim: [manim cairo backend](https://github.com/3b1b/manim/tree/cairo-backend) (rendering with Cairo), manimGL and [manimCE](https://www.github.com/ManimCommunity/Manim) (community version))
2. ` class ExampleScene(Scene): ` and ` def construct(self): ` Construct a class named ExampleScene that inherits from the Scene class, and define a construct function for it. All animation codes are implemented here.
3. ` text_1 = Tex("a^{2} + b^{2} = c^{2}") `This line of code creates an instance of Tex class and takes the parameter "a^{2} + b^{2} = c^{2}".This is a LaTeX code.
4. ` text_2 = Text("This is the Pythagorean theorem.").next_to(text_1,DOWN) `This line of code creates an instance of the text class and takes the parameter "this is the Pythagorean theorem.".

    It should be noted that here:` .next_to(text_1,DOWN) ` ,This represents text_ 1 is below text_2.

5. ` vg_1 = VGroup(text_1,text_2) ` This line of code creates a VGroup example and puts text_1 and text_2 in it.VGroup is similar to the list in Python and is used to store VMobjects in manim.
6. from ` text_1 = Tex(r"\int_{a}^{b} f(x)\mathrm{d}x = F(b)-F(a)") ` to ` vg_2 = VGroup(text_1,text_2) ` This means that text_1 and text_2 re-assign and put into a new VGroup.
7. ` self.add(vg_1) `This means adding the vg_1 to the scene (that is the self).
8. ` self.play(Transform(vg_1,vg_2)) ` This means the vg_1 in this scene transform to vg_2 by Transform animation.
9. ` self.wait() `This step is purely for the sake of an interval, and it means that the animation is displayed instead of the picture.

In this way, you created your first manim program.

## Thanks

Thank you [3blue1brown](https://www.github.com/3b1b) ,You created this repository. Thank you here.

Thank the [Manim library](https://ww.github.com/3b1b/manim) ,and thanks all who contribute to manim.