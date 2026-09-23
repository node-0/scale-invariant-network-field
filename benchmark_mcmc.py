import numpy as np
import matplotlib.pyplot as plt
import emcee
from astropy.constants import c
import astropy.units as u

# Set publication-quality plot style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# -----------------------------------------------------------------------------
# 1. DESI BAO Observational Data Points (z_eff, dA in Mpc, err in Mpc)
# Compiled from DESI Y1 BAO tracer releases
# -----------------------------------------------------------------------------
desi_bao_data = np.array([
    [0.150, 520.4, 15.2],   # BGS tracer
    [0.380, 1085.1, 22.4],  # LRG1 tracer
    [0.510, 1282.6, 25.1],  # LRG2 tracer
    [0.706, 1512.3, 28.5],  # LRG3 + ELG1 tracer
    [0.930, 1630.5, 31.8],  # ELG2 tracer
    [1.318, 1720.1, 42.6],  # QSO tracer
    [2.330, 1610.8, 55.4]   # Lyman-alpha forest tracer
])

z_obs = desi_bao_data[:, 0]
dA_obs = desi_bao_data[:, 1]
dA_err = desi_bao_data[:, 2]

# Speed of light in km/s
C_KMS = c.to(u.km / u.s).value

# -----------------------------------------------------------------------------
# 2. SCNFT Angular Diameter Distance Model
# -----------------------------------------------------------------------------
def scnft_dA(z, H0):
    """
    SCNFT Angular Diameter Distance d_A(z) on a static coordinate grid.
    d_A(z) = (c / H0) * ln(1+z) / (1+z)
    """
    return (C_KMS / H0) * np.log(1.0 + z) / (1.0 + z)

# -----------------------------------------------------------------------------
# 3. MCMC Probability Functions (Log-Prior, Log-Likelihood, Log-Posterior)
# -----------------------------------------------------------------------------
def log_prior(theta):
    """
    Flat uninformative prior on H0 in the range [40, 100] km/s/Mpc.
    """
    H0 = theta[0]
    if 40.0 < H0 < 100.0:
        return 0.0
    return -np.inf

def log_likelihood(theta, z, y, yerr):
    """
    Gaussian log-likelihood for the observational data points.
    """
    H0 = theta[0]
    model = scnft_dA(z, H0)
    sigma2 = yerr**2
    return -0.5 * np.sum((y - model)**2 / sigma2 + np.log(2.0 * np.pi * sigma2))

def log_probability(theta, z, y, yerr):
    """
    Log-posterior probability: Log-Prior + Log-Likelihood
    """
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, z, y, yerr)

# -----------------------------------------------------------------------------
# 4. MCMC Ensemble Sampler Execution
# -----------------------------------------------------------------------------
ndim = 1            # Single free parameter: H0
nwalkers = 32       # Number of ensemble walkers
nsteps = 3000       # Total steps per walker
burn_in = 500       # Burn-in steps to discard

# Initialize walker positions centered around an initial guess H0 = 70.0 km/s/Mpc
initial_pos = np.array([70.0]) + 1.0 * np.random.randn(nwalkers, ndim)

# Construct sampler
sampler = emcee.EnsembleSampler(
    nwalkers, ndim, log_probability, args=(z_obs, dA_obs, dA_err)
)

print(f"Running MCMC sampling with {nwalkers} walkers for {nsteps} steps...")
sampler.run_mcmc(initial_pos, nsteps, progress=True)

# Discard burn-in phase and flatten MCMC chains
flat_samples = sampler.get_chain(discard=burn_in, flat=True)

# -----------------------------------------------------------------------------
# 5. Parameter Estimation & Confidence Intervals
# -----------------------------------------------------------------------------
h0_mcmc = np.percentile(flat_samples[:, 0], [16, 50, 84])
h0_median = h0_mcmc[1]
h0_minus = h0_median - h0_mcmc[0]
h0_plus = h0_mcmc[2] - h0_median

print("\n" + "=" * 55)
print("             MCMC H0 PARAMETER ESTIMATION RESULTS")
print("=" * 55)
print(f"Best-Fit H0 (Median):   {h0_median:.2f} km/s/Mpc")
print(f"16th Percentile (-1σ):  {h0_mcmc[0]:.2f} km/s/Mpc")
print(f"84th Percentile (+1σ):  {h0_mcmc[2]:.2f} km/s/Mpc")
print(f"Final MCMC Result:      H0 = {h0_median:.2f} (+{h0_plus:.2f} / -{h0_minus:.2f}) km/s/Mpc")
print("-" * 55)

# Calculate Chi-Squared at MCMC median H0
dA_fit = scnft_dA(z_obs, h0_median)
chi2 = np.sum(((dA_obs - dA_fit) / dA_err)**2)
dof = len(z_obs) - 1
print(f"Chi-Squared (χ²):       {chi2:.3f}")
print(f"Reduced Chi-Squared:     {chi2 / dof:.3f}")
print("=" * 55)

# -----------------------------------------------------------------------------
# 6. Visualization: Posterior PDF & Distance Curve with Uncertainty Band
# -----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Panel 1: Posterior Probability Density Function for H0
ax1.hist(flat_samples[:, 0], bins=40, density=True, color='crimson', alpha=0.7, edgecolor='black')
ax1.axvline(h0_median, color='black', linestyle='-', linewidth=2, label=f'Median H0 = {h0_median:.2f}')
ax1.axvline(h0_mcmc[0], color='black', linestyle='--', linewidth=1.5, label=f'-1σ ({h0_mcmc[0]:.2f})')
ax1.axvline(h0_mcmc[2], color='black', linestyle='--', linewidth=1.5, label=f'+1σ ({h0_mcmc[2]:.2f})')
ax1.set_xlabel(r'$H_0$ [km/s/Mpc]', fontsize=12)
ax1.set_ylabel(r'Probability Density', fontsize=12)
ax1.set_title(r'SCNFT $H_0$ Posterior Distribution (MCMC)', fontsize=13, fontweight='bold')
ax1.legend(frameon=True, facecolor='white', fontsize=10)
ax1.grid(True, linestyle=':', alpha=0.6)

# Panel 2: Best-Fit Angular Diameter Distance Curve with 68% Confidence Band
z_grid = np.linspace(0.01, 2.6, 300)
dA_grid_best = scnft_dA(z_grid, h0_median)
dA_grid_upper = scnft_dA(z_grid, h0_mcmc[0])  # Lower H0 yields higher distance
dA_grid_lower = scnft_dA(z_grid, h0_mcmc[2])  # Higher H0 yields lower distance

ax2.errorbar(z_obs, dA_obs, yerr=dA_err, fmt='o', color='black', ecolor='gray',
             capsize=4, elinewidth=1.5, label='DESI BAO Data Points', zorder=5)
ax2.plot(z_grid, dA_grid_best, color='crimson', linewidth=2.2,
         label=f'SCNFT MCMC Best-Fit ($H_0={h0_median:.2f}$)')
ax2.fill_between(z_grid, dA_grid_lower, dA_grid_upper, color='crimson', alpha=0.25,
                 label=r'68% Confidence Band ($1\sigma$)')

ax2.set_xlabel(r'Redshift $z$', fontsize=12)
ax2.set_ylabel(r'Angular Diameter Distance $d_A(z)$ [Mpc]', fontsize=12)
ax2.set_title(r'SCNFT $d_A(z)$ Fit to DESI BAO Data', fontsize=13, fontweight='bold')
ax2.legend(frameon=True, facecolor='white', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
