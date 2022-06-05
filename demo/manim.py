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