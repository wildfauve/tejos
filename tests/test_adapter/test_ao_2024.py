from tejos import adapter

class Event:
    ...
def test_parse_draw():
    result = adapter.ao_draw_parser.build_draw(event=Event, for_rd=1, scores_only=False, full_draw=True)