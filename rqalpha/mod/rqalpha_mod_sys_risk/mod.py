# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


from rqalpha.interface import AbstractMod
from rqalpha.const import FRONT_VALIDATOR_TYPE

from .validators import (
    CashValidator, StockPositionValidator, FuturePositionValidator, PriceValidator, IsTradingValidator,
    SelfTradeValidator
)


class RiskManagerMod(AbstractMod):
    def start_up(self, env, mod_config):
        if mod_config.validate_price:
            env.add_frontend_validator(PriceValidator(env), FRONT_VALIDATOR_TYPE.PRICE)
        if mod_config.validate_is_trading:
            env.add_frontend_validator(IsTradingValidator(env))
        if mod_config.validate_cash:
            env.add_frontend_validator(CashValidator(env), FRONT_VALIDATOR_TYPE.CASH)
        if mod_config.validate_stock_position:
            env.add_frontend_validator(StockPositionValidator(), FRONT_VALIDATOR_TYPE.POSITION)
        if mod_config.validate_future_position:
            env.add_frontend_validator(FuturePositionValidator(), FRONT_VALIDATOR_TYPE.POSITION)
        if mod_config.validate_self_trade:
            env.add_frontend_validator(SelfTradeValidator(env))

    def tear_down(self, code, exception=None):
        pass
