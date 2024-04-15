from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# parameter names of the statistics we want to show
params = [
    "Data",
    "Facilities",
    "Operations",
    "Philosophy",
    "H&P",
    "Ind Development",
    "Organisation",
    "People",
    "Player Care",
    "Practice",
    "Staffing",
    "Strategy",
    "Talent ID",
    "Team Development",
    "Transition 1st Team"
]


# The lower and upper boundaries for the statistics
low = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
high = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# Add anything to this list where having a lower number is better
# this flips the statistic
lower_is_better = ['Miscontrol']


radar = Radar(params, low, high,
              lower_is_better=lower_is_better,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*len(params),
              num_rings=3,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)



unkown = [0.89, 0.55, 0.54, 0.81, 0.39, 0.47, 0.55, 0.47, 0.33, 0.56, 0.92, 0.55, 0.19, 0.4, 0.21]






average = [
    0.778911607, 0.802803393, 0.351289679, 0.757135786, 0.700314143, 0.643409571, 0.559844893,
    0.44153125, 0.527084286, 0.645216321, 0.8973685, 0.548156143, 0.577573429, 0.782038821,
    0.369866061
]

max_values = [
    0.990741, 0.97092, 0.553704, 0.932751, 0.921296, 0.974248, 0.814691, 0.639881,
    0.758095, 0.867553, 0.99, 0.840083, 0.801347, 0.940909, 0.65625
]

# creating the figure using the grid function from mplsoccer:
fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                title_space=0, endnote_space=0, grid_key='radar', axis=False)

# plot radar
radar.setup_axis(ax=axs['radar'])  # format axis as a radar
rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='white', edgecolor='white')
radar_output = radar.draw_radar_compare(unkown, average, ax=axs['radar'],
                                        kwargs_radar={'facecolor': '#B49A36', 'alpha': 0.6},
                                        kwargs_compare={'facecolor': 'grey', 'alpha': 0.4})
radar_poly, radar_poly2, vertices1, vertices2 = radar_output
range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=10,alpha = 0.6)
param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=12)



axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                     c='#B49A36', edgecolors='black', marker='o', s=100, zorder=2)
axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                     c='grey', edgecolors='black', marker='o', s=100, zorder=2)


# adding the endnote and title text (these axes range from 0-1, i.e. 0, 0 is the bottom left)
# Note we are slightly offsetting the text from the edges by 0.01 (1%, e.g. 0.99)
endnote_text = axs['endnote'].text(0.99, 0.5, "Unknown FA Evaluation", fontsize=15, ha='right', va='center')
title1_text = axs['title'].text(0.01, 0.65, 'Unknown FC', fontsize=25,fontproperties='robotto_bold.prop', color='#B49A36', ha='left', va='center')
title2_text = axs['title'].text(0.01, 0.25, 'Values Per Category', fontsize=20,ha='left', va='center', color='#B49A36')
title3_text = axs['title'].text(0.99, 0.65, 'All Teams', fontsize=25,ha='right', va='center', color='grey')
title4_text = axs['title'].text(0.99, 0.25, 'Average Values', fontsize=20,ha='right', va='center', color='grey')


plt.show()
#plt.savefig('hungary.png',bbox_inches='tight')