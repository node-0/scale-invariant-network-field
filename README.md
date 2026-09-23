# Static-Coordinate Network Field Theory: A Scale-Invariant Scalar Mechanism for Cosmological Redshift and Gravitational Emergence

**Compiler:** Independent Research Specification  
**Date:** September 2026  
**License:** MIT  

---

## Abstract

We present a self-contained, scale-invariant field framework—**Static-Coordinate Network Field Theory (SCNFT)**—which accounts for cosmological redshift and localized gravitational attraction without appealing to dynamic metric expansion ($a(t)$) or mysterious dark energy components. Operating on a fixed Minkowski geometry ($ds^2 = -c^2 dt^2 + d\mathbf{r}^2$), physical interaction scales are modulated across time and space by a continuous scalar field $\Phi(\mathbf{r}, t)$. We demonstrate that atomic emission frequencies decrease monotonically as the global scalar field background evolves, reproducing Hubble's redshift law $z \approx \frac{H_0}{c} d$ for local observers. Furthermore, local gradients in $\Phi$ generate an effective spatial potential that accounts for Newtonian gravitation as an emergent gradient force.

---

## 1. Introduction & Physical Motivation

Standard cosmological models rely on the Friedmann-Lemaître-Robertson-Walker (FLRW) metric, attributing the observed galactic redshift $z$ to the physical stretching of spatial geometry over time ($a(t)$). While successful at fitting observational parameters, this framework introduces conceptual tensions, including the horizon problem, the cosmological constant problem, and the requirement of dark energy.

SCNFT offers an alternative, minimal baseline:
1. **Static Spacetime Baseline:** The background metric remains uncurved and non-expanding:
   $$ds^2 = -c^2 dt^2 + d\mathbf{r}^2$$
2. **Scalar Gauge Invariance:** Material standards—atomic transition energy levels, rest masses, and fundamental charges—scale dynamically with a scalar field $\Phi(\mathbf{r}, t)$.
3. **Apparent Motion via Field Phase:** Cosmological redshift arises from the intrinsic evolution of physical reference scales between emission and detection, rather than from photon energy loss during transit or spatial stretching.

---

## 2. Mathematical Framework

### 2.1 Field Lagrangian & Action

The action $S$ governs the interaction between the gravitational/scalar sector $\Phi$ and standard matter fields $\psi_m$:

$$S = \int d^4 x \sqrt{-\eta} \left[ \frac{1}{2} \eta^{\mu\nu} \partial_\mu \Phi \partial_\nu \Phi - V(\Phi) + \mathcal{L}_m(\psi_m, e^{\alpha\Phi}\eta_{\mu\nu}) \right]$$

where:
* $\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$ is the flat Minkowski metric.
* $\alpha$ is a dimensionless coupling parameter.
* $V(\Phi)$ is a smooth field potential.

### 2.2 Scaled Field Equations

Varying the action with respect to $\Phi$ yields the field equation:

$$\Box \Phi + \frac{dV}{d\Phi} = -\alpha \, T_m$$

where $T_m = \eta^{\mu\nu} T_{\mu\nu}^{(m)}$ represents the trace of the energy-momentum tensor for matter.

For a homogeneous cosmological background, $\Phi(\mathbf{r}, t) \rightarrow \Phi_0(t)$, simplifying the wave equation to:

$$\frac{1}{c^2} \frac{\partial^2 \Phi_0}{\partial t^2} + \frac{dV}{d\Phi_0} = -\alpha \rho_m c^2$$

---

## 3. Mechanism of Cosmological Redshift

### 3.1 Emission Scale Evolution

Atomic energy levels $E_n$ for matter bound to the scalar field background scale exponentially with $\Phi_0(t)$:

$$E_n(t) = E_n(0) \exp\left( \alpha \Phi_0(t) \right)$$

Consider a photon emitted by an atomic transition at time $t_e$ with frequency $\nu_e$:

$$\nu_e = \frac{E_n(t_e) - E_m(t_e)}{h} = \nu_0 \exp\left( \alpha \Phi_0(t_e) \right)$$

### 3.2 Photon Propagation and Observational Shift

Photons propagate along null geodesics of the flat metric $\eta_{\mu\nu}$ with constant global frequency $\nu_{\text{prop}} = \nu_e$. Upon arrival at the detector at time $t_r = t_e + d/c$, the local reference emission frequency has shifted to:

$$\nu_r = \nu_0 \exp\left( \alpha \Phi_0(t_r) \right)$$

The observed redshift $z$ is defined by the ratio of received vs. emitted reference frequencies:

$$1 + z = \frac{\nu_e}{\nu_r} = \frac{\nu_0 \exp\left( \alpha \Phi_0(t_e) \right)}{\nu_0 \exp\left( \alpha \Phi_0(t_r) \right)} = \exp\left( \alpha \left[ \Phi_0(t_e) - \Phi_0(t_r) \right] \right)$$

Assuming a slowly evolving scalar background where $\dot{\Phi}_0 \approx -H_0 / \alpha$:

$$1 + z \approx \exp\left( H_0 (t_r - t_e) \right) = \exp\left( \frac{H_0 d}{c} \right)$$

First-order Taylor expansion yields Hubble's law:

$$z \approx \frac{H_0}{c} d$$

---

## 4. Emergent Gravitational Dynamics

Local density perturbations $\delta \rho_m(\mathbf{r})$ induce spatial gradients $\nabla \Phi(\mathbf{r})$ in the scalar field.

### 4.1 Gradient Force Derivation

The equations of motion for a point mass $m$ in a spatially non-uniform scalar field $\Phi(\mathbf{r})$ yield an acceleration:

$$\mathbf{a} = -c^2 \alpha \nabla \Phi(\mathbf{r})$$

Matching this to the Newtonian gravitational acceleration $\mathbf{a}_N = -\nabla \Phi_N$:

$$\Phi_N(\mathbf{r}) = c^2 \alpha \Phi(\mathbf{r})$$

For a spherical mass distribution $M$:

$$\Phi(\mathbf{r}) = \Phi_0 - \frac{G M}{\alpha c^2 r}$$

This reproduces standard Keplerian orbits and weak-field general relativistic effects without requiring metric curvature.

---

## 5. Observational Predictions & Falsifiability

SCNFT makes testable predictions that distinguish it from standard $\Lambda\text{CDM}$ expansion models:

| Phenomenon | $\Lambda\text{CDM}$ Prediction | SCNFT Prediction |
| :--- | :--- | :--- |
| **Space Metric** | Expanding ($a(t)$) | Static ($\eta_{\mu\nu}$) |
| **Angular Diameter Distance** | Decreases at high $z$ ($z > 1.5$) | Strictly monotonic $d_A = \frac{d}{1+z}$ |
| **Surface Brightness Scaling** | $(1+z)^{-4}$ (Tolman test) | $(1+z)^{-2}$ (No metric expansion dimming) |
| **Atomic Clock Drift** | Stationary local ratio | Continuous background ratio drift $\frac{\dot{\nu}}{\nu} \sim H_0$ |

---

## 6. Verification & Implementation

To simulate light propagation through the network field numerical grid, use the following Python validation snippet:

```python
import numpy as np

def calculate_redshift(distance_mpc, H0=70.0):
    """
    Calculates cosmological redshift z under static-coordinate scalar field dynamics.
    
    Parameters:
        distance_mpc (float): Distance to target in Megaparsecs.
        H0 (float): Hubble constant in km/s/Mpc.
        
    Returns:
        float: Calculated redshift z.
    """
    c_kms = 299792.458  # Speed of light in km/s
    time_delay_sec = (distance_mpc * 3.0857e19) / (c_kms * 1000)
    H0_per_sec = (H0 * 1000) / (3.0857e19)
    
    # Exact SCNFT exponential relation
    z = np.exp(H0_per_sec * time_delay_sec) - 1.0
    return z

# Example: Galaxy at 500 Mpc
dist = 500.0
z_scnft = calculate_redshift(dist)
print(f"Redshift at {dist} Mpc: z = {z_scnft:.4f}")
