"""
LJPW Analyzer Tool

Command-line interface for the LJPW mathematical baselines and dynamic model.
"""

import sys
import argparse
from src.ljpw_baselines import LJPWBaselines, DynamicLJPWv3, NumericalEquivalents

def analyze(l, j, p, w):
    """Run static analysis."""
    print(f"Analyzing LJPW State: L={l}, J={j}, P={p}, W={w}")
    print("-" * 50)

    results = LJPWBaselines.full_diagnostic(l, j, p, w)

    metrics = results['metrics']
    print(f"Composite Score:      {metrics['composite_score']:.4f}")
    print(f"Harmony Index:        {metrics['harmony_index']:.4f}")
    print(f"Geometric Mean:       {metrics['geometric_mean']:.4f}")
    print(f"Harmonic Mean:        {metrics['harmonic_mean']:.4f}")
    print(f"Coupling-Aware Sum:   {metrics['coupling_aware_sum']:.4f}")
    print("-" * 50)

    distances = results['distances']
    print(f"Distance from Anchor: {distances['from_anchor']:.4f}")
    print(f"Distance from NE:     {distances['from_natural_equilibrium']:.4f}")

    print("-" * 50)
    eff = results['effective_dimensions']
    print("Effective Dimensions (Coupling Adjusted):")
    print(f"  L: {eff['effective_L']:.4f}")
    print(f"  J: {eff['effective_J']:.4f}")
    print(f"  P: {eff['effective_P']:.4f}")
    print(f"  W: {eff['effective_W']:.4f}")

def simulate(initial_state, duration=50, output=None):
    """Run dynamic simulation."""
    print(f"Running Simulation for {duration} time units...")
    print(f"Initial State: {initial_state}")

    sim = DynamicLJPWv3()
    history = sim.simulate(initial_state, duration=duration)

    final_state = (history['L'][-1], history['J'][-1], history['P'][-1], history['W'][-1])
    print(f"Final State:   {final_state}")

    if output:
        sim.plot_simulation(history, output_path=output)
    else:
        print("No output file specified, skipping plot.")

def main():
    parser = argparse.ArgumentParser(description="LJPW Analyzer & Simulator")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Static analysis of LJPW coordinates")
    analyze_parser.add_argument("L", type=float, help="Love coordinate")
    analyze_parser.add_argument("J", type=float, help="Justice coordinate")
    analyze_parser.add_argument("P", type=float, help="Power coordinate")
    analyze_parser.add_argument("W", type=float, help="Wisdom coordinate")

    # Simulate command
    sim_parser = subparsers.add_parser("simulate-v3", help="Run v3.0 dynamic simulation")
    sim_parser.add_argument("--L", type=float, default=0.5, help="Initial Love")
    sim_parser.add_argument("--J", type=float, default=0.5, help="Initial Justice")
    sim_parser.add_argument("--P", type=float, default=0.5, help="Initial Power")
    sim_parser.add_argument("--W", type=float, default=0.5, help="Initial Wisdom")
    sim_parser.add_argument("--duration", type=float, default=50.0, help="Simulation duration")
    sim_parser.add_argument("--output", type=str, help="Output path for plot image")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze(args.L, args.J, args.P, args.W)
    elif args.command == "simulate-v3":
        initial = (args.L, args.J, args.P, args.W)
        simulate(initial, args.duration, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
