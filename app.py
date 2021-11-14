from enum import Enum
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

from rule_list import RuleList


class Season(Enum):
    SUMMER = 1
    AUTUMN = 2
    WINTER = 3
    SPRING = 4


class Temperature(Enum):
    WARM = 1
    TEMPERED = 2


class WaterState(Enum):
    RUNNING = 1
    CLOUDY = 2
    STAGNANT = 3
    NORMAL = 4
    CALM = 5


class DayTime(Enum):
    MORNING = 1
    MIDDAY = 2
    NOON = 3
    NIGHT = 4
    DAWN = 5


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Depth(Enum):
    SHALLOW = 1
    MEDIUM = 2
    LARGE = 3


class Bait(Enum):
    MOJARRA = 1
    WORM = 2
    CATFISH = 3
    EEL = 4


class ReelSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class LineDiameter(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class PlumbWeight(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Fish(object):
    def __init__(self, seasons, temperature, water_states, timeframes, size, depth, diet, needs_telescopic_rod,
                 needed_reel_size, needs_reel_stop, needs_line_diameter, needs_plumb, needed_plumb_weight):
        self.seasons = seasons
        self.temperature = temperature
        self.water_states = water_states
        self.timeframes = timeframes
        self.size = size
        self.depth = depth
        self.diet = diet
        self.needs_telescopic_rod = needs_telescopic_rod
        self.needed_reel_size = needed_reel_size
        self.needs_reel_stop = needs_reel_stop
        self.needed_line_diameter = needs_line_diameter
        self.needs_plumb = needs_plumb
        self.needed_plumb_weight = needed_plumb_weight
        self.points = 0

    def __str__(self):
        # return "Points {}, name {}".format(str(self.points), type(self).__name__)
        return str(type(self).__name__)


class Trucha(Fish):
    def __init__(self):
        super(Trucha, self).__init__(
            seasons=[Season.SUMMER],
            temperature=Temperature.WARM,
            water_states=WaterState.CALM,
            depth=[Depth.MEDIUM],
            timeframes=[DayTime.NIGHT],
            size=Size.MEDIUM,
            diet=Bait.MOJARRA,
            needs_telescopic_rod=False,
            needed_reel_size=ReelSize.MEDIUM,
            needs_reel_stop=True,
            needs_line_diameter=LineDiameter.LARGE,
            needs_plumb=True,
            needed_plumb_weight=[PlumbWeight.LARGE]
        )


class Carpa(Fish):
    def __init__(self):
        super(Carpa, self).__init__(
            seasons=[Season.SUMMER],
            temperature=Temperature.WARM,
            water_states=WaterState.NORMAL,
            depth=[Depth.SHALLOW, Depth.MEDIUM, Depth.LARGE],
            timeframes=[DayTime.MORNING, DayTime.NOON, DayTime.NIGHT],
            size=Size.SMALL,
            diet=Bait.WORM,
            needs_telescopic_rod=False,
            needed_reel_size=ReelSize.SMALL,
            needs_reel_stop=True,
            needs_line_diameter=LineDiameter.SMALL,
            needs_plumb=True,
            needed_plumb_weight=[PlumbWeight.SMALL]
        )


class Surubi(Fish):
    def __init__(self):
        super(Surubi, self).__init__(
            seasons=[Season.SUMMER],
            temperature=Temperature.WARM,
            water_states=WaterState.NORMAL,
            depth=[Depth.LARGE],
            timeframes=[DayTime.NIGHT],
            size=Size.LARGE,
            diet=Bait.EEL,
            needs_telescopic_rod=False,
            needed_reel_size=ReelSize.LARGE,
            needs_reel_stop=True,
            needs_line_diameter=LineDiameter.LARGE,
            needs_plumb=True,
            needed_plumb_weight=[PlumbWeight.LARGE]
        )


class Pejerrey(Fish):
    def __init__(self):
        super(Pejerrey, self).__init__(
            seasons=[Season.WINTER],
            temperature=Temperature.TEMPERED,
            water_states=WaterState.CLOUDY,
            depth=[Depth.SHALLOW],
            timeframes=[DayTime.MORNING],
            size=Size.SMALL,
            diet=Bait.MOJARRA,
            needs_telescopic_rod=True,
            needed_reel_size=ReelSize.SMALL,
            needs_reel_stop=False,
            needs_line_diameter=LineDiameter.SMALL,
            needs_plumb=False,
            needed_plumb_weight=[PlumbWeight.SMALL, PlumbWeight.MEDIUM, PlumbWeight.LARGE]
        )


class Dorado(Fish):
    def __init__(self):
        super(Dorado, self).__init__(
            seasons=[Season.SUMMER, Season.SPRING, Season.AUTUMN, Season.WINTER],
            temperature=Temperature.WARM,
            water_states=WaterState.RUNNING,
            depth=[Depth.MEDIUM],
            timeframes=[DayTime.MORNING, DayTime.NOON],
            size=Size.MEDIUM,
            diet=Bait.CATFISH,
            needs_telescopic_rod=False,
            needed_reel_size=ReelSize.MEDIUM,
            needs_reel_stop=True,
            needs_line_diameter=LineDiameter.LARGE,
            needs_plumb=True,
            needed_plumb_weight=[PlumbWeight.MEDIUM]
        )


class Model(object):
    def __init__(self, season=None, temperature=None, water_state=None, fishing_depth=None, time=None, fish_size=None,
                 bait=None, has_telescopic_rod=None, reel_size=None, has_reel_stop=None, line_diameter=None,
                 has_plumb=None, plumb_weight=None):
        self._season = season
        self._temperature = temperature
        self._water_state = water_state
        self._fishing_depth = fishing_depth
        self._time = time
        self._fish_size = fish_size
        self._bait = bait
        self._has_telescopic_rod = has_telescopic_rod
        self._reel_size = reel_size
        self._has_reel_stop = has_reel_stop
        self._line_diameter = line_diameter
        self._has_plumb = has_plumb
        self._plumb_weight = plumb_weight
        self._options = [Trucha(), Carpa(), Dorado(), Pejerrey(), Surubi()]

    def evaluate_season(self, season):
        season = Season(season)
        for fish in self._options:
            if season in fish.seasons:
                fish.points += 10
            else:
                fish.points -= 5

    def evaluate_temperature(self, temperature):
        temperature = Temperature(temperature)
        for fish in self._options:
            if fish.temperature == temperature:
                fish.points += 10

    def evaluate_water_state(self, water_state):
        water_state = WaterState(water_state)
        for fish in self._options:
            if fish.water_states == water_state:
                fish.points += 10

    def evaluate_depth(self, depth):
        depth = WaterState(depth)
        for fish in self._options:
            if depth in fish.depth:
                fish.points += 10

    def evaluate_time(self, time):
        time = DayTime(time)
        for fish in self._options:
            if time in fish.timeframes:
                fish.points += 10

    def evaluate_fish_size(self, size):
        size = Size(size)
        for fish in self._options:
            if size == fish.size:
                fish.points += 5

    def evaluate_bait(self, bait):
        bait = Bait(bait)
        for fish in self._options:
            if fish.diet == bait:
                fish.points += 10

    def evaluate_has_telescopic_rod(self, has_telescopic_rod):
        for fish in self._options:
            if fish.needs_telescopic_rod:
                if has_telescopic_rod:
                    fish.points += 10
                else:
                    fish.points -= 10

    def evaluate_reel_size(self, reel_size):
        reel_size = ReelSize(reel_size)
        for fish in self._options:
            if fish.needed_reel_size.value <= reel_size.value:
                fish.points += 5

    def evaluate_has_reel_stop(self, reel_stop):
        for fish in self._options:
            if fish.needs_reel_stop:
                if reel_stop:
                    fish.points += 10
                else:
                    fish.points -= 10

    def evaluate_line_diameter(self, line_diameter):
        line_diameter = LineDiameter(line_diameter)
        for fish in self._options:
            if fish.needed_line_diameter == line_diameter:
                fish.points += 5

    def evaluate_has_plumb(self, has_plumb):
        for fish in self._options:
            if fish.needs_plumb:
                if has_plumb:
                    fish.points += 10
                else:
                    fish.points -= 10

    def evaluate_plumb_weight(self, plumb_weight):
        plumb_weight = PlumbWeight(plumb_weight)
        for fish in self._options:
            if fish.needed_plumb_weight == plumb_weight:
                fish.points += 10

    def best_proposal(self):
        fish_list = sorted(self._options, key=lambda fish: fish.points, reverse=True)
        max_points = fish_list[0].points
        fish_list = [fish for fish in fish_list if fish.points == max_points]
        return sorted(fish_list, key=lambda fish: fish.size.value, reverse=True)[0]

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        self._season = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def water_state(self):
        return self._water_state

    @water_state.setter
    def water_state(self, value):
        self._water_state = value

    @property
    def fishing_depth(self):
        return self._fishing_depth

    @fishing_depth.setter
    def fishing_depth(self, value):
        self._fishing_depth = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def fish_size(self):
        return self._fish_size

    @fish_size.setter
    def fish_size(self, value):
        self._fish_size = value

    @property
    def bait(self):
        return self._bait

    @bait.setter
    def bait(self, value):
        self._bait = value

    @property
    def has_telescopic_rod(self):
        return self._has_telescopic_rod

    @has_telescopic_rod.setter
    def has_telescopic_rod(self, value):
        self._has_telescopic_rod = value

    @property
    def reel_size(self):
        return self._reel_size

    @reel_size.setter
    def reel_size(self, value):
        self._reel_size = value

    @property
    def has_reel_stop(self):
        return self._has_reel_stop

    @has_reel_stop.setter
    def has_reel_stop(self, value):
        self._has_reel_stop = value

    @property
    def line_diameter(self):
        return self._line_diameter

    @line_diameter.setter
    def line_diameter(self, value):
        self._line_diameter = value

    @property
    def has_plumb(self):
        return self._has_plumb

    @has_plumb.setter
    def has_plumb(self, value):
        self._has_plumb = value

    @property
    def plumb_weight(self):
        return self._plumb_weight

    @plumb_weight.setter
    def plumb_weight(self, value):
        self._plumb_weight = value

    def __str__(self):
        return "Season: {}, Temperature: {}, Water state: {}, Fishing depth: {}, " \
               "Day time: {}, Fish size: {}, Bait: {}, Has telescopic rod: {}, " \
               "Reel size: {}, Has reel stop size: {}, Line diameter: {}, " \
               "Has plumb: {}, Plumb weight: {}".format(self._season.name,
                                                        self._temperature.name.capitalize(),
                                                        self._water_state.name.capitalize(),
                                                        self._fishing_depth.name.capitalize(),
                                                        self._time.name.capitalize(),
                                                        self._fish_size.name.capitalize(),
                                                        self._bait.name.capitalize(),
                                                        str(self._has_telescopic_rod),
                                                        self._reel_size.name.capitalize(),
                                                        str(self._has_reel_stop),
                                                        self._line_diameter.name.capitalize(),
                                                        str(self._has_plumb),
                                                        self._plumb_weight.name.capitalize()
                                                        )


app = Flask(__name__)
CORS(app)


@app.route('/evaluate', methods=['POST'])
def suggestion_fallas2():
    parameters = request.get_json()
    suggestion = evaluate(
        parameters.get('season', None),
        parameters.get('temperature', None),
        parameters.get('water state', None),
        parameters.get('fishing depth', None),
        parameters.get('time', None),
        parameters.get('fish size', None),
        parameters.get('bait', None),
        parameters.get('has telescopic rod', None),
        parameters.get('reel size', None),
        parameters.get('has reel stop', None),
        parameters.get('line diameter', None),
        parameters.get('has plumb', None),
        parameters.get('plumb weight', None)
    )

    return jsonify({'suggestion': str(suggestion)})


class FishEngine:

    def learn(self, rules_file, learning_method='forward_chaining'):
        self.rule_list = RuleList(rules_file)
        self.learning_method = learning_method

    def learn_model(self, model_object):
        self.model_object = model_object

    def reason(self):
        if self.learning_method == 'forward_chaining':
            self.forward_chaining()
        else:
            raise Exception('Not Supported learning method')

    def forward_chaining(self):
        for rule in self.rule_list.rules:
            applies_rule = all(condition.evaluate(self.model_object) for condition in rule.conditions)
            if applies_rule:
                map(lambda consequence: consequence.apply(self.model_object), rule.consequences)

    @property
    def knowledge(self):
        return self.model_object


def evaluate(season, temperature, water_state, fishing_depth, time, fish_size, bait, has_telescopic_rod, reel_size,
             has_reel_stop, line_diameter, has_plumb, plumb_weight):
    engine = FishEngine()

    engine.learn("rules.json")

    model = Model(season=season, temperature=temperature, water_state=water_state, fishing_depth=fishing_depth,
                  time=time, fish_size=fish_size, bait=bait, has_telescopic_rod=has_telescopic_rod,
                  reel_size=reel_size, has_reel_stop=has_reel_stop, line_diameter=line_diameter,
                  has_plumb=has_plumb, plumb_weight=plumb_weight)

    engine.learn_model(model)
    engine.reason()

    return engine.knowledge.best_proposal()
