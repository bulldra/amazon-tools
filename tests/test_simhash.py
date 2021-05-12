import simhash
import logzero
import settings
import kindle_util

class a:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __eq__(self, other):
        return self.a + self.b == other.a + other.b
    def __hash__(self):
        return hash(self.a + self.b)
    def __lt__(self, other):
        return self.c < other.c
    def __gt__(self, other):
        return self.c > other.c


def test_simset():
    logzero.logfile(
        settings.settings_dict['logfile'],
        loglevel=20,
        maxBytes=1e6,
        backupCount=3
    )
    log = logzero.logger

    value = settings.load_text_list('../work/kindle_lib_title.txt')[0:100]

    result = set()
    for v1 in value:
        for v2 in value:
            x = simhash.Simhash(kindle_util.tlanslate_series_title(v1))
            y = simhash.Simhash(kindle_util.tlanslate_series_title(v2))
            result.add(a(v1, v2, x.distance(y)))

#    for x in sorted(result):
#        log.info(f'{x.a} {x.b} {x.c}')
