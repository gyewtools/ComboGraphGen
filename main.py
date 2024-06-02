import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np

plt.style.use('dark_background')
sns.set_theme(style="darkgrid")

file_path = 'emails.txt'

with open(file_path, 'r') as file:
    emails = file.readlines()

domains = []
for email in emails:
    try:
        domain = email.split('@')[1].split(':')[0]
        domains.append(domain)
    except IndexError:
        continue

domain_counts = Counter(domains)
sorted_domain_counts = domain_counts.most_common()

fig, ax = plt.subplots(figsize=(14, 10))
domains, counts = zip(*sorted_domain_counts)

colors = plt.cm.viridis(np.linspace(0, 1, len(domains)))

ax.barh(domains, counts, color=colors)
ax.set_xlabel('Number of Emails', fontsize=16, color='white', labelpad=15)
ax.set_ylabel('Email Domains', fontsize=16, color='white', labelpad=15)
ax.set_title('Combo graph', fontsize=20, color='white', pad=20)
ax.grid(axis='x', linestyle='--', alpha=0.7)

for index, value in enumerate(counts):
    ax.text(value, index, str(value), va='center', fontsize=12, color='black', fontweight='bold')

plt.figtext(0.5, 0.95, 'Gyews combo graph', ha='center', fontsize=26, color='black', fontweight='bold')
plt.figtext(0.5, 0.02, 'discord.gg/silentgen', ha='center', fontsize=16, color='cyan', fontweight='bold')

plt.tight_layout(pad=2.0)
output_path = 'image.png'
plt.savefig(output_path, facecolor=fig.get_facecolor())
plt.show()
