import resource

PAGE_SIZE = resource.getpagesize()
FIELDS = ('vsz',  # vm size
          'rss',  # resident set size
          'shr',  # share size
          'text', # code size
          'lib',  # lib size
          'data', # data + stack
          'dt')   # dirty size

def pages_to_kb(num):
    return int(num) * PAGE_SIZE / 1024

def stats_in_kb():
    statm = open('/proc/self/statm').read().strip()
    int_fields = map(pages_to_kb, statm.split())
    return dict(zip(FIELDS, int_fields))

if __name__ == '__main__':
    import pprint
    pprint.pprint(stats_in_kb())
