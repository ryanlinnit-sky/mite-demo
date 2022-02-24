
scenarios = [
    (10, "src.application.journeys:get_url1_journey", None),
    (10, "src.application.journeys:get_url2_journey", None),
    (10, "src.application.journeys:get_url3_journey", None),
]

def quick_scenario():
    for peak, journey, datapool in scenarios:
        # vm = baseline_rampup_factory(peak / 4, ramp_over=100, sustain=60)
        volumemodel = lambda start, end: 1
        yield journey, datapool, volumemodel
