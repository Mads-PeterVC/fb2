import numpy as np
import pandas as pd

data = pd.read_csv('combined_data.txt', sep='\t') # Læser data fra en tab-separeret fil

substrate = data['Substrate_Concentration']  # Substrat koncentration
velocity = data['Reaction_Velocity']  # Reaktions hastighed

# Add Gaussian noise
noise_level = 0.05  # Juster støjniveauet her
noisy_velocity = velocity + np.random.normal(0, noise_level, len(velocity))

# Opretter en DataFrame med støjende data
noisy_data = pd.DataFrame({
    'Substrate_Concentration': substrate,
    'Reaction_Velocity': noisy_velocity,
    'Inverse_Substrate': 1 / substrate,
    'Inverse_Velocity': 1 / noisy_velocity
})

# Save the noisy data to a new file
noisy_data.to_csv('noisy_combined_data.txt', sep='\t', index=False)

