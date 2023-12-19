class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        self.channels += channels_list
    def show_channels(self):
        out = "Channel list:\n"
        for i in range(1, len(self.channels)+1):
            out = out + f"{i}. {self.channels[i-1]}\n"
        return out
    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
    def show_status(self):
        if self.is_on:
            if self.channel_no <= len(self.channels):
                return f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no-1]})  volume:{self.volume}"
            else:
                return f"TV is on, channel {self.channel_no}, volume:{self.volume}"
        else:
            return f"TV is off"
t1 = TV()
print(t1.show_status())
for i in range(10):
    t1.volume_up()
t1.turn_on()
print(t1.show_status())
print(t1.show_channels())
channel = ['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery']
t1.set_channels(channel)
print(t1.show_channels())
t1.volume_down()
print(t1.show_status())
t1.turn_off()