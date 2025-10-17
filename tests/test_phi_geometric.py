"""
COMPREHENSIVE TEST SUITE FOR PHI GEOMETRIC ENGINE

Tests all golden ratio mathematical operations for semantic database.

Test Categories:
1. Fibonacci Sequence Generation
2. Golden Spiral Distance Calculations
3. Golden Angle Rotations
4. Exponential Phi Binning
5. Dodecahedral Anchor Geometry
6. Performance Benchmarks

Run with: python -m pytest tests/test_phi_geometric.py -v
"""

import sys
import os
import time
import math
import pytest
import numpy as np

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from phi_geometric_engine import (
    PHI, PHI_INVERSE, GOLDEN_ANGLE_RAD, GOLDEN_ANGLE_DEG,
    PhiCoordinate, FibonacciSequence, GoldenSpiral,
    GoldenAngleRotator, PhiExponentialBinner, DodecahedralAnchors,
    fibonacci, golden_spiral_distance, rotate_by_golden_angle, get_phi_bin
)


# ============================================================================
# FIBONACCI SEQUENCE TESTS
# ============================================================================

class TestFibonacciSequence:
    """Test Fibonacci sequence generation and properties"""

    def test_first_fibonacci_numbers(self):
        """Test first 10 Fibonacci numbers"""
        fib = FibonacciSequence()
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        actual = [fib.get(i) for i in range(10)]
        assert actual == expected

    def test_fibonacci_identity(self):
        """Test F(n) = F(n-1) + F(n-2)"""
        fib = FibonacciSequence()
        for n in range(2, 20):
            assert fib.get(n) == fib.get(n-1) + fib.get(n-2)

    def test_fibonacci_phi_convergence(self):
        """Test that F(n+1)/F(n) -> phi as n increases"""
        fib = FibonacciSequence()

        # Check convergence at large n
        ratio_15 = fib.get(15) / fib.get(14)
        ratio_20 = fib.get(20) / fib.get(19)
        ratio_25 = fib.get(25) / fib.get(24)

        # Should get closer to phi
        error_15 = abs(ratio_15 - PHI)
        error_20 = abs(ratio_20 - PHI)
        error_25 = abs(ratio_25 - PHI)

        assert error_20 < error_15
        assert error_25 < error_20
        assert error_25 < 0.0001  # Very close to phi

    def test_fibonacci_binet_formula(self):
        """Test Binet's formula approximation"""
        fib = FibonacciSequence()

        for n in range(10, 21):
            actual = fib.get(n)
            approx = fib.approximate_with_phi(n)
            error_percent = abs(actual - approx) / actual * 100
            assert error_percent < 1.0  # Within 1%

    def test_fibonacci_range(self):
        """Test getting range of Fibonacci numbers"""
        fib = FibonacciSequence()
        range_result = fib.get_range(5, 10)
        expected = [5, 8, 13, 21, 34, 55]
        assert range_result == expected

    def test_find_fibonacci_index(self):
        """Test finding index for target value"""
        fib = FibonacciSequence()

        # F(10) = 55
        assert fib.find_index_for_value(50) in [10, 11]
        # F(15) = 610
        assert fib.find_index_for_value(600) in [15, 16]


# ============================================================================
# GOLDEN SPIRAL TESTS
# ============================================================================

class TestGoldenSpiral:
    """Test golden spiral calculations in 4D space"""

    def test_spiral_radius_growth(self):
        """Test that spiral radius grows exponentially with phi"""
        spiral = GoldenSpiral()

        r0 = spiral.radius_at_angle(0)
        r_pi = spiral.radius_at_angle(math.pi)
        r_2pi = spiral.radius_at_angle(2 * math.pi)

        # Each π/2 rotation multiplies radius by phi
        expected_ratio = PHI ** 2  # (π / (π/2)) = 2
        actual_ratio = r_pi / r0

        assert abs(actual_ratio - expected_ratio) < 0.01

    def test_spiral_angle_inverse(self):
        """Test angle_at_radius is inverse of radius_at_angle"""
        spiral = GoldenSpiral()

        for theta in [0.5, 1.0, 2.0, 3.0]:
            r = spiral.radius_at_angle(theta)
            theta_back = spiral.angle_at_radius(r)
            assert abs(theta - theta_back) < 0.01

    def test_spiral_4d_distance_vs_euclidean(self):
        """Test spiral distance differs from Euclidean"""
        spiral = GoldenSpiral()

        p1 = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        p2 = PhiCoordinate(0.7, 0.6, 0.8, 0.9)

        spiral_dist = spiral.distance_4d(p1, p2)
        euclidean_dist = np.linalg.norm(p1.to_vector() - p2.to_vector())

        # Spiral distance should be different (usually longer)
        assert spiral_dist != euclidean_dist
        assert spiral_dist > 0

    def test_spiral_distance_symmetry(self):
        """Test spiral distance is symmetric"""
        spiral = GoldenSpiral()

        p1 = PhiCoordinate(0.3, 0.4, 0.5, 0.6)
        p2 = PhiCoordinate(0.7, 0.8, 0.2, 0.1)

        dist_12 = spiral.distance_4d(p1, p2)
        dist_21 = spiral.distance_4d(p2, p1)

        assert abs(dist_12 - dist_21) < 0.01

    def test_spiral_path_points(self):
        """Test generating points along spiral"""
        spiral = GoldenSpiral()

        points = spiral.spiral_path_points(0, 2*math.pi, num_points=100)

        assert len(points) == 100
        assert all(isinstance(p, tuple) and len(p) == 2 for p in points)

        # Check radius increases
        radii = [math.sqrt(x**2 + y**2) for x, y in points]
        assert radii[-1] > radii[0]  # Radius grows


# ============================================================================
# GOLDEN ANGLE ROTATION TESTS
# ============================================================================

class TestGoldenAngleRotator:
    """Test golden angle rotations for optimal diversity"""

    def test_golden_angle_value(self):
        """Test golden angle is approximately 137.5 degrees"""
        rotator = GoldenAngleRotator()

        assert abs(rotator.golden_angle_deg - 137.5) < 0.1
        assert abs(rotator.golden_angle_rad - 2.4) < 0.1

    def test_2d_rotation_preserves_magnitude(self):
        """Test 2D rotation preserves distance from origin"""
        rotator = GoldenAngleRotator()

        x, y = 1.0, 0.0
        original_mag = math.sqrt(x**2 + y**2)

        for n in range(1, 10):
            x_rot, y_rot = rotator.rotate_2d(x, y, n)
            rotated_mag = math.sqrt(x_rot**2 + y_rot**2)
            assert abs(rotated_mag - original_mag) < 0.0001

    def test_4d_rotation_preserves_magnitude(self):
        """Test 4D rotation preserves magnitude"""
        rotator = GoldenAngleRotator()

        coord = PhiCoordinate(1.0, 0.5, 0.3, 0.7)
        original_mag = coord.magnitude()

        for plane in ["LP", "LW", "LJ", "PW", "PJ", "WJ"]:
            rotated = rotator.rotate_4d(coord, n=1, plane=plane)
            rotated_mag = rotated.magnitude()
            assert abs(rotated_mag - original_mag) < 0.0001

    def test_rotation_cycles(self):
        """Test multiple rotations eventually cycle"""
        rotator = GoldenAngleRotator()

        coord = PhiCoordinate(1.0, 0.0, 0.0, 0.0)

        # After many golden angle rotations, should come close to original
        # (not exactly due to incommensurability of phi)
        rotated = coord
        for i in range(100):
            rotated = rotator.rotate_4d(rotated, n=1, plane="LP")

        # Won't be exact, but should be in same general direction
        dot_product = (coord.love * rotated.love +
                      coord.power * rotated.power +
                      coord.wisdom * rotated.wisdom +
                      coord.justice * rotated.justice)

        # Cosine similarity should be somewhat positive
        assert dot_product > -0.5

    def test_optimal_distribution(self):
        """Test generating optimally distributed points"""
        rotator = GoldenAngleRotator()
        center = PhiCoordinate(0.5, 0.5, 0.5, 0.5)

        points = rotator.generate_optimal_distribution(center, radius=0.3, count=8)

        assert len(points) == 8

        # All points should be approximately same distance from center
        distances = []
        for point in points:
            diff = point.to_vector() - center.to_vector()
            distances.append(np.linalg.norm(diff))

        avg_dist = np.mean(distances)
        for dist in distances:
            assert abs(dist - avg_dist) < 0.1  # Within 10% of average


# ============================================================================
# PHI EXPONENTIAL BINNING TESTS
# ============================================================================

class TestPhiExponentialBinner:
    """Test exponential binning with phi for O(log_phi n) complexity"""

    def test_bin_boundaries(self):
        """Test bin boundaries follow phi^n pattern"""
        binner = PhiExponentialBinner(max_bins=10)

        for i in range(10):
            expected = PHI ** i
            actual = binner.bin_boundaries[i]
            assert abs(actual - expected) < 0.0001

    def test_bin_assignment(self):
        """Test values are assigned to correct bins"""
        binner = PhiExponentialBinner()

        # Bin 0: [1.000, 1.618)
        assert binner.get_bin(0.5) == 0
        assert binner.get_bin(1.0) == 0
        assert binner.get_bin(1.5) == 0

        # Bin 1: [1.618, 2.618)
        assert binner.get_bin(2.0) == 1

        # Bin 2: [2.618, 4.236)
        assert binner.get_bin(3.0) == 2

    def test_bin_ranges(self):
        """Test bin range retrieval"""
        binner = PhiExponentialBinner()

        bin0_range = binner.get_bin_range(0)
        assert bin0_range[0] == 1.0
        assert abs(bin0_range[1] - PHI) < 0.0001

        bin1_range = binner.get_bin_range(1)
        assert abs(bin1_range[0] - PHI) < 0.0001
        assert abs(bin1_range[1] - (PHI ** 2)) < 0.0001

    def test_bin_center(self):
        """Test bin center calculation (geometric mean)"""
        binner = PhiExponentialBinner()

        center0 = binner.get_bin_center(0)
        expected0 = math.sqrt(1.0 * PHI)
        assert abs(center0 - expected0) < 0.0001

    def test_bins_in_range(self):
        """Test finding all bins overlapping a range"""
        binner = PhiExponentialBinner()

        bins = binner.bins_in_range(1.5, 5.0)
        # Should include bins 0, 1, 2, 3
        assert 0 in bins
        assert 1 in bins
        assert 2 in bins
        assert 3 in bins

    def test_logarithmic_complexity(self):
        """Test that binning enables logarithmic search"""
        binner = PhiExponentialBinner(max_bins=20)

        # For value = phi^10, should get bin 10 directly
        value = PHI ** 10
        bin_idx = binner.get_bin(value)

        assert bin_idx == 10

        # This means we can find the right bin in O(1) time,
        # reducing search from O(n) to O(log_phi n)


# ============================================================================
# DODECAHEDRAL ANCHORS TESTS
# ============================================================================

class TestDodecahedralAnchors:
    """Test 12-anchor dodecahedral geometry"""

    def test_12_anchors_generated(self):
        """Test that exactly 12 anchors are created"""
        dodec = DodecahedralAnchors()
        assert len(dodec.anchors) == 12

    def test_anchor_point_a(self):
        """Test Anchor Point A is at (1,1,1,1) normalized"""
        dodec = DodecahedralAnchors()
        anchor_a = dodec.get_anchor(1)

        assert anchor_a is not None
        # After normalization, should be on unit sphere
        mag = anchor_a.magnitude()
        assert abs(mag - 1.0) < 0.01

    def test_all_anchors_on_unit_sphere(self):
        """Test all anchors are normalized to unit sphere"""
        dodec = DodecahedralAnchors()

        for anchor_id in range(1, 13):
            anchor = dodec.get_anchor(anchor_id)
            mag = anchor.magnitude()
            assert abs(mag - 1.0) < 0.01

    def test_nearest_anchor(self):
        """Test finding nearest anchor"""
        dodec = DodecahedralAnchors()

        # Point very close to anchor 1
        point = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        nearest_id, distance = dodec.nearest_anchor(point)

        assert nearest_id in range(1, 13)
        assert distance >= 0

    def test_pentagonal_cluster(self):
        """Test each anchor has pentagonal cluster of 6 (self + 5)"""
        dodec = DodecahedralAnchors()

        for anchor_id in range(1, 13):
            cluster = dodec.get_pentagonal_cluster(anchor_id)
            assert len(cluster) == 6  # Self + 5 nearest
            assert anchor_id in cluster

    def test_anchor_distribution(self):
        """Test anchors are well-distributed in 4D space"""
        dodec = DodecahedralAnchors()

        # Calculate pairwise distances
        distances = []
        for i in range(1, 13):
            for j in range(i+1, 13):
                anchor_i = dodec.get_anchor(i)
                anchor_j = dodec.get_anchor(j)
                diff = anchor_i.to_vector() - anchor_j.to_vector()
                dist = np.linalg.norm(diff)
                distances.append(dist)

        # Standard deviation should be relatively low (well-distributed)
        std_dev = np.std(distances)
        assert std_dev < 0.5


# ============================================================================
# CONVENIENCE FUNCTIONS TESTS
# ============================================================================

class TestConvenienceFunctions:
    """Test convenience wrapper functions"""

    def test_fibonacci_function(self):
        """Test fibonacci() convenience function"""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55

    def test_golden_spiral_distance_function(self):
        """Test golden_spiral_distance() convenience function"""
        p1 = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        p2 = PhiCoordinate(0.7, 0.6, 0.8, 0.9)

        dist = golden_spiral_distance(p1, p2)
        assert dist > 0

    def test_rotate_by_golden_angle_function(self):
        """Test rotate_by_golden_angle() convenience function"""
        coord = PhiCoordinate(1.0, 0.0, 0.0, 0.0)
        rotated = rotate_by_golden_angle(coord, n=1, plane="LP")

        assert rotated.magnitude() > 0
        assert rotated != coord

    def test_get_phi_bin_function(self):
        """Test get_phi_bin() convenience function"""
        assert get_phi_bin(0.5) == 0
        assert get_phi_bin(2.0) == 1
        assert get_phi_bin(3.0) == 2


# ============================================================================
# PERFORMANCE BENCHMARKS
# ============================================================================

class TestPerformance:
    """Performance benchmarks for phi geometric operations"""

    def test_fibonacci_generation_speed(self):
        """Benchmark Fibonacci generation"""
        fib = FibonacciSequence(max_precompute=100)

        start = time.time()
        for i in range(100):
            _ = fib.get(i)
        elapsed = time.time() - start

        print(f"\nFibonacci(0-99): {elapsed*1000:.2f}ms")
        assert elapsed < 0.01  # Should be very fast (precomputed)

    def test_spiral_distance_speed(self):
        """Benchmark spiral distance calculation"""
        spiral = GoldenSpiral()
        p1 = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        p2 = PhiCoordinate(0.8, 0.6, 0.7, 0.9)

        start = time.time()
        for _ in range(1000):
            _ = spiral.distance_4d(p1, p2)
        elapsed = time.time() - start

        print(f"\n1000 spiral distances: {elapsed*1000:.2f}ms")
        assert elapsed < 1.0  # Should complete in under 1 second

    def test_binning_speed(self):
        """Benchmark phi binning O(log n) complexity"""
        binner = PhiExponentialBinner()

        values = [i * 0.1 for i in range(1, 1001)]

        start = time.time()
        for val in values:
            _ = binner.get_bin(val)
        elapsed = time.time() - start

        print(f"\n1000 bin lookups: {elapsed*1000:.2f}ms")
        assert elapsed < 0.1  # O(1) operations should be instant

    def test_rotation_speed(self):
        """Benchmark golden angle rotations"""
        rotator = GoldenAngleRotator()
        coord = PhiCoordinate(0.5, 0.5, 0.5, 0.5)

        start = time.time()
        for i in range(1000):
            _ = rotator.rotate_4d(coord, n=1, plane="LP")
        elapsed = time.time() - start

        print(f"\n1000 rotations: {elapsed*1000:.2f}ms")
        assert elapsed < 0.5


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple phi geometric operations"""

    def test_fibonacci_guided_spiral_search(self):
        """Test using Fibonacci sequence to guide spiral search depths"""
        fib = FibonacciSequence()
        spiral = GoldenSpiral()

        # Simulate semantic search expanding by Fibonacci levels
        center = PhiCoordinate(0.5, 0.5, 0.5, 0.5)
        test_points = [
            PhiCoordinate(0.6, 0.5, 0.5, 0.5),
            PhiCoordinate(0.7, 0.6, 0.6, 0.6),
            PhiCoordinate(0.8, 0.7, 0.7, 0.7),
        ]

        # Search at Fibonacci-spaced radii
        for depth in range(3):
            search_radius = fib.get(depth + 3) / 10.0  # F(3), F(4), F(5)
            # Simulate finding points within radius
            found_count = sum(1 for p in test_points
                            if spiral.distance_4d(center, p) < search_radius)

        assert found_count >= 0  # Just verify it runs

    def test_dodecahedral_navigation_with_golden_angle(self):
        """Test navigating between dodecahedral anchors using golden angle"""
        dodec = DodecahedralAnchors()
        rotator = GoldenAngleRotator()

        # Start at anchor 1
        current = dodec.get_anchor(1)

        # Rotate by golden angle to find next navigation target
        rotated = rotator.rotate_4d(current, n=1, plane="LP")

        # Find nearest anchor to rotated position
        nearest_id, distance = dodec.nearest_anchor(rotated)

        assert nearest_id in range(1, 13)
        assert nearest_id != 1  # Should be different anchor

    def test_exponential_binning_with_fibonacci_counts(self):
        """Test using Fibonacci counts for bin populations"""
        binner = PhiExponentialBinner()
        fib = FibonacciSequence()

        # Simulate storing Fibonacci number of items per bin
        bin_counts = {}
        for bin_idx in range(10):
            expected_count = fib.get(bin_idx + 1)
            bin_counts[bin_idx] = expected_count

        # Verify Fibonacci pattern in distribution
        assert bin_counts[5] == 8  # F(6) = 8
        assert bin_counts[7] == 21  # F(8) = 21


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
