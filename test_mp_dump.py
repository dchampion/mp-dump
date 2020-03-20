import mp_dump

URL_ROOT = 'https://www.mountainproject.com/data/'
ARG_0 = 'mp_dump.py'
MEMBER_KEY = 'abcd-1234'

def test_build_url():
    url = mp_dump.build_url([ARG_0, 'member', 'foo@bar.com', MEMBER_KEY])
    assert url == URL_ROOT + 'get-user?email=foo@bar.com&key=abcd-1234'

    url = mp_dump.build_url([ARG_0, 'ticks', 'foo@bar.com', MEMBER_KEY])
    assert url == URL_ROOT + 'get-ticks?email=foo@bar.com&key=abcd-1234'

    url = mp_dump.build_url([ARG_0, 'todos', 'foo@bar.com', MEMBER_KEY])
    assert url == URL_ROOT + 'get-to-dos?email=foo@bar.com&key=abcd-1234'

    url = mp_dump.build_url([ARG_0, 'routes', '105742085', MEMBER_KEY])
    assert url == URL_ROOT + 'get-routes?routeIds=105742085&key=abcd-1234'

    url = mp_dump.build_url([ARG_0, 'routes', '105742085', '105835842', MEMBER_KEY])
    assert url == URL_ROOT + 'get-routes?routeIds=105742085,105835842&key=abcd-1234'

    url = mp_dump.build_url([ARG_0, 'routes', '40.03', '-105.25', MEMBER_KEY])
    assert url == URL_ROOT + 'get-routes-for-lat-lon?lat=40.03&lon=-105.25&key=abcd-1234'

def test_build_id_str():
    id_str = mp_dump.build_id_str([ARG_0, 'routes', '105742085', MEMBER_KEY])
    assert id_str == '105742085'

    id_str = mp_dump.build_id_str([ARG_0, 'routes', '105742085', '105835842', MEMBER_KEY])
    assert id_str == '105742085,105835842'

def test_lat_lon():
    assert mp_dump.lat_lon([ARG_0, 'routes', '40.03', '-105.25', MEMBER_KEY])
    assert mp_dump.lat_lon([ARG_0, 'routes', '40', '-105.25', MEMBER_KEY])
    assert mp_dump.lat_lon([ARG_0, 'routes', '40.03', '-105', MEMBER_KEY])
    assert not mp_dump.lat_lon([ARG_0, 'routes', '40', '-105', MEMBER_KEY])
