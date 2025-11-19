class Launch:
    def __init__(self, launch_id=None, rocket_id=None, site_id=None,
                 angle=None, velocity=None, range_=None, max_height=None):
        self.launch_id = launch_id
        self.rocket_id = rocket_id
        self.site_id = site_id
        self.angle = angle
        self.velocity = velocity
        self.range = range_
        self.max_height = max_height
