from produce import fill_queue


def test_connection():
    fill_queue.get_connection()
    print("woho")
