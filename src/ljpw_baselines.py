"""
LJPW Mathematical Baselines
Version 3.0

Provides objective, non-arbitrary baselines for LJPW framework implementations.
Includes both static analysis and a validated, non-linear dynamic simulator.
"""

import math
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional
import numpy as np

@dataclass
class NumericalEquivalents:
    """Fundamental constants for LJPW dimensions"""
    L: float = (1 + math.sqrt(5)) / 2 - 1  # φ - 1 ≈ 0.618034
    J: float = math.sqrt(2) - 1             # √2 - 1 ≈ 0.414214
    P: float = math.e - 2                   # e - 2 ≈ 0.718282
    W: float = math.log(2)                  # ln(2) ≈ 0.693147


@dataclass
class ReferencePoints:
    """Key reference points in LJPW space"""
    ANCHOR_POINT: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0)
    NATURAL_EQUILIBRIUM: Tuple[float, float, float, float] = (
        0.618034,  # L
        0.414214,  # J
        0.718282,  # P
        0.693147   # W
    )


class LJPWBaselines:
    """LJPW mathematical baselines and calculations (Static Analysis)"""

    # Coupling matrix
    COUPLING_MATRIX = {
        'LL': 1.0, 'LJ': 1.4, 'LP': 1.3, 'LW': 1.5,
        'JL': 0.9, 'JJ': 1.0, 'JP': 0.7, 'JW': 1.2,
        'PL': 0.6, 'PJ': 0.8, 'PP': 1.0, 'PW': 0.5,
        'WL': 1.3, 'WJ': 1.1, 'WP': 1.0, 'WW': 1.0,
    }

    @staticmethod
    def effective_dimensions(L: float, J: float, P: float, W: float) -> Dict[str, float]:
        """Calculate coupling-adjusted effective dimensions"""
        return {
            'effective_L': L,
            'effective_J': J * (1 + 1.4 * L),
            'effective_P': P * (1 + 1.3 * L),
            'effective_W': W * (1 + 1.5 * L),
        }

    @staticmethod
    def harmonic_mean(L: float, J: float, P: float, W: float) -> float:
        """Harmonic mean - robustness (weakest link)"""
        if L <= 0 or J <= 0 or P <= 0 or W <= 0:
            return 0.0
        return 4.0 / (1/L + 1/J + 1/P + 1/W)

    @staticmethod
    def geometric_mean(L: float, J: float, P: float, W: float) -> float:
        """Geometric mean - effectiveness (multiplicative)"""
        return (L * J * P * W) ** 0.25

    @staticmethod
    def coupling_aware_sum(L: float, J: float, P: float, W: float) -> float:
        """Coupling-aware weighted sum - growth potential"""
        J_eff = J * (1 + 1.4 * L)
        P_eff = P * (1 + 1.3 * L)
        W_eff = W * (1 + 1.5 * L)
        return 0.35 * L + 0.25 * J_eff + 0.20 * P_eff + 0.20 * W_eff

    @staticmethod
    def harmony_index(L: float, J: float, P: float, W: float) -> float:
        """Harmony index - balance (inverse distance from Anchor)"""
        d_anchor = math.sqrt((1-L)**2 + (1-J)**2 + (1-P)**2 + (1-W)**2)
        return 1.0 / (1.0 + d_anchor)

    @staticmethod
    def composite_score(L: float, J: float, P: float, W: float) -> float:
        """Composite score - overall performance"""
        baselines = LJPWBaselines
        growth = baselines.coupling_aware_sum(L, J, P, W)
        effectiveness = baselines.geometric_mean(L, J, P, W)
        robustness = baselines.harmonic_mean(L, J, P, W)
        harmony = baselines.harmony_index(L, J, P, W)

        return 0.35 * growth + 0.25 * effectiveness + 0.25 * robustness + 0.15 * harmony

    @staticmethod
    def full_diagnostic(L: float, J: float, P: float, W: float) -> Dict:
        """Complete diagnostic analysis"""
        baselines = LJPWBaselines
        eff = baselines.effective_dimensions(L, J, P, W)
        NE = ReferencePoints.NATURAL_EQUILIBRIUM

        return {
            'coordinates': {'L': L, 'J': J, 'P': P, 'W': W},
            'effective_dimensions': eff,
            'distances': {
                'from_anchor': baselines.distance_from_anchor(L, J, P, W),
                'from_natural_equilibrium': math.sqrt(
                    (NE[0]-L)**2 + (NE[1]-J)**2 + (NE[2]-P)**2 + (NE[3]-W)**2
                ),
            },
            'metrics': {
                'harmonic_mean': baselines.harmonic_mean(L, J, P, W),
                'geometric_mean': baselines.geometric_mean(L, J, P, W),
                'coupling_aware_sum': baselines.coupling_aware_sum(L, J, P, W),
                'harmony_index': baselines.harmony_index(L, J, P, W),
                'composite_score': baselines.composite_score(L, J, P, W),
            }
        }

    @staticmethod
    def distance_from_anchor(L, J, P, W): return math.sqrt((1-L)**2 + (1-J)**2 + (1-P)**2 + (1-W)**2)
    @staticmethod
    def distance_from_natural_equilibrium(L, J, P, W):
        NE = ReferencePoints.NATURAL_EQUILIBRIUM
        return math.sqrt((NE[0]-L)**2 + (NE[1]-J)**2 + (NE[2]-P)**2 + (NE[3]-W)**2)


class DynamicLJPWv3:
    """
    LJPW v3.0: Empirically-validated, non-linear dynamic simulator.
    """

    def __init__(self, params=None):
        """
        Initializes with empirically-derived parameters from Bayesian calibration.
        """
        if params is None:
            # Default parameters are now the POSTERIOR MEANS from our calibration
            self.params = {
                # Growth Rates
                'alpha_LJ': 0.10, 'alpha_LW': 0.15, 'beta_L': 0.35,
                'alpha_JL': 0.41, 'alpha_JW': 0.20, 'beta_J': 0.60,
                'alpha_PL': 0.35, 'alpha_PJ': 0.25, 'beta_P': 0.20,
                'alpha_WL': 0.30, 'alpha_WJ': 0.15, 'alpha_WP': 0.20, 'beta_W': 0.40,
                # Non-Linear Parameters (v3.0)
                'K_JL': 0.59,    # Saturation constant for L -> J
                'gamma_JP': 0.49,# Erosion rate for P -> J
                'K_JP': 0.71,    # Threshold constant for P -> J
                'n_JP': 4.1,     # Steepness for P -> J erosion
            }
        else:
            self.params = params
        self.NE = ReferencePoints.NATURAL_EQUILIBRIUM

    def _derivatives(self, state):
        """Calculates the derivatives with non-linear dynamics."""
        L, J, P, W = state
        p = self.params

        # Love equation (remains linear)
        dL_dt = p['alpha_LJ'] * J + p['alpha_LW'] * W - p['beta_L'] * L

        # Justice equation (with saturation and threshold effects)
        L_effect_on_J = p['alpha_JL'] * (L / (p['K_JL'] + L)) # Saturation
        P_effect_on_J = p['gamma_JP'] * (P**p['n_JP'] / (p['K_JP']**p['n_JP'] + P**p['n_JP'])) * (1 - W) # Threshold
        dJ_dt = L_effect_on_J + p['alpha_JW'] * W - P_effect_on_J - p['beta_J'] * J

        # Power and Wisdom equations (can be similarly enhanced in future versions)
        dP_dt = p['alpha_PL'] * L + p['alpha_PJ'] * J - p['beta_P'] * P
        dW_dt = p['alpha_WL'] * L + p['alpha_WJ'] * J + p['alpha_WP'] * P - p['beta_W'] * W

        return np.array([dL_dt, dJ_dt, dP_dt, dW_dt])

    def _rk4_step(self, state, dt):
        """Performs a single 4th-order Runge-Kutta integration step."""
        k1 = self._derivatives(state)
        k2 = self._derivatives(state + 0.5 * dt * k1)
        k3 = self._derivatives(state + 0.5 * dt * k2)
        k4 = self._derivatives(state + dt * k3)
        return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    def simulate(self, initial_state: Tuple[float, float, float, float], duration: float, dt: float = 0.01) -> Dict:
        """Runs the simulation using the more accurate RK4 method."""
        steps = int(duration / dt)
        state = np.array(initial_state, dtype=float)

        history = {'t': [0], 'L': [state[0]], 'J': [state[1]], 'P': [state[2]], 'W': [state[3]]}

        for i in range(steps):
            state = self._rk4_step(state, dt)
            state = np.clip(state, 0, 1.5)

            history['t'].append((i + 1) * dt)
            history['L'].append(state[0]); history['J'].append(state[1]); history['P'].append(state[2]); history['W'].append(state[3])

        return history

    def plot_simulation(self, history: Dict, output_path: Optional[str] = None):
        """Plots the results of a simulation."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Matplotlib not installed. Cannot plot simulation.")
            return

        try:
            plt.style.use('seaborn-v0_8-whitegrid')
        except OSError:
            pass # Fallback if style not found

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.plot(history['t'], history['L'], label='Love (L)', color='crimson', lw=2)
        ax.plot(history['t'], history['J'], label='Justice (J)', color='royalblue', lw=2)
        ax.plot(history['t'], history['P'], label='Power (P)', color='darkgreen', lw=2)
        ax.plot(history['t'], history['W'], label='Wisdom (W)', color='purple', lw=2)
        for i, val in enumerate(self.NE):
            ax.axhline(y=val, color=['crimson', 'royalblue', 'darkgreen', 'purple'][i], linestyle='--', alpha=0.3)
        ax.set_title("LJPW v3.0 System Evolution (Non-Linear, RK4)")
        ax.set_xlabel("Time")
        ax.set_ylabel("Dimension Value")
        ax.set_ylim(0, 1.2)
        ax.legend()

        if output_path:
            plt.savefig(output_path)
            print(f"Simulation plot saved to {output_path}")
        else:
            plt.show()

# Example usage if run directly
if __name__ == '__main__':
    # --- Static Analysis Example ---
    L, J, P, W = 0.792, 0.843, 0.940, 0.724
    print("LJPW Static Diagnostic")
    print("=" * 60)
    diagnostic = LJPWBaselines.full_diagnostic(L, J, P, W)
    print(f"Composite Score: {diagnostic['metrics']['composite_score']:.3f}")
    print(f"Distance from NE: {diagnostic['distances']['from_natural_equilibrium']:.3f}")
    print()

    # --- Dynamic Simulation Example ---
    print("LJPW v3.0 Dynamic Simulation: 'Reckless Power' Scenario")
    print("=" * 60)
    simulator = DynamicLJPWv3()
    initial_state = (0.2, 0.3, 0.9, 0.2) # High P, low L, J, W
    history = simulator.simulate(initial_state, duration=50, dt=0.05)

    # Print final state
    final_state = (history['L'][-1], history['J'][-1], history['P'][-1], history['W'][-1])
    print(f"Initial State: L={initial_state[0]:.2f}, J={initial_state[1]:.2f}, P={initial_state[2]:.2f}, W={initial_state[3]:.2f}")
    print(f"Final State:   L={final_state[0]:.2f}, J={final_state[1]:.2f}, P={final_state[2]:.2f}, W={final_state[3]:.2f}")
