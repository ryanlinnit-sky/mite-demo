from mite.scenario import StopScenario


def volume_model_factory(n):
    def vm(start, end):
        if start > 60 * 5:  # Will run for 5 mins
            raise StopScenario
        return n

    vm.__name__ = f"volume model {n}"
    return vm


scenarios = [
    (5, "application.journeys:get_url1_journey", None),
    (1, "application.journeys:get_url2_journey", None),
    (1, "application.journeys:get_url3_journey", None),
    (3, "application.journeys:post_url5_journey", None),
    (10, "application.journeys:get_profile_journey", None),
    (1, "application.journeys:get_404_journey", None),
]


def quick_scenario():
    for peak, journey, datapool in scenarios:
        yield journey, datapool, volume_model_factory(peak)
