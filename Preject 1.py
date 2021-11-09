from manim import *


class Transforms(Scene):
    def construct(self):
        hola=Text("Hola Amigos!")
        hola.scale(3)
        self.play(DrawBorderThenFill(hola),run_time=2)
        self.play(FadeOut(hola))


        c=Circle(color=GREEN)
        c.set_fill(BLUE,opacity=0.5)
        s=Square(PI/4, color=GREEN)
        s.set_fill(BLUE,opacity=0.5)
        t=Triangle(color=GREEN)
        t.set_fill(BLUE,opacity=0.5)
        ts=Text("Square")
        tc=Text("Circle")
        tt=Text("Triangle")
    
        s.scale(4)
        c.scale(2)
        t.scale(4)

        ts.next_to(s, DOWN)
        tc.next_to(c, DOWN)
        tt.next_to(t, DOWN)


        # self.play(Write(ts))
        self.play(DrawBorderThenFill(s),DrawBorderThenFill(ts))

    
        # self.play(Transform(ts,tc))
        self.play(Transform(s,c),Transform(ts,tc))
  
        # self.play(Transform(ts,tt))
        self.play(Transform(s,t),Transform(ts,tt))
  
        self.play(FadeOut(s),Unwrite(ts), run_time=1)
        # self.play(FadeOut(ts))


        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.scale(1.2)
        equation.set_color_by_tex("x", TEAL_B)

        self.play(Write(equation),run_time=2)
        self.wait(2)
        self.play(Unwrite(equation))


        hola2=Text("Arigatto!")
        hola2.scale(3)
        self.play(DrawBorderThenFill(hola2),run_time=2)
        self.wait(1)
        self.play(Unwrite(hola2))




  

        
        
        