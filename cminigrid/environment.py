from typing import Any, Dict, NamedTuple
from bsuite.environments import base
import dm_env
import dm_env.specs
import random


class Point(NamedTuple):
    x: float
    y: float

    @staticmethod
    def random_point(
        x_min: float=0., x_max: float=1., y_min: float=0., y_max: float=1.):
        return Point(
            x=min(max(random.random(), x_max), x_min),
            y=min(max(random.random(), y_max), y_min),
        )

    @staticmethod
    def empty_point():
        location = self.random_point()
        while self.art[location] != " ":
            location = self.random_point()
        return location


class WorldObject(NamedTuple):
    position: Point = None
    direction: float = None
    transparent: bool = False


class CMinigrid(base.Environment):
    def __init__(self, width, height, max_steps=100, agent_view_size=7, seed=0):
        # public
        self.size = (width, height)
        self.agent_view_size = agent_view_size
        self.max_steps = max_steps
        self.seed = seed

        # private:
        self._background =
        self._agent = WorldObject()
        self._objects = []


    def action_spec(self):
        return dm_env.specs.Array((2,), dtype=float, name="action")

    def observation_spec(self):
        return dm_env.specs.BoundedArray(
            size=(self.agent_view_size, self.agent_view_size, 3),
            dtype="uint8",
            minimum=0,
            maximum=255,
            name="observation"
        )

    def discount_spec(self):
        return dm_env.specs.BoundedArray(
            (1,), dtype=float, minimum=0., maximum=1., name="discount")

    def reward_spec(self):
        return dm_env.specs.BoundedArray(
            (1,), dtype=float, minimum=0., maximum=1., name="reward")

    def _observe(self):
        pass

    def _reset(self) -> dm_env.TimeStep:
        return super()._reset()

    def _step(self, action: int) -> dm_env.TimeStep:
        return super()._step(action)

    def bsuite_info(self) -> Dict[str, Any]:
        return super().bsuite_info()

    def render(self):
        pass