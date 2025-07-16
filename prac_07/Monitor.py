class Monitor:
    def __init__(self, model, width, height):
        """Initialize a Monitor instance."""
        self.model = model
        self.width = width
        self.height = height
    def get_resolution(self)->tuple:
        """Return the resolution of the monitor."""
        return (self.width, self.height)

    def get_total_pixels(self)->int:
        """Return the total number of pixels in the monitor."""
        return self.width * self.height



    def __eq__(self, other):
        """compare two Monitor objects."""
        return self.width == other.width and self.height == other.height


def main():
        monitor = Monitor("Dell U2723QE", 3840, 2160)
        monitor1 = Monitor("Zowie XL2540KE", 3840, 2160)
        monitor2 = Monitor("Zowie XL2546K", 1920, 1080)
        print("Monitor model:", monitor.model)
        print("Resolution:", monitor.get_resolution())
        print("Total pixels:", monitor.get_total_pixels())
        print(monitor1 == monitor2)

main()



