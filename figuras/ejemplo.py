"""Figura de ejemplo de la guía: los mismos datos con el estilo por omisión de matplotlib y con las
reglas de la guía. Genera antes.png y despues.png en esta carpeta.

Datos: oscilación amortiguada x(t) = exp(-t/tau) cos(2 pi t) para tres tiempos de amortiguamiento,
con la envolvente de la curva más lenta como referencia.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

AQUI = Path(__file__).parent
t = np.linspace(0, 5, 600)
TAUS = (0.5, 1.0, 2.0)


def datos(ax, colores=None, estilo_ref="-"):
    for i, tau in enumerate(TAUS):
        kw = {"color": colores[i]} if colores is not None else {}
        ax.plot(t, np.exp(-t / tau) * np.cos(2 * np.pi * t), label=f"tau = {tau}"
                if colores is None else rf"$\tau$ = {tau:g} s", **kw)
    ref = np.exp(-t / TAUS[-1])
    kw = {"color": "0.4", "lw": 1.0} if colores is not None else {}
    ax.plot(t, ref, estilo_ref, label="envolvente", **kw)
    ax.plot(t, -ref, estilo_ref, **kw)


# Antes: matplotlib tal como viene
mpl.rcdefaults()
fig, ax = plt.subplots()
datos(ax)
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.legend()
fig.savefig(AQUI / "antes.png", dpi=150)
plt.close(fig)

# Después: el punto de partida de la guía, a una columna
mpl.rcParams.update({
    "figure.figsize": (3.35, 2.4), "figure.constrained_layout.use": True,
    "savefig.dpi": 300, "savefig.bbox": "tight",
    "font.family": "serif", "mathtext.fontset": "cm", "font.size": 9,
    "axes.labelsize": 9, "legend.fontsize": 8, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "lines.linewidth": 1.3, "axes.linewidth": 0.8,
    "xtick.major.width": 0.8, "ytick.major.width": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "legend.frameon": False, "axes.grid": False,
})
colores = [mpl.colormaps["inferno"](x) for x in np.linspace(0.15, 0.75, len(TAUS))]
fig, ax = plt.subplots()
datos(ax, colores, estilo_ref="--")
ax.set(xlabel="tiempo $t$ [s]", ylabel="desplazamiento $x$ [cm]", xlim=(0, 5), ylim=(-1, 1),
       xticks=range(6), yticks=(-1, 0, 1))
ax.legend(loc="upper right", ncol=2)
fig.savefig(AQUI / "despues.png")
plt.close(fig)
print("listo")
