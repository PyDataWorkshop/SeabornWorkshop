%-- http://www.stanford.edu/~mwaskom/software/seaborn/aesthetics.html

sns.regplot(*np.random.randn(2, 100))
main, x_marg, y_marg = plt.gcf().axes

sns.despine(ax=main)
sns.despine(ax=x_marg, left=True)
sns.despine(ax=y_marg, bottom=True)
