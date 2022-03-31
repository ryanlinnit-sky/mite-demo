from mite.scenario import StopScenario


def volume_model_factory(n, duration=60 * 5):
    def vm(start, end):
        if start > duration:
            raise StopScenario
        return n

    vm.__name__ = f"volume model {n}"
    return vm


scenarios = [
    (5, "application.journeys:get_url1_journey", None),
    (1, "application.journeys:get_url2_journey", None),
    (1, "application.journeys:get_url3_journey", None),
    (3, "application.journeys:post_url5_journey", None),
    (2, "application.journeys:get_profile_journey", None),
    (1, "application.journeys:get_404_journey", None),
]


# Peak scenario running at full TPS for 1 hour
def peak_scenario():
    for peak, journey, datapool in scenarios:
        yield journey, datapool, volume_model_factory(peak, duration=1 * 60 * 60)


# Soak scenario running at a third TPS for 6 hours
def soak_scenario():
    for peak, journey, datapool in scenarios:
        yield journey, datapool, volume_model_factory(peak / 3, duration=6 * 60 * 60)


# Quick scenario running at full TPS for default time of 5 minute
def quick_scenario():
    for peak, journey, datapool in scenarios:
        yield journey, datapool, volume_model_factory(peak)
