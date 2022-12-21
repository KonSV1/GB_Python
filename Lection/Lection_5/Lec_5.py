# from isOdd import isOdd
from progress1bar import ProgressBar
# import time
# import emoji
# import matplotlib.pyplot as plt
# import numpy as np






# print(isOdd(2))  # False
# print(isOdd(3))  # True


bar = FillingSquaresBar('Processing', max=20)
bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.5)
    bar.next()
bar.finish()


# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias')) # Поддержка псевдонимов
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# print(emoji.is_emoji("👍"))


# plt.style.use('_mpl-gallery-nogrid')


# # make data
# x = [2,4,6]
# colors = plt.get_cmap('YlGnBu')(np.linspace(0.2, 0.7, len(x)))

# # plot
# fig, ax = plt.subplots()
# ax.pie(x, colors=colors, radius=3, center=(4, 4),
#        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()


# x = [1, 4, 2, 4, 7, 3]
# plt.plot(x)
# plt.show()

