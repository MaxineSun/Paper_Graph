import networkx as nx
from bokeh.io import output_file, show
from bokeh.models import Circle, HoverTool, MultiLine, Plot, Range1d
from bokeh.plotting import from_networkx
from bokeh.models import NodesAndLinkedEdges


class Visualize():
    def __init__(self, G):
        self.graph = G

    def Visualize_graph(self):
        plot = Plot(plot_width=870,
                    x_range=Range1d(-1.1, 1.1),
                    plot_height=530,
                    y_range=Range1d(-1.1, 1.1))

        plot.title.text = "digCon"
        plot.outline_line_color = None
        plot.toolbar.logo = None
        node_highlight_color = 'white'
        edge_highlight_color = 'black'

        # pdoi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, issn, isbn, loc, url, edt, anm
        node_hover_tool = HoverTool(tooltips=[("doi", "@index"),
                                              ("title", "@tit"),
                                              ("author", "@aut"),
                                              ("type","@typ"),
                                              ("journal", "@jnl"),
                                              ("issue", "@iss"),
                                              ("year", "@ymd"),
                                              ("volume", "@vol")],
                                    show_arrow=False)

        plot.add_tools(node_hover_tool)

        graph_renderer = from_networkx(self.graph.Graph,
                                       nx.spring_layout,
                                       scale=1,
                                       center=(0, 0))

        graph_renderer.node_renderer.glyph = Circle(size=15,
                                                    fill_color='skyblue',
                                                    line_color='black')

        graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color",
                                                       line_alpha=0.2,
                                                       line_width=1)

        # Set node highlight colors
        graph_renderer.node_renderer.hover_glyph = Circle(size=2,
                                                          fill_color=node_highlight_color,
                                                          line_width=2)
        graph_renderer.node_renderer.selection_glyph = Circle(size=2,
                                                              fill_color=node_highlight_color,
                                                              line_width=2)

        # Set edge highlight colors
        graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=edge_highlight_color,
                                                                 line_width=2)
        graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=edge_highlight_color,
                                                             line_width=2)

        # Highlight nodes and edges
        graph_renderer.selection_policy = NodesAndLinkedEdges()
        graph_renderer.inspection_policy = NodesAndLinkedEdges()

        plot.renderers.append(graph_renderer)
        output_file("digCon.html")
        show(plot)

        from bokeh.io import export_svgs

        plot.output_backend = "svg"
        export_svgs(plot, filename="plot.svg")