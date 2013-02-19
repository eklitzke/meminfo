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
    return num * PAGE_SIZE / 1024

def stats_in_kb():
    statm = open('/proc/self/statm').read().strip()
    return dict(zip(FIELDS, statm.split()))

print stats_in_kb()
