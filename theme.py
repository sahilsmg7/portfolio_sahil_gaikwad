import re

path = 'c:/Users/sahil/Anti-Gravity/Youtube Workspace/portfolio_sahil_gaikwad/style.css'
with open(path, 'r') as f:
    css = f.read()

# Background & text
css = css.replace("background: lavenderblush;", "background: #f4f6fb;")
css = css.replace("background: #051129;", "background: #ffffff;\n    box-shadow: 0 2px 10px rgba(0,0,0,0.05);")
css = css.replace("color: white;", "color: #1a1a1a;")
css = css.replace("color: #fff;", "color: #1a1a1a;")
css = css.replace("color: aliceblue;", "color: #444444;")
css = css.replace("color: orangered;", "color: #0056b3;")

# Accents
css = css.replace("color:#0ef;", "color: #0056b3;")
css = css.replace("color: #0ef;", "color: #0056b3;")
css = css.replace("border: 2px solid #0ef;", "border: 2px solid #e0e0e0;\n    background: #ffffff;")
css = css.replace("background: #0ef;", "background: #0056b3;")
css = css.replace("color: #081b29;", "color: #ffffff;")
css = css.replace("color: #001b29;", "color: #ffffff;")

# Form & Shadows
css = css.replace("background: #555557;", "background: #ffffff;\n    border: 1px solid #ddd;")
css = css.replace("box-shadow: 1px 1px 20px #012290f7,\n                1px 1px 40px #0053b8f7;", "box-shadow: 0 10px 30px rgba(0,0,0,0.05);\n    background: #ffffff;")
css = css.replace("background-color: #0ef;", "background-color: #0056b3;")
css = css.replace("stroke: #0ef;", "stroke: #0056b3;")
css = css.replace("stroke: black;", "stroke: #e0e0e0;")
css = css.replace("background: linear-gradient(rgba(0,0,0,0.1),#0ef);", "background: linear-gradient(rgba(244,246,251,0.9), rgba(255,255,255,1));")
css = css.replace("color: #ff004f;", "color: #0056b3;")
css = css.replace("background: rgb(7, 85, 91);", "background: #ffffff;\n    border-top: 1px solid #e0e0e0;")

# Remove neon glow shadows
css = re.sub(r'box-shadow: 0 0 5px #0ef,\s*0 0 25px #0ef;', 'box-shadow: 0 4px 10px rgba(0,86,179,0.2);', css)
css = re.sub(r'box-shadow: 0 0 5px cyan,[^;]+;', 'box-shadow: 0 6px 15px rgba(0,86,179,0.3);', css)
css = re.sub(r'box-shadow: 0 0 20px #0ef;', 'box-shadow: 0 6px 15px rgba(0,86,179,0.3);', css)

# Fix placeholder
css = css.replace("::placeholder\n{\n    color: white;\n}", "::placeholder\n{\n    color: #888;\n}")

# Layer text overrides for new light background
css = css.replace(".layer h5{\n    color: #000;", ".layer h5{\n    color: #0056b3;")
css = css.replace(".layer p{\n    color: #000;", ".layer p{\n    color: #333;")

with open(path, 'w') as f:
    f.write(css)

# Also fix the index.html inline styles for the new theme
html_path = 'c:/Users/sahil/Anti-Gravity/Youtube Workspace/portfolio_sahil_gaikwad/index.html'
with open(html_path, 'r') as f:
    html = f.read()

html = html.replace('style="color: white;"', 'style="color: #1a1a1a;"')
html = html.replace('color: rgb(228, 228, 228);', 'color: #333;')
html = html.replace('color: rgb(177, 177, 177);', 'color: #666;')
html = html.replace('<h4 style="color: black;">Full Stack Developer!</h4>', '<h4 style="color: #0056b3;">Full Stack Developer!</h4>')

with open(html_path, 'w') as f:
    f.write(html)
