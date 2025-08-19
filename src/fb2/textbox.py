def add_textbox(ax, a=None, b=None, V_max=None, K_m=None, mse=None):
    """
    Laver en tekstboks i et matplotlib-plot med information om hældning, skæringspunkt, V_max, K_m og MSE.    
    """
    textbox = ''
    textbox += f'Hældning: {a:.2f}\n' if a is not None else ''
    textbox += f'Skæringspunkt: {b:.2f}\n' if b is not None else ''
    textbox += rf'$V_\mathrm{{max}}$: {V_max:.2f} [μM/min]' + '\n' if V_max is not None else ''
    textbox += f'$K_m$: {K_m:.2f} [mM]\n' if K_m is not None else ''
    textbox += f'MSE: {mse:.1e}\n' if mse is not None else ''
    ax.text(0.05, 0.95, textbox, transform=ax.transAxes, va='top')
