from collections import namedtuple

BitField = namedtuple('BitField', ('offset', 'width'))


class BitfieldContainer:

    def __init__(self, int_value=0):
        self._int_value = int_value

    def __getattribute__(self, item):
        attr = super(BitfieldContainer, self).__getattribute__(item)
        if isinstance(attr, BitField):
            return self._get_value(attr)
        return attr

    def __setattr__(self, key, value):
        if hasattr(self, key):
            attr = super(BitfieldContainer, self).__getattribute__(key)
            if isinstance(attr, BitField):
                self._set_value(attr, value)
                return
        super().__setattr__(key, value)

    @staticmethod
    def _get_mask(width: int) -> int:
        return (1 << width) - 1

    def _get_value(self, bitfield: BitField):
        mask = self._get_mask(bitfield.width)
        return (self._int_value >> bitfield.offset) & mask

    def _set_value(self, bitfield: BitField, value: int):
        mask = self._get_mask(bitfield.width)
        self._int_value &= ~(mask << bitfield.offset)
        self._int_value |= ((value & mask) << bitfield.offset)

    @property
    def value(self):
        return self._int_value
