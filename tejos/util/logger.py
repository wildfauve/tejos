from typing import Dict, Optional, Union, Tuple
# from pino import pino
# import sys
# from functools import reduce
import time

# public interface
def with_perf_log(perf_log_type: str = None, name: str = None):
    """
    Decorator which wraps the fn in a timer and writes a performance log
    """
    def inner(fn):
        def invoke(*args, **kwargs):
            t1 = time.time()
            result = fn(*args, **kwargs)
            t2 = time.time()
            fn_name = kwargs['name'] if 'name' in kwargs else name or fn.__name__
            perf_log(fn=f"{fn_name} ctx: {kwargs.get('perf_ctx', None)}", delta_t=(t2-t1)*1000.0)
            return result
        return invoke
    return inner


def perf_log(fn: str, delta_t: float):
    print(f"PerfLog: delta_t: {delta_t}, fn: {fn}")
