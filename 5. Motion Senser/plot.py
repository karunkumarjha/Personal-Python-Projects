from motion import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["StartString"] = df["Start"].dt.strftime("%Y-%m-%d %H-%M-%S")
df["EndString"] = df["End"].dt.strftime("%Y-%m-%d %H-%M-%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 300, width = 1000, title = "Motion Detector")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips = [("Start:", "@StartString"), ("End", "@EndString")])
p.add_tools(hover)
q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = 'green', source = cds)

output_file("Graph.html")
show(p) 