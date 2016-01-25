sample = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=100)
pal = sns.dark_palette("palegreen", as_cmap=True)
plt.figure(figsize=(6, 6))
sns.kdeplot(sample, cmap=pal);
