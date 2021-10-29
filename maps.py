import osmnx as ox

print("Enter your City to map out: ")
City = input()
print("Enter your Country to map out: ")
Country = input()

place = [City, Country]
G = ox.graph_from_place(place, retain_all=True,
                        simplify=True, network_type='all')

###############################################################################
#                           Unpacking the Data                                #
###############################################################################
u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)

# Lists to store colors and widths
roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#d40a47"

        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            color = "#e78119"

        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            color = "#30bab0"

        elif item["length"] > 400 and item["length"] <= 800:
            color = "#bbbbbb"
            linewidth = 0.35
        else:
            color = "#d5d5d5"
            linewidth = 0.45

        if "primary" in item["highway"]:
            linewidth = 0.5
            color = "#ffff"
    else:
        color = "#a6a6a6"
        linewidth = 0.10

    roadColors.append(color)
    roadWidths.append(linewidth)

for item in data:
    if "footway" in item["highway"]:
        color = "#ededed"
        linewidth = 0.5
    else:
        color = "#a6a6a6"
        linewidth = 0.5

    roadWidths.append(linewidth)

bgcolor = "#061529"

#Load and save the image
fig, ax = ox.plot_graph(G, node_size=0, figsize=(27, 30),
                        dpi=300, bgcolor=bgcolor,
                        save=False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("Figure1.png", dpi=300, format="png", bbox_inches='tight',
            facecolor=fig.get_facecolor(), transparent=False)
