import time
import json
import sys

# f = open(r"D:\MultiMC\instances\Eye Candy\.minecraft\config\jsMacros\Macros\logs\myout.txt", 'w')


class EventWrapper:
    """

    """

    def __init__(self, event):
        self.event = event
        self.name = event.eventName
        self.named_attr = str(self.event.getString("_attribute_list")).split()

        self.finalized = False

        self.put_key = {
            str: self.event.putString,
            int: self.event.putInt,
            float: self.event.putDouble,
            bool: self.event.putBoolean
        }
        self.get_key = {
            str: self.event.getString,
            int: self.event.getInt,
            float: self.event.getDouble,
            bool: self.event.getBoolean
        }

        self.data = {
            "numeric": []
        }

    def load(self):
        """
        Loads the data in the event into self.data so it can be manipulated.

        """
        print("===== NYI NYI NYI =====")

    def __getitem__(self, key):
        """Gets an item.

        @todo EventWrapper.__getitem__ | make support for automatic types, right now only supports string.
        @todo EventWrapper.__getitem__ | Add support for finalized wrappers.
        """
        return self.data[key]

    def __iter__(self):
        """Generator to iterate through numeric-keyed attributes. Only works on loaded instances. """
        for i in self.data["numeric"]:
            yield i

    def __len__(self):
        return len(self.data) - 1 + len(self.data["numeric"])

    def iter_all(self):
        """Generator to iterate through all attributes. Iterates through numeric-keyed attributes first.
        Only works on loaded instances. """
        for i in self.data["numeric"]:
            yield i
        for i in self.data.keys():
            if i == "numeric":
                continue
            yield self.data[i]

    @property
    def numeric_length(self):
        """Returns the number of numeric-keyed attributes the event has."""
        return len(self.data["numeric"])

    def join(self):
        return ' '.join([i for i in self])

    def join_all(self):
        return ' '.join([i for i in self.iter_all()])

    def unwrap(self):
        """Returns the unwrapped event object. Don't do this on an unfinalized event, you won't get anything."""
        return self.event

    def trigger(self, callback=None):
        if callback:
            self.event.trigger(callback)
            return
        self.event.trigger()
        return self

    def trigger_join(self):
        """Triggers the event and waits for it to complete.
        EXERCISE CAUTION WHEN USING, as this may cause circular waiting when triggered from the same
        thread as the jsmacros.on registration for the event"""
        self.event.triggerJoin()
        return self

    def put(self, value, name):
        """Adds the value to data."""
        if name.isdigit():
            self.data['numeric'][int(name)] = value
        else:
            self.data[name] = value

    def _put(self, value, name):
        """Attempts to divine the type of the value, and then calls the associated put function on the event"""
        name = str(name)
        self.finalized = False
        try:
            self.put_key[type(value)](name, value)
        except KeyError:
            # putting object
            self.event.putObject(name, value)
        if name.isdigit():
            pass
        else:
            self.named_attr.append(name)
        return self

    def append(self, value):
        self.data['numeric'].append(value)
        return self

    def _place_data(self, value, name):
        """DON'T TOUCH, INTERNAL METHOD FOR PLACING DATA"""
        string = value.split('{')
        try:
            self.put(f"data_{name}", '{' + string[1])
            return True
        except IndexError:
            return False

    def _put_data(self, value, name):
        """DON'T TOUCH, INTERNAL METHOD FOR APPENDING DATA TO data DICT"""
        

    def parse_put(self, string):
        """Allows assigning a string attribute from chat using syntax name=value

        @todo EventWrapper.parse_put | make support for types other than string
        """
        if '=' in string:
            string = string.split('=')
            self._put_data(string[1], string[0])
            self.put(string[0], string[1])
        else:
            self._place_data(str(self.numeric_length + 1), string)
            self.put_numeric(string)
        return self

    def smart_put(self, value):
        """Uses self.parse_put when it detects a '=' in the input, otherwise uses self.put_numeric
        """
        if '=' in value or '{' in value:
            f.write(f"Parsing {value}")
            self.parse_put(value)
        else:
            f.write(f"Placing {value}")
            self.put_numeric(value)
        return self

    def put_numeric_list(self, values):
        """Places every item in value into a numeric key, starting from the one right after the last existing one.
        @type values: list
        """
        key = self.numeric_length + 1
        for key, value in range(key, len(values)), values:
            self.put(key, value)
        return self

    def smart_put_list(self, values):
        """Places every item in value into a smart key as defined by event.smart_put
        """
        for value in values:
            f.write(f"Adding {value} to list! ")
            self.smart_put(value)

    def put_dict(self, value_dict):
        """Takes a dictionary and puts each of its keys as a named attr of the event, with the value as the value.

        @type value_dict: dict
        """
        for i in value_dict.keys():
            self.put(i, value_dict[i])
        return self

    def finalize(self):
        """You need to call this after creating the event, to finalize its creation.

        Writes attributes of the EventWrapper to the event itself, so that it can be used by regular JSM code.
        """
        self.event.putString("_attribute_list", ' '.join(self.named_attr))
        self.finalized = True

        return self.event


class WorldWrapper:
    def __init__(self, World):
        self.world = World

    def __getitem__(self, key):
        return getattr(self, key)

    @property
    def is_loaded(self):
        return self.world.isWorldLoaded()

    @property
    def loaded_players(self):
        return self.world.getLoadedPlayers()

    @property
    def players(self):
        return self.world.getPlayers()

    @property
    def scoreboards(self):
        return self.world.getScoreboards()

    @property
    def entities(self):
        return self.world.getEntities()

    @property
    def dimension(self):
        return self.world.getDimension()

    @property
    def biome(self):
        return self.world.getBiome()

    @property
    def time(self):
        return self.world.getTime()

    @property
    def time_of_day(self):
        return self.world.getTimeOfDay()

    @property
    def respawn_pos(self):
        return self.world.getRespawnPos()

    @property
    def difficulty(self):
        return self.world.getDifficulty()

    @property
    def moon_phase(self):
        return self.world.getMoonPhase()

    @property
    def boss_bars(self):
        return self.world.getBossBars()

    @property
    def tps(self):
        return self.world.getServerTPS()

    @property
    def tab_list_header(self):
        return self.world.getTabListHeader()

    @property
    def tab_list_footer(self):
        return self.world.getTabListFooter()

    @property
    def server_address(self):
        return self.world.getCurrentServerAddress()

    @property
    def instant_tps(self):
        return self.world.getServerInstantTPS()

    def average_tps(self, average_time):
        if average_time not in [1, 5, 15]:
            raise ValueError
        else:
            if average_time == 1:
                return self.world.getServer1MAverageTPS()
            elif average_time == 5:
                return self.world.getServer5MAverageTPS()
            elif average_time == 15:
                return self.world.getServer15MAverageTPS()

    def get_block(self, x, y, z):
        return self.world.getBlock(x, y, z)

    def get_sky_light(self, x, y, z):
        return self.world.getSkyLight(x, y, z)

    def get_block_light(self, x, y, z):
        return self.world.getBlockLight(x, y, z)

    def is_chunk_loaded(self, chunk_x, chunk_z):
        return self.world.isChunkLoaded(chunk_x, chunk_z)

    def get_biome_at(self, x, z):
        return self.world.getBiomeAt(x, z)

    def play_sound(self, ID, volume=1, pitch=1, x=0, y=0, z=0):
        if x and y and z:
            self.world.playSound(ID, volume, pitch, x, y, z)
        else:
            self.world.playSound(ID, volume, pitch)

    def unwrap(self):
        """Returns the unwrapped World object. Basically the same as self.world."""
        return self.world


class ChatWrapper:
    def __init__(self, chat):
        self.chat = chat

    def log(self, msg, wait=False):
        self.chat.log(msg, wait)

    def log_fancy(self, msg, wait=False):
        self.chat.log(build_string(msg), wait)

    def say(self, msg, wait=False):
        self.chat.say(msg, wait)

    def title(self, title, subtitle, fade_in, remain, fade_out):
        self.chat.title(title, subtitle, fade_in, remain, fade_out)

    def actionbar(self, text, tinted=False):
        self.chat.actionbar(text, tinted)

    def toast(self, title, desc):
        self.chat.toast(title, desc)

    def string_to_text_helper(self, content):
        return self.chat.createTextHelperFromString(content)

    def get_logger(self, name=None):
        return self.chat.getLogger(name) if name else self.chat.getLogger()

    def json_to_text_helper(self, content):
        return self.chat.createTextHelperFromJSON(content)

    def create_text_builder(self):
        """Creates a text builder. Recommended to use log_fancy, as it has similar behavior but better semantics."""
        return self.chat.createTextBuilder()

    def create_command_builder(self):
        """Used for registering commands. Using utils_run.py is probably better."""
        return self.chat.createCommandBuilder()

    @property
    def history(self):
        """Returns a wrapped ChatHistoryManager object. If you want a raw object, use chat.raw_history."""
        return HistoryWrapper(self.raw_history)

    @property
    def raw_history(self):
        """Returns a raw ChatHistoryManager object. If you want a Wrapped object, use chat.history."""
        return self.chat.getHistory()

    def unwrap(self):
        """Returns the unwrapped Chat object."""
        return self.chat


class HistoryWrapper:
    def __init__(self, history):
        self.history = history

    def get_recv_line(self, index):
        return LineWrapper(self.history.getRecvLine(index))

    def insert_recv_text(self, index, line, time_ticks=0, do_refresh=True):
        """
        @type index: int
        @type line: TextHelper
        @type time_ticks: int
        @type do_refresh: bool
        """
        if not time_ticks:
            self.history.insertRecvText(index, line)
        else:
            self.history.insertRecvText(index, timeTicks)
            if do_refresh:
                self.refresh_visible()

    def remove_recv_text(self, index, wait=False):
        self.history.removeRecvText(index, wait)

    def remove_recv_text_matching(self, index, wait=False):
        self.history.removeRecvTextMatching(index, wait)

    def remove_recv_text_matching_filter(self, index, wait=False):
        self.history.removeRecvTextMatchingFilter(index, wait)

    def refresh_visible(self, wait=False):
        self.history.refreshVisible(wait)

    def clear_recv(self, wait=False):
        self.history.clearRecv(wait)

    @property
    def sent(self):
        return self.history.getSent()

    @property
    def messages(self):
        out = []
        i = 0
        while self.get_recv_line(i):
            # Chat.log(self.get_recv_line(i).getString())
            out.append(LineWrapper(self.get_recv_line(i)))
        # Chat.log("Out of Messages")
        return out

    def clear_sent(self, wait=False):
        self.history.clearSent(wait)


class LineWrapper:
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return self.text_string()

    def __repr__(self):
        return self.text.toString()

    @property
    def text(self):
        return self.line.getText()

    @property
    def text_string(self):
        return self.text.getString()

    @property
    def ID(self):
        return self.line.getId()

    @property
    def creation_tick(self):
        return self.line.getCreationTick()

    @property
    def msg_author(self):
        if '>' not in self.text_string:
            return None
        else:
            return self.text_string.split('>')[0][1:]

    @property
    def msg_content(self):
        if '>' not in self.text_string:
            return self.text_string
        else:
            return self.text_string.split('>')[1]

    def delete_by_id(self):
        self.line.deleteById()

    def unwrap(self):
        return self.line


class EventStub:
    def __init__(self, attr):
        self.attr = attr

    def getString(self, key):
        try:
            return self.attr[int(key)]
        except IndexError:
            return


def build_params(param, param_list):
    """Adds a list of parameters to an event, with numeric keys.
    Functionally the same as EventWrapper(param).put_numeric_list(param_list).

    @deprecated
    """
    for n, i in enumerate(param_list):
        param.putString(str(n), i)


def build_string(string):
    out = []
    prev = string[0]
    for i in string:
        if i == '&' and prev != '\\':
            out.append("§")
        elif i == '\\':
            pass
        else:
            out.append(i)
        prev = i
    return ''.join(out)


def dist_3d(x1, y1, z1, x2, y2, z2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    z1 = float(z1)
    z2 = float(z2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


def dist_2d(x1, z1, x2, z2):
    x1 = float(x1)
    x2 = float(x2)
    z1 = float(z1)
    z2 = float(z2)
    return ((x1 - x2) ** 2 + (z1 - z2) ** 2) ** 0.5


def pos_tuple(position):
    return position.x, position.y, position.z


def angle_look(playerObj, pitch, yaw, steps):
    current_pitch = playerObj.getPitch()
    current_yaw = playerObj.getYaw()
    step_pitch = (current_pitch - pitch) / steps

    if current_yaw - yaw >= 180:
        step_yaw = -(current_yaw - yaw - 180) / steps
    else:
        step_yaw = (current_yaw - yaw) / steps

    for x in range(1, steps):
        current_pitch = playerObj.getPitch()
        current_yaw = playerObj.getYaw()
        playerObj.lookAt(current_pitch - step_pitch, current_yaw - step_yaw)
        time.sleep(0.01)


def look_at(playerObj, x, y, z):
    vec = playerObj.getPos().add(0, playerObj.getEyeHeight(), 0).toVector().reverse().add(0, 0, 0, x, y, z)
    yaw = vec.getYaw()
    pitch = vec.getPitch()
    angle_look(playerObj, pitch, yaw, 10)
