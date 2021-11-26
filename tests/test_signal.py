# -*- coding: utf-8 -*-
import pytest

from sensirion_driver_support_types.signals import AbstractSignal, ScaleAndOffsetSignal


class FlowSignal(ScaleAndOffsetSignal):
    def __init__(self, raw_flow):
        super().__init__(raw_value=raw_flow, scaling=64, offset=200, num_digits=5)


class SignalTemperature(ScaleAndOffsetSignal):
    def __init__(self, raw_temperature):
        super().__init__(raw_value=raw_temperature, scaling=200.0, offset=0)


@pytest.mark.parametrize("signal, expected_name", [(SignalTemperature(5000), 'Temperature'),
                                                   (FlowSignal(1500), 'Flow')])
def test_signal_name(signal, expected_name):
    assert isinstance(signal, AbstractSignal)
    assert signal.name == expected_name


@pytest.mark.parametrize("signal, expected_value", [(SignalTemperature(5000), 5000.0 / 200.0),
                                                    (FlowSignal(1500), (1500.0 - 200.0) / 64)])
def test_signal_value(signal: ScaleAndOffsetSignal, expected_value):
    assert isinstance(signal, AbstractSignal)
    assert signal.value == expected_value
    assert str(signal) == signal.number_format.format(expected_value)
