from numba import typeof
from numba.experimental import jitclass

from definitions.position import Position


@jitclass([
    ("long", typeof(Position('', 0.0, 0.0, 0.0, 0.0, 0, ''))),
    ("short", typeof(Position('', 0.0, 0.0, 0.0, 0.0, 0, '')))
])
class PositionList:
    """
    A class representing long and short positions.
    """

    def __init__(self):
        self.long = Position('', 0.0, 0.0, 0.0, 0.0, 0, '')
        self.short = Position('', 0.0, 0.0, 0.0, 0.0, 0, '')

    def update_long(self, position: Position):
        self.long.symbol = position.symbol
        self.long.size = position.size
        self.long.price = position.price
        self.long.liquidation_price = position.liquidation_price
        self.long.upnl = position.upnl
        self.long.leverage = position.leverage
        self.long.position_side = position.position_side

    def update_short(self, position: Position):
        self.short.symbol = position.symbol
        self.short.size = position.size
        self.short.price = position.price
        self.short.liquidation_price = position.liquidation_price
        self.short.upnl = position.upnl
        self.short.leverage = position.leverage
        self.short.position_side = position.position_side
