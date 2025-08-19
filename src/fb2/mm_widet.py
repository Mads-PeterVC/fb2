import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, interactive, VBox

V_max_max = 2
S = np.linspace(0.01, 10, 200)

def mm(S, Vmax, Km):
    return (Vmax * S) / (Km + S)

def plot_curve(Vmax, Km):

    v = mm(S, Vmax, Km)
    fig, ax  = plt.subplots(figsize=(6, 4))
    ax.plot(S, v, label=rf'$V_{{\mathrm{{max}}}}$={Vmax:.2f}, $K_m$={Km:.2f}')

    km_index = np.argmin(np.abs(S - Km))
    ax.plot([0, S[km_index]], [v[km_index], v[km_index]], linestyle='--', color='gray')
    ax.plot([S[km_index], S[km_index]], [0, v[km_index]], linestyle='--', color='gray')
    ax.axhline(Vmax, color='red', linestyle='--', label=rf'$V_{{\mathrm{{max}}}}$={Vmax:.2f}')

    ax.text(S.max()/2, Vmax+0.025, rf'$V_{{\mathrm{{max}}}} = {Vmax:.2f}$ [μM/min]', color='red', fontsize=11, ha='center', va='bottom')
    ax.text(S[km_index]+0.1, v[km_index]/2, f'$K_m$={Km:.2f} [mM]', color='gray', fontsize=11, ha='left', va='center')

    ax.set_ylim(0, V_max_max+0.2)    
    ax.set_xlim(0, S.max())
    ax.set_title('Michaelis-Menten Ligningen')
    ax.set_xlabel('Substrat koncentration [mM]')
    ax.set_ylabel('Reaktions hastighed [μM/min]')
    plt.show()

def mm_widget():

    widget = interactive(plot_curve,
                        Vmax=FloatSlider(value=1, min=0.01, max=V_max_max, step=0.01, description='Vmax'),
                        Km=FloatSlider(value=3.5, min=0.01, max=S.max(), step=0.05, description='Km'))


    output = widget.children[-1]   # the output area (plot)
    controls = VBox(widget.children[:-1])  # the sliders

    # Reorder: plot first, sliders below
    return VBox([output, controls])
