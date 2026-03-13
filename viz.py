import matplotlib.pyplot as plt
import numpy as np

# יצירת נתונים לדוגמה לגרף
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.title("דוגמה לגרף")
plt.xlabel("ערך X")
plt.ylabel("ערך Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()