#!/usr/bin/env python3
"""Small sanity tests for the mathematical bookkeeping used in the ASCP paper.

These tests do not prove the architecture secure. They check that the examples
and identities encoded in the public release behave as stated.
"""
from __future__ import annotations

import unittest


def attenuates(child: dict[str, set[str]], parent: dict[str, set[str]]) -> bool:
    return all(child[k] <= parent[k] for k in parent)


def weighted_score(xs: list[float], ws: list[float]) -> float:
    if len(xs) != len(ws) or not xs or any(w < 0 for w in ws) or sum(ws) <= 0:
        raise ValueError("invalid score inputs")
    return sum(x * w for x, w in zip(xs, ws)) / sum(ws)


def brier(p: float, outcome: int) -> float:
    return (p - outcome) ** 2


def union_from_complement_chain(conditionals_given_no_prior_failure: list[float]) -> float:
    survival = 1.0
    for p in conditionals_given_no_prior_failure:
        if not 0.0 <= p <= 1.0:
            raise ValueError("probability outside [0,1]")
        survival *= 1.0 - p
    return 1.0 - survival


class TestASCPMath(unittest.TestCase):
    def test_vertical_attenuation(self) -> None:
        parent = {
            "R": {"db", "files"},
            "O": {"read", "write"},
            "D": {"public", "internal"},
            "E": {"query", "update"},
        }
        child = {
            "R": {"db"},
            "O": {"read"},
            "D": {"internal"},
            "E": {"query"},
        }
        amplified = {**child, "O": {"read", "delete"}}
        self.assertTrue(attenuates(child, parent))
        self.assertFalse(attenuates(amplified, parent))

    def test_horizontal_handoff_uses_sponsor_authority_not_planner_subset(self) -> None:
        planner_resources = {"calendar"}
        sponsor_max_resources = {"calendar", "database"}
        specialist_resources = {"database"}
        self.assertFalse(specialist_resources <= planner_resources)
        self.assertTrue(specialist_resources <= sponsor_max_resources)

    def test_weighted_policy_score_is_bounded(self) -> None:
        value = weighted_score([0.1, 0.7, 0.4], [2.0, 1.0, 3.0])
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)
        self.assertAlmostEqual(value, (0.2 + 0.7 + 1.2) / 6.0)

    def test_brier_score_examples(self) -> None:
        self.assertAlmostEqual(brier(0.60, 1), 0.16)
        self.assertAlmostEqual(brier(0.60, 0), 0.36)

    def test_exact_complement_chain_for_correlated_two_event_example(self) -> None:
        # Explicit correlated joint distribution:
        # P(F1)=0.20
        # P(F2|not F1)=0.25
        # P(F2|F1)=0.90
        # Thus P(F1 union F2)=0.20 + 0.80*0.25 = 0.40.
        exact_union = union_from_complement_chain([0.20, 0.25])
        self.assertAlmostEqual(exact_union, 0.40)

        # The marginal P(F2) is 0.20*0.90 + 0.80*0.25 = 0.38.
        # Incorrectly applying an independence formula to the marginals gives
        # 1-(1-.20)(1-.38)=.504, demonstrating why independence is not general.
        marginal_f2 = 0.20 * 0.90 + 0.80 * 0.25
        independence_guess = 1.0 - (1.0 - 0.20) * (1.0 - marginal_f2)
        self.assertAlmostEqual(marginal_f2, 0.38)
        self.assertAlmostEqual(independence_guess, 0.504)
        self.assertNotAlmostEqual(independence_guess, exact_union)


if __name__ == "__main__":
    unittest.main()
