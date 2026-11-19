"""Evaluation helpers for ordered phase sequences."""

from __future__ import annotations

import numpy as np


def frame_accuracy(predictions, targets) -> float:
    predictions = np.asarray(predictions)
    targets = np.asarray(targets)
    if predictions.shape != targets.shape:
        raise ValueError("predictions and targets must have identical shapes")
    return float((predictions == targets).mean())


def first_transition(sequence, from_class: int, to_class: int) -> int | None:
    """Find the first adjacent transition between two ordered classes."""
    values = np.asarray(sequence)
    hits = np.flatnonzero((values[:-1] == from_class) & (values[1:] == to_class))
    return int(hits[0] + 1) if len(hits) else None


def transition_absolute_error(predicted, target, from_class: int, to_class: int):
    pred_index = first_transition(predicted, from_class, to_class)
    target_index = first_transition(target, from_class, to_class)
    if pred_index is None or target_index is None:
        return None
    return abs(pred_index - target_index)

