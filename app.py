from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    # Create the plot
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend_label="Line", line_width=2)
    script, div = components(p)
    cdn_js = CDN.js_files[0]

    return render_template('index.html',cdn_js=cdn_js,script=script,div=div)
if __name__=="__main__":
    app.run(host="0.0.0.0")